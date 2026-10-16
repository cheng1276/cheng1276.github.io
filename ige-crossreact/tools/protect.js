#!/usr/bin/env node
/*
 * IgE 交叉反應判讀器：密碼保護工具（只用 Node 內建模組）
 *
 * 公開儲存庫裡只放加密後的檔案：
 *   index.html  密碼畫面＋加密的網頁（瀏覽器以 Web Crypto 解密）
 *   source.enc  加密的原始檔（src/ 整個資料夾）
 *
 * 用法（密碼從環境變數 IGE_PASSWORD 讀取；沒有設定時會在終端機詢問）：
 *   node tools/protect.js unpack            把 source.enc 解密還原成 src/
 *   node tools/protect.js page [檔案]        把 build.py 產生的網頁（預設 build/page.html）加密成 index.html
 *   node tools/protect.js pack              把 src/ 加密打包成 source.enc
 *   node tools/protect.js check             確認密碼能解開 index.html 與 source.enc
 *
 * 選項：
 *   --new-password  換密碼時使用（page 與 pack 都要加）。沒有加的話，密碼必須能解開現有的
 *                   source.enc，避免打錯字把網頁鎖住。
 *   --force         unpack 時覆寫內容不同的 src/ 檔案。
 *
 * 加密方式：PBKDF2-HMAC-SHA256（600,000 次）導出 256 位元金鑰，以 AES-256-GCM 加密；
 * IV 每次重新產生；index.html 在密碼不變時沿用 salt，換密碼時才換新。密碼本身不會寫入任何檔案。
 */
'use strict';
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const zlib = require('zlib');
const readline = require('readline');

const ROOT = path.resolve(__dirname, '..');
const SRC = path.join(ROOT, 'src');
const SOURCE_ENC = path.join(ROOT, 'source.enc');
const INDEX = path.join(ROOT, 'index.html');
const GATE = path.join(__dirname, 'gate.tpl');
const DEFAULT_PAGE = path.join(ROOT, 'build', 'page.html');
const ITER = 600000;

const die = msg => { console.error('錯誤：' + msg); process.exit(1); };

function deriveKey(password, salt, iter) {
  return crypto.pbkdf2Sync(Buffer.from(password.normalize('NFC'), 'utf8'), salt, iter, 32, 'sha256');
}

// salt 沿用時，密碼不變則金鑰不變：網頁更新後，勾選「記住密碼」的裝置仍可直接開啟
function encrypt(password, plain, salt = crypto.randomBytes(16)) {
  const iv = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv('aes-256-gcm', deriveKey(password, salt, ITER), iv);
  // Web Crypto 的 AES-GCM 期待「密文＋16 位元組驗證標籤」連在一起
  const ct = Buffer.concat([cipher.update(plain), cipher.final(), cipher.getAuthTag()]);
  return { v: 1, kdf: 'PBKDF2-SHA256', iter: ITER, salt: salt.toString('base64'), iv: iv.toString('base64'), ct: ct.toString('base64') };
}

function decrypt(password, box) {
  const all = Buffer.from(box.ct, 'base64');
  const decipher = crypto.createDecipheriv('aes-256-gcm', deriveKey(password, Buffer.from(box.salt, 'base64'), box.iter), Buffer.from(box.iv, 'base64'));
  decipher.setAuthTag(all.subarray(all.length - 16));
  return Buffer.concat([decipher.update(all.subarray(0, all.length - 16)), decipher.final()]); // 密碼錯誤時會丟出例外
}

function tryDecrypt(password, box) {
  if (!box) return null;
  try { return decrypt(password, box); } catch (e) { return null; }
}

/* ---------- 密碼輸入 ---------- */
function ask(question) {
  return new Promise(resolve => {
    const rl = readline.createInterface({ input: process.stdin, output: process.stdout, terminal: !!process.stdin.isTTY });
    if (process.stdin.isTTY) rl._writeToOutput = s => { if (s.includes(question)) rl.output.write(question); }; // 不顯示輸入的字
    rl.question(question, answer => { rl.close(); if (process.stdin.isTTY) process.stdout.write('\n'); resolve(answer); });
  });
}

async function getPassword({ confirm = false } = {}) {
  let pw = process.env.IGE_PASSWORD;
  if (pw == null) {
    pw = await ask('密碼：');
    if (confirm && (await ask('再輸入一次新密碼：')) !== pw) die('兩次輸入的密碼不同');
  }
  pw = pw.trim();
  if (!pw) die('密碼不能是空的');
  return pw;
}

/* 沒有 --new-password 時，密碼必須能解開現有的 source.enc */
function assertSamePassword(pw, flags) {
  if (flags.has('--new-password') || !fs.existsSync(SOURCE_ENC)) return;
  if (!tryDecrypt(pw, readBox(SOURCE_ENC))) die('密碼無法解開現有的 source.enc。若要更換密碼，請在 page 與 pack 都加上 --new-password。');
}

/* ---------- 檔案格式 ---------- */
function readBox(file) {
  const text = fs.readFileSync(file, 'utf8');
  if (file.endsWith('.html')) {
    const m = text.match(/<script id="payload" type="application\/json">([\s\S]*?)<\/script>/);
    return m ? JSON.parse(m[1]) : null; // 尚未加密的舊版 index.html 沒有加密內容
  }
  return JSON.parse(text);
}

