<!doctype html>
<html lang="zh-Hant-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<title>IgE 交叉反應判讀器</title>
<meta name="description" content="輸入 BioIC 等多重過敏原報告，依陽性組合推測哪些可能來自 CCD、profilin、tropomyosin 等共同結構的交叉反應。此頁面需要密碼才能開啟。">
<meta property="og:type" content="website">
<meta property="og:title" content="IgE 交叉反應判讀器">
<meta property="og:description" content="多重過敏原檢測的交叉反應判讀工具。此頁面需要密碼才能開啟。">
<meta property="og:url" content="https://cheng1276.github.io/ige-crossreact/">
<link rel="canonical" href="https://cheng1276.github.io/ige-crossreact/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&amp;family=Noto+Serif+TC:wght@700&amp;display=swap">
<style>
:root {
  --bg: #f1f3f8; --panel: #ffffff; --panel-2: #e9edf5;
  --ink: #131a27; --ink-2: #4b566a; --ink-3: #788398; --line: #d4dae6;
  --tmb: #2340c4; --tmb-ink: #ffffff; --tmb-soft: #e3e8ff;
  --bad: #b42318; --bad-bg: #fdece9;
  --shadow: 0 1px 2px rgba(19, 26, 39, .06), 0 10px 30px rgba(19, 26, 39, .07);
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #0c1017; --panel: #141a24; --panel-2: #1b2230;
    --ink: #e6eaf2; --ink-2: #a5afc1; --ink-3: #7d889c; --line: #283142;
    --tmb: #8099ff; --tmb-ink: #0c1017; --tmb-soft: #1c2546;
    --bad: #ff8b7b; --bad-bg: #3a1613;
    --shadow: 0 1px 2px rgba(0, 0, 0, .4), 0 10px 30px rgba(0, 0, 0, .3);
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --bg: #0c1017; --panel: #141a24; --panel-2: #1b2230;
  --ink: #e6eaf2; --ink-2: #a5afc1; --ink-3: #7d889c; --line: #283142;
  --tmb: #8099ff; --tmb-ink: #0c1017; --tmb-soft: #1c2546;
  --bad: #ff8b7b; --bad-bg: #3a1613;
  --shadow: 0 1px 2px rgba(0, 0, 0, .4), 0 10px 30px rgba(0, 0, 0, .3);
  color-scheme: dark;
}
* { box-sizing: border-box; }
[hidden] { display: none !important; }
html, body { margin: 0; }
body {
  min-height: 100vh; min-height: 100dvh;
  display: grid; place-items: center;
  padding-block: max(24px, env(safe-area-inset-top, 0px)) max(24px, env(safe-area-inset-bottom, 0px));
  padding-left: max(16px, env(safe-area-inset-left, 0px));
  padding-right: max(16px, env(safe-area-inset-right, 0px));
  background: var(--bg); color: var(--ink);
  font: 15px/1.6 "PingFang TC", "Noto Sans TC", "Microsoft JhengHei", "Heiti TC", system-ui, sans-serif;
}
.unlocking .gate { visibility: hidden; }
.gate {
  width: min(100%, 400px);
  background: var(--panel); border: 1px solid var(--line); border-radius: 14px; box-shadow: var(--shadow);
  padding: 26px 24px 20px;
  display: flex; flex-direction: column; gap: 18px;
}
.head { display: flex; gap: 14px; align-items: center; }
.plate {
  flex: none; display: grid; grid-template-columns: repeat(4, 11px); gap: 5px;
  padding: 8px; border-radius: 10px; background: var(--panel-2); border: 1px solid var(--line);
}
.plate i { width: 11px; height: 11px; border-radius: 50%; background: var(--tmb); }
h1 { margin: 0; font: 700 1.32rem/1.3 "Noto Serif TC", "Songti TC", "PMingLiU", serif; text-wrap: balance; }
.sub { margin: 2px 0 0; color: var(--ink-2); font-size: .9rem; }
form { display: flex; flex-direction: column; gap: 12px; }
.field { display: flex; flex-direction: column; gap: 6px; font-size: .82rem; color: var(--ink-2); }
input[type="password"] {
  font: inherit; font-size: 1.05rem; letter-spacing: .06em;
  width: 100%; padding: 11px 12px; border-radius: 10px;
  border: 1px solid var(--line); background: var(--bg); color: var(--ink);
}
.check { display: flex; gap: 8px; align-items: flex-start; font-size: .84rem; color: var(--ink-2); }
.check input { margin: 4px 0 0; accent-color: var(--tmb); }
button {
  font: inherit; font-weight: 700; padding: 11px 14px; border-radius: 10px; border: 0;
  background: var(--tmb); color: var(--tmb-ink); cursor: pointer;
}
button[disabled] { opacity: .65; cursor: progress; }
input:focus-visible, button:focus-visible { outline: 2px solid var(--tmb); outline-offset: 2px; }
.msg { margin: 0; min-height: 1.5em; font-size: .86rem; color: var(--ink-3); }
.msg.bad { color: var(--bad); }
.foot { margin: 0; padding-top: 12px; border-top: 1px solid var(--line); font-size: .76rem; color: var(--ink-3); }
</style>
</head>
<body>
<main class="gate">
  <div class="head">
    <div class="plate" aria-hidden="true"><i style="opacity:.12"></i><i style="opacity:.3"></i><i style="opacity:.55"></i><i style="opacity:.9"></i><i style="opacity:.2"></i><i style="opacity:.75"></i><i style="opacity:.08"></i><i style="opacity:.42"></i></div>
    <div>
      <h1>IgE 交叉反應判讀器</h1>
      <p class="sub">此頁面需要密碼才能開啟</p>
    </div>
  </div>
  <form id="f">
    <label class="field">密碼
      <input type="password" id="pw" name="password" autocomplete="current-password" required>
    </label>
    <label class="check"><input type="checkbox" id="remember"> 在這台裝置記住密碼（共用電腦請勿勾選）</label>
    <button type="submit" id="go">開啟</button>
    <p class="msg" id="msg" role="status" aria-live="polite"></p>
  </form>
  <noscript><p class="msg bad">需要啟用 JavaScript 才能開啟此頁面。</p></noscript>
  <p class="foot">密碼只在你的瀏覽器中用來解密頁面，不會傳送到任何伺服器。</p>