function listFiles(dir, base = dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap(d => {
    if (d.name === '__pycache__' || d.name.endsWith('.pyc') || d.name.startsWith('.')) return [];
    const full = path.join(dir, d.name);
    return d.isDirectory() ? listFiles(full, base) : [path.relative(base, full).split(path.sep).join('/')];
  }).sort();
}

function packSource() {
  if (!fs.existsSync(SRC)) die('找不到 src/，請先執行 unpack');
  const files = {};
  for (const rel of listFiles(SRC)) files[rel] = fs.readFileSync(path.join(SRC, rel)).toString('base64');
  return files;
}

function unpackSource(buf) {
  return JSON.parse(zlib.gunzipSync(buf).toString('utf8')).files;
}

const sameFiles = (a, b) => JSON.stringify(Object.entries(a).sort()) === JSON.stringify(Object.entries(b).sort());

/* ---------- 指令 ---------- */
async function cmdPage(args, flags) {
  const file = args[0] ? path.resolve(args[0]) : DEFAULT_PAGE;
  if (!fs.existsSync(file)) die(`找不到 ${file}；請先執行 python3 src/build.py`);
  const plain = fs.readFileSync(file);
  const pw = await getPassword({ confirm: flags.has('--new-password') });
  assertSamePassword(pw, flags);
  const tpl = fs.readFileSync(GATE, 'utf8');
  if (!tpl.includes('__PAYLOAD__')) die('gate.tpl 缺少 __PAYLOAD__');
  let salt;
  if (!flags.has('--new-password') && fs.existsSync(INDEX)) {
    const current = fs.readFileSync(INDEX, 'utf8');
    const box = readBox(INDEX);
    const old = tryDecrypt(pw, box);
    const sameGate = current.replace(/(<script id="payload" type="application\/json">)[\s\S]*?(<\/script>)/, '$1__PAYLOAD__$2') === tpl;
    if (old && old.equals(plain) && sameGate) { console.log('index.html 內容沒有變更，不重新加密'); return; }
    if (old && box.iter === ITER) salt = Buffer.from(box.salt, 'base64'); // 同一密碼沿用 salt，IV 每次重新產生
  }
  fs.writeFileSync(INDEX, tpl.replace('__PAYLOAD__', JSON.stringify(encrypt(pw, plain, salt))));
  console.log(`已加密 ${path.relative(process.cwd(), file)} → index.html（${fs.statSync(INDEX).size} bytes）`);
}

async function cmdPack(args, flags) {
  const files = packSource();
  const pw = await getPassword({ confirm: flags.has('--new-password') });
  assertSamePassword(pw, flags);
  if (!flags.has('--new-password') && fs.existsSync(SOURCE_ENC)) {
    const old = tryDecrypt(pw, readBox(SOURCE_ENC));
    if (old && sameFiles(unpackSource(old), files)) { console.log('src/ 沒有變更，不重新打包'); return; }
  }
  const plain = zlib.gzipSync(Buffer.from(JSON.stringify({ v: 1, files })), { level: 9 });
  fs.writeFileSync(SOURCE_ENC, JSON.stringify(encrypt(pw, plain)) + '\n');
  console.log(`已加密 ${Object.keys(files).length} 個檔案 → source.enc（${fs.statSync(SOURCE_ENC).size} bytes）`);
}

async function cmdUnpack(args, flags) {
  if (!fs.existsSync(SOURCE_ENC)) die('找不到 source.enc');
  const pw = await getPassword();
  const buf = tryDecrypt(pw, readBox(SOURCE_ENC));
  if (!buf) die('密碼不正確');
  const files = unpackSource(buf);
  const conflicts = Object.keys(files).filter(rel => {
    const target = path.join(SRC, rel);
    return fs.existsSync(target) && !fs.readFileSync(target).equals(Buffer.from(files[rel], 'base64'));
  });
  if (conflicts.length && !flags.has('--force')) die(`src/ 裡這些檔案和 source.enc 不同，未覆寫（加 --force 可覆寫）：\n  ${conflicts.join('\n  ')}`);
  for (const [rel, b64] of Object.entries(files)) {
    const target = path.join(SRC, rel);
    fs.mkdirSync(path.dirname(target), { recursive: true });
    fs.writeFileSync(target, Buffer.from(b64, 'base64'));
  }
  console.log(`已還原 ${Object.keys(files).length} 個檔案到 src/`);
}

async function cmdCheck() {
  const pw = await getPassword();
  let ok = true;
  for (const [name, file] of [['index.html', INDEX], ['source.enc', SOURCE_ENC]]) {
    if (!fs.existsSync(file)) { console.log(`${name}：不存在`); ok = false; continue; }
    const box = readBox(file);
    if (!box) { console.log(`${name}：沒有加密內容`); ok = false; continue; }
    const buf = tryDecrypt(pw, box);
    console.log(`${name}：${buf ? `可解開（${buf.length} bytes）` : '密碼無法解開'}`);
    if (!buf) ok = false;
  }
  process.exit(ok ? 0 : 1);
}

const COMMANDS = { page: cmdPage, pack: cmdPack, unpack: cmdUnpack, check: cmdCheck };
const argv = process.argv.slice(2);
const cmd = COMMANDS[argv[0]];
if (!cmd) { console.log(fs.readFileSync(__filename, 'utf8').split('*/')[0].replace(/^#!.*\n\/\*\n?/, '').replace(/^ \* ?/gm, '')); process.exit(argv[0] ? 1 : 0); }
cmd(argv.slice(1).filter(a => !a.startsWith('--')), new Set(argv.filter(a => a.startsWith('--')))).catch(e => die(e.message));