</main>
<script id="payload" type="application/json">__PAYLOAD__</script>
<script>
(function () {
  'use strict';
  var KEY = 'ige-crossreact-unlock';
  var box = JSON.parse(document.getElementById('payload').textContent);
  var $ = function (id) { return document.getElementById(id); };
  var fromB64 = function (s) { return Uint8Array.from(atob(s), function (c) { return c.charCodeAt(0); }); };
  var toB64 = function (buf) { var b = new Uint8Array(buf), s = ''; for (var i = 0; i < b.length; i++) s += String.fromCharCode(b[i]); return btoa(s); };
  var stores = function () {
    var out = [];
    try { if (window.sessionStorage) out.push(window.sessionStorage); } catch (e) {}
    try { if (window.localStorage) out.push(window.localStorage); } catch (e) {}
    return out;
  };
  var saved = {
    get: function () {
      var list = stores();
      for (var i = 0; i < list.length; i++) {
        try { var v = JSON.parse(list[i].getItem(KEY) || 'null'); if (v && v.salt === box.salt && v.k) return v.k; } catch (e) {}
      }
      return null;
    },
    set: function (k, remember) {
      var v = JSON.stringify({ salt: box.salt, k: k });
      try { window.sessionStorage.setItem(KEY, v); } catch (e) {}
      try { if (remember) window.localStorage.setItem(KEY, v); else window.localStorage.removeItem(KEY); } catch (e) {}
    },
    clear: function () { stores().forEach(function (s) { try { s.removeItem(KEY); } catch (e) {} }); }
  };
  var msg = function (text, bad) { $('msg').textContent = text; $('msg').className = bad ? 'msg bad' : 'msg'; };

  function deriveBits(password) {
    var enc = new TextEncoder().encode(password.normalize('NFC'));
    return crypto.subtle.importKey('raw', enc, 'PBKDF2', false, ['deriveBits']).then(function (base) {
      return crypto.subtle.deriveBits({ name: 'PBKDF2', salt: fromB64(box.salt), iterations: box.iter, hash: 'SHA-256' }, base, 256);
    });
  }
  function decrypt(bits) {
    return crypto.subtle.importKey('raw', bits, 'AES-GCM', false, ['decrypt']).then(function (key) {
      return crypto.subtle.decrypt({ name: 'AES-GCM', iv: fromB64(box.iv) }, key, fromB64(box.ct));
    }).then(function (plain) { return new TextDecoder().decode(plain); });
  }
  // 解密後以完整頁面取代這個密碼畫面，並在頁尾加上「鎖定」連結
  function addLock() {
    var foot = document.querySelector('footer.foot');
    if (!foot || foot.querySelector('.ige-lock')) return;
    var p = document.createElement('p');
    var a = document.createElement('a');
    a.href = '#'; a.className = 'ige-lock'; a.textContent = '鎖定此頁（下次開啟需重新輸入密碼）';
    a.addEventListener('click', function (e) { e.preventDefault(); saved.clear(); location.reload(); });
    p.appendChild(a);
    foot.appendChild(p);
  }
  function show(html) {
    document.open();
    document.write(html);
    document.close();
    // 頁面可能還在解析（例如等待樣式表），等解析完成再加連結
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', addLock);
    else addLock();
  }

  if (!window.crypto || !crypto.subtle || !window.TextEncoder) {
    msg('這個瀏覽器無法解密，請改用較新版本的 Chrome、Safari 或 Edge 開啟。', true);
    $('go').disabled = true;
    return;
  }

  var k = saved.get();
  if (k) {
    document.documentElement.classList.add('unlocking');
    decrypt(fromB64(k)).then(show).catch(function () {
      saved.clear();
      document.documentElement.classList.remove('unlocking');
    });
  }

  $('f').addEventListener('submit', function (e) {
    e.preventDefault();
    var pw = $('pw').value.trim();
    if (!pw) return;
    $('go').disabled = true;
    msg('解密中…');
    deriveBits(pw).then(function (bits) {
      return decrypt(bits).then(function (html) {
        saved.set(toB64(bits), $('remember').checked);
        show(html);
      });
    }).catch(function () {
      $('go').disabled = false;
      msg('密碼不正確，請再試一次。', true);
      $('pw').select();
    });
  });
})();
</script>
</body>
</html>
