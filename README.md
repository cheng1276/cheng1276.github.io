<html lang="zh-Hant-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>血脂治療決策工具｜台灣 2025 血脂管理臨床路徑共識 × 健保降血脂藥物給付（表一 115/9/1 新制／表二原規定）× ACC/AHA 2026 statin 強度</title>
<meta name="description" content="輸入病患特徵，依 2025 台灣血脂管理臨床路徑共識判定 ASCVD 風險分級、LDL-C 目標、statin/non-statin 用藥建議，並比對 115/9/1 修訂後健保降血脂藥物給付規定（表一）、原給付規定（表二，適用不適用表一之品項）與 PCSK9 給付規定；附 2026 ACC/AHA statin 強度分類表。">
<style>
:root{
  --bg:#F3F5F7; --paper:#FFFFFF; --ink:#1A2330; --ink-2:#3B4756; --muted:#66727F;
  --line:#DCE1E7; --line-2:#EDF0F3;
  --brand:#0B5563; --brand-ink:#083F4A; --brand-soft:#E4F0F2; --brand-tint:#F1F7F8;
  --ok:#1E7A4C; --ok-soft:#E4F4EA; --warn:#8A5A00; --warn-soft:#FBF1D9; --no:#B3261E; --no-soft:#FCE8E6; --info:#1F4FA3; --info-soft:#E7EEFA; --na:#66727F; --na-soft:#EEF1F4;
  --r-ext:#9E1B2A; --r-vh:#C0510C; --r-h:#1F4FA3; --r-m:#0E7C6E; --r-l:#557A16; --r-z:#6B7280;
  --mono: ui-monospace,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace;
  --sans: "Noto Sans TC","PingFang TC","Heiti TC","Microsoft JhengHei","Segoe UI",Roboto,system-ui,-apple-system,sans-serif;
  --radius:10px; --shadow:0 1px 2px rgba(16,24,40,.06),0 1px 3px rgba(16,24,40,.08);
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:15px;line-height:1.6;}
a{color:var(--brand)}
button{font-family:inherit}
code,.mono{font-family:var(--mono);font-size:.92em}
h1,h2,h3,h4{margin:0;line-height:1.3}
p{margin:.35em 0}
ul,ol{margin:.35em 0;padding-left:1.4em}
li{margin:.15em 0}
small{font-size:.86em}
.muted{color:var(--muted)}
.hide{display:none !important}
:focus-visible{outline:2px solid var(--brand);outline-offset:2px}

/* ---------- Header ---------- */
.hdr{background:var(--paper);border-bottom:1px solid var(--line);border-top:4px solid var(--brand)}
.hdr-in{max-width:1280px;margin:0 auto;padding:16px 20px 10px}
.hdr h1{font-size:20px;font-weight:700;letter-spacing:.02em;color:var(--brand-ink)}
.hdr .sub{color:var(--muted);font-size:13px;margin-top:2px}
.src-badges{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.badge{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);border-radius:999px;padding:3px 10px;font-size:12px;color:var(--ink-2);background:var(--bg)}
.badge b{font-weight:600;color:var(--brand-ink);white-space:nowrap}
.badge .dot{width:7px;height:7px;border-radius:50%;background:var(--brand)}
.tabs{max-width:1280px;margin:0 auto;padding:0 12px;display:flex;gap:2px;overflow-x:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch}
.tabs::-webkit-scrollbar{display:none}
.tab{appearance:none;background:none;border:0;border-bottom:3px solid transparent;padding:10px 12px;font-size:14px;color:var(--ink-2);white-space:nowrap;cursor:pointer;font-weight:500}
.tab[aria-selected="true"]{color:var(--brand-ink);border-bottom-color:var(--brand);font-weight:700}
.tab:hover{color:var(--brand-ink)}

/* ---------- Layout ---------- */
main{max-width:1280px;margin:0 auto;padding:16px 16px 96px}
.panel{display:none}
.panel.active{display:block}
.grid{display:grid;grid-template-columns:minmax(0,1fr);gap:16px}
.col-form,.col-result{min-width:0}
@media (min-width:1024px){
  .grid{grid-template-columns:minmax(0,46fr) minmax(0,54fr);align-items:start}
  .col-result{position:sticky;top:12px;max-height:calc(100vh - 24px);overflow:auto;padding-right:6px;scrollbar-gutter:stable;scrollbar-width:thin;scrollbar-color:#B9C2CC transparent}
  .col-result::-webkit-scrollbar{width:8px}
  .col-result::-webkit-scrollbar-thumb{background:#B9C2CC;border-radius:8px}
  main{padding-bottom:32px}
}
.card{background:var(--paper);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:16px 18px;margin-bottom:14px}
.card h2{font-size:16px;font-weight:700;color:var(--brand-ink);display:flex;align-items:center;gap:10px}
.step-no{display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:50%;background:var(--brand);color:#fff;font-size:13px;font-weight:700;flex:none;font-family:var(--mono)}
.card .hint{font-size:12.5px;color:var(--muted);margin:2px 0 10px 34px}
.notice{border-radius:8px;padding:10px 12px;font-size:13px;line-height:1.55;margin:10px 0;border:1px solid}
.notice.info{background:var(--info-soft);border-color:#C9D8F5;color:#173C7A}
.notice.warn{background:var(--warn-soft);border-color:#EED9A0;color:#5C3D00}
.notice.no{background:var(--no-soft);border-color:#F3C4C0;color:#7A1A14}
.notice.ok{background:var(--ok-soft);border-color:#BFE3CC;color:#155235}

/* ---------- Form controls ---------- */
.field-row{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 14px}
@media (min-width:560px){.field-row.four{grid-template-columns:repeat(4,minmax(0,1fr))}}
.field label,.field .lbl{display:block;font-size:12.5px;color:var(--ink-2);font-weight:600;margin-bottom:4px}
.field label .u{font-weight:400;color:var(--muted)}
.inp{position:relative;display:flex;align-items:center}
.inp input[type=number],.inp input[type=text],.inp select{width:100%;border:1px solid var(--line);border-radius:8px;padding:9px 10px;font-size:16px;font-family:var(--mono);color:var(--ink);background:#fff;min-height:42px}
.inp input[type=text]{font-family:var(--sans);font-size:15px}
.inp select{font-family:var(--sans);font-size:14.5px;appearance:none;-webkit-appearance:none;padding-right:28px;background-image:linear-gradient(45deg,transparent 50%,var(--muted) 50%),linear-gradient(135deg,var(--muted) 50%,transparent 50%);background-position:calc(100% - 15px) 18px,calc(100% - 10px) 18px;background-size:5px 5px,5px 5px;background-repeat:no-repeat}
.inp .unit{position:absolute;right:10px;font-size:11.5px;color:var(--muted);pointer-events:none;background:#fff;padding-left:4px}
.inp input:focus,.inp select:focus{border-color:var(--brand);box-shadow:0 0 0 3px var(--brand-soft);outline:none}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:8px;overflow:hidden;background:#fff}
.seg button{appearance:none;border:0;background:none;padding:8px 14px;font-size:14px;color:var(--ink-2);cursor:pointer;min-height:40px;border-right:1px solid var(--line)}
.seg button:last-child{border-right:0}
.seg button[aria-pressed="true"]{background:var(--brand);color:#fff;font-weight:600}
.seg.wrap{flex-wrap:wrap}
.seg.block{display:flex}
.seg.block button{flex:1}
.chk-group{display:flex;flex-direction:column;gap:2px;margin-top:6px}
.chk-group + .chk-group{margin-top:12px}
.grp-title{font-size:12.5px;font-weight:700;color:var(--muted);letter-spacing:.04em;text-transform:uppercase;margin:10px 0 2px}
.chk{display:flex;align-items:flex-start;gap:10px;padding:8px 8px;border-radius:8px;cursor:pointer;min-height:40px;position:relative}
.chk:hover{background:var(--brand-tint)}
.chk input{position:absolute;opacity:0;pointer-events:none}
.chk .box{flex:none;width:20px;height:20px;border:2px solid #9AA5B1;border-radius:5px;margin-top:2px;display:inline-flex;align-items:center;justify-content:center;background:#fff;transition:background .12s,border-color .12s}
.chk .box::after{content:"";width:6px;height:11px;border:solid #fff;border-width:0 2.5px 2.5px 0;transform:rotate(45deg) translate(-1px,-1px);opacity:0}
.chk input:checked + .box{background:var(--brand);border-color:var(--brand)}
.chk input:checked + .box::after{opacity:1}
.chk input:focus-visible + .box{outline:2px solid var(--brand);outline-offset:2px}
.chk.auto .box{background:var(--brand-soft);border-color:var(--brand)}
.chk.auto input:checked + .box{background:var(--brand)}
.chk .txt{font-size:14.5px;line-height:1.45}
.chk .txt small{display:block;color:var(--muted);font-size:12.5px;margin-top:1px}
.chk .tag{display:inline-block;font-size:11px;padding:1px 6px;border-radius:4px;background:var(--brand-soft);color:var(--brand-ink);margin-left:6px;vertical-align:middle;font-weight:600}
.sub{margin-left:26px;border-left:2px solid var(--line-2);padding-left:6px}
.sub .sub{margin-left:22px}
.chk.disabled{opacity:.6;cursor:default}
.inline-note{font-size:12.5px;color:var(--muted);margin:2px 0 4px 8px}
.rf-status{font-size:12.5px;padding:2px 8px;border-radius:999px;background:var(--na-soft);color:var(--muted);margin-left:auto;white-space:nowrap;align-self:center}
.rf-status.on{background:var(--ok-soft);color:var(--ok)}
.rf-status.unk{background:var(--warn-soft);color:var(--warn)}
.tx-block{border:1px solid var(--line-2);border-radius:8px;padding:10px 12px;margin-top:10px;background:var(--brand-tint)}
.tx-block h4{font-size:13.5px;color:var(--brand-ink);margin-bottom:6px}
.btn{appearance:none;border:1px solid var(--line);background:#fff;color:var(--ink);border-radius:8px;padding:9px 14px;font-size:14px;cursor:pointer;min-height:40px;font-weight:600}
.btn:hover{border-color:var(--brand);color:var(--brand-ink)}
.btn.primary{background:var(--brand);border-color:var(--brand);color:#fff}
.btn.primary:hover{background:var(--brand-ink)}
.btn.small{padding:6px 10px;font-size:13px;min-height:34px}
.actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
.search-box{margin-top:6px}
.search-res{margin-top:6px;font-size:13.5px}
.search-res .hit{padding:6px 8px;border-radius:6px;background:var(--bg);margin-top:4px;display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.search-res .hit code{font-size:12.5px}
.search-res .hit .btn{margin-left:auto}
.prod-sel{margin-top:8px;border:1px solid var(--line);border-radius:8px;padding:8px 10px;background:#fff;font-size:13.5px;display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.prod-sel .nm{font-weight:700}
.prod-sel code{font-size:12.5px}
.prod-sel.t2{border-color:#F3C4C0;background:#FFF7F6}
.prod-sel.t1{border-color:#BFE3CC;background:#F4FBF6}
.pill{display:inline-block;font-size:11.5px;padding:2px 8px;border-radius:999px;font-weight:600;white-space:nowrap}
.pill.no{background:var(--no-soft);color:var(--no)}
.pill.warn{background:var(--warn-soft);color:var(--warn)}
.pill.ok{background:var(--ok-soft);color:var(--ok)}
.pill.info{background:var(--info-soft);color:var(--info)}
.pill.na{background:var(--na-soft);color:var(--na)}

/* ---------- Result ---------- */
.res-empty{color:var(--muted);text-align:center;padding:26px 10px;font-size:14px}
.risk{border-left:6px solid var(--r-z);border-radius:var(--radius);padding:14px 16px;background:var(--paper);border:1px solid var(--line);border-left-width:6px;box-shadow:var(--shadow);margin-bottom:14px}
.risk .eyebrow{font-size:12px;letter-spacing:.06em;color:var(--muted);font-weight:700}
.risk .name{font-size:26px;font-weight:800;line-height:1.2;margin:2px 0 4px}
.risk .why{font-size:13.5px;color:var(--ink-2)}
.risk .why ul{margin:4px 0 0;padding-left:1.2em}
.risk.t-EXT{border-left-color:var(--r-ext)}.risk.t-EXT .name{color:var(--r-ext)}
.risk.t-VH{border-left-color:var(--r-vh)}.risk.t-VH .name{color:var(--r-vh)}
.risk.t-H{border-left-color:var(--r-h)}.risk.t-H .name{color:var(--r-h)}
.risk.t-M{border-left-color:var(--r-m)}.risk.t-M .name{color:var(--r-m)}
.risk.t-L{border-left-color:var(--r-l)}.risk.t-L .name{color:var(--r-l)}
.risk.t-Z{border-left-color:var(--r-z)}.risk.t-Z .name{color:var(--r-z)}
.readouts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:6px 0 10px}
@media (max-width:420px){.readouts{grid-template-columns:repeat(2,minmax(0,1fr))}}
.ro{border:1px solid var(--line-2);border-radius:8px;padding:8px 10px;background:var(--bg)}
.ro .k{font-size:11.5px;color:var(--muted);font-weight:600;letter-spacing:.03em}
.ro .v{font-family:var(--mono);font-size:22px;font-weight:700;line-height:1.2;color:var(--ink)}
.ro .v small{font-size:11px;font-weight:500;color:var(--muted);font-family:var(--sans)}
.ro.goal-ok .v{color:var(--ok)}
.ro.goal-no .v{color:var(--no)}
.ruler-wrap{overflow-x:auto;overflow-y:hidden;-webkit-overflow-scrolling:touch}
.ruler{width:100%;height:auto;display:block;margin:6px 0 2px}
@media (max-width:640px){.ruler{min-width:540px}}
.ruler text{font-family:var(--mono);font-size:11px;fill:var(--ink-2)}
.ruler .tier-lbl{font-family:var(--sans);font-size:10px;fill:var(--muted)}
.ruler .active-lbl{font-weight:700;fill:var(--ink)}
.ruler .marker{transition:transform .35s ease}
.ruler-legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:12px;color:var(--muted);margin-bottom:6px}
.ruler-legend i{display:inline-block;width:12px;height:10px;border-radius:2px;vertical-align:-1px;margin-right:4px}
.sec-title{font-size:14.5px;font-weight:700;color:var(--brand-ink);border-bottom:2px solid var(--brand-soft);padding-bottom:4px;margin:14px 0 8px;display:flex;align-items:center;gap:8px}
.sec-title .n{font-family:var(--mono);font-size:12px;color:var(--brand);background:var(--brand-soft);padding:1px 6px;border-radius:4px}
.dec{border-radius:8px;padding:10px 12px;font-size:14.5px;line-height:1.55;border:1px solid var(--line);background:#fff}
.dec .headline{font-weight:800;font-size:16px;margin-bottom:4px}
.dec.go{border-color:#BFE3CC;background:#F3FBF6}.dec.go .headline{color:var(--ok)}
.dec.wait{border-color:#EED9A0;background:#FFFBF0}.dec.wait .headline{color:var(--warn)}
.dec.hold{border-color:#C9D8F5;background:#F5F8FE}.dec.hold .headline{color:var(--info)}
.dec.now{border-color:#F3C4C0;background:#FFF6F5}.dec.now .headline{color:var(--no)}
.dec ul{margin:4px 0 0}
.drug-list{margin:6px 0 0;padding-left:0;list-style:none}
.drug-list li{padding:6px 10px;border-left:3px solid var(--line);margin:4px 0;font-size:14px;background:var(--bg);border-radius:0 6px 6px 0}
.drug-list li.hi{border-left-color:var(--r-ext)}
.drug-list li.mod{border-left-color:var(--r-h)}
.drug-list li.lo{border-left-color:var(--r-l)}
.drug-list li.ns{border-left-color:var(--brand)}
.drug-list b{font-weight:700}
.nhi-item{border:1px solid var(--line);border-radius:8px;padding:10px 12px;margin:8px 0;background:#fff}
.nhi-item.t2{border-left:4px solid var(--no)}
.nhi-item .top{display:flex;align-items:flex-start;gap:8px;flex-wrap:wrap}
.nhi-item .nm{font-weight:700;font-size:14.5px;flex:1 1 auto}
.nhi-item .det{font-size:13.5px;color:var(--ink-2);margin-top:4px}
.nhi-item .det ul{margin:2px 0 0;padding-left:1.2em}
.chk-list{list-style:none;padding:0;margin:4px 0 0}
.chk-list li{display:flex;gap:8px;align-items:flex-start;font-size:13.5px;padding:3px 0}
.chk-list .m{flex:none;width:18px;height:18px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:12px;font-weight:800;margin-top:2px}
.chk-list .m.y{background:var(--ok-soft);color:var(--ok)}
.chk-list .m.n{background:var(--no-soft);color:var(--no)}
.chk-list .m.q{background:var(--warn-soft);color:var(--warn)}
.fu-list li{font-size:14px}
.summary-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
.toast{position:fixed;left:50%;bottom:84px;transform:translateX(-50%);background:var(--ink);color:#fff;padding:8px 14px;border-radius:999px;font-size:13px;opacity:0;pointer-events:none;transition:opacity .2s;z-index:50}
.toast.show{opacity:1}

/* ---------- Reference tables ---------- */
.tbl{width:100%;border-collapse:collapse;font-size:13.5px;margin:8px 0}
.tbl th,.tbl td{border:1px solid var(--line);padding:8px 10px;vertical-align:top;text-align:left}
.tbl th{background:var(--brand-tint);color:var(--brand-ink);font-weight:700}
.tbl td.c{text-align:center}
.tbl-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
.stat-grid{display:grid;grid-template-columns:1fr;gap:12px;margin-top:8px}
@media (min-width:760px){.stat-grid{grid-template-columns:repeat(3,minmax(0,1fr))}}
.stat-col{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;background:#fff}
.stat-col .h{padding:10px 12px;color:#fff;font-weight:800;font-size:15px}
.stat-col .h small{display:block;font-weight:500;opacity:.9;font-size:12.5px}
.stat-col.hi .h{background:var(--r-ext)}.stat-col.mod .h{background:var(--r-h)}.stat-col.lo .h{background:var(--r-l)}
.stat-col .b{padding:8px 12px}
.stat-col .b .lbl{font-size:11.5px;color:var(--muted);font-weight:700;letter-spacing:.04em;margin-top:6px}
.stat-col ul{list-style:none;padding:0;margin:2px 0 4px}
.stat-col li{padding:5px 0;border-bottom:1px dashed var(--line-2);font-size:14px}
.stat-col li:last-child{border-bottom:0}
.stat-col li b{font-weight:800}
.stat-col li .rct{font-weight:800;text-decoration:underline dotted;text-underline-offset:3px}
.legend{font-size:12.5px;color:var(--muted);margin-top:8px}
.acc{border:1px solid var(--line);border-radius:8px;margin:8px 0;background:#fff}
.acc summary{cursor:pointer;padding:10px 12px;font-weight:700;color:var(--brand-ink);font-size:14.5px;list-style:none;display:flex;justify-content:space-between;align-items:center}
.acc summary::-webkit-details-marker{display:none}
.acc summary::after{content:"＋";color:var(--muted);font-weight:400}
.acc[open] summary::after{content:"－"}
.acc .body{padding:0 12px 12px;font-size:14px}
.rule-text{white-space:normal;font-size:14px;line-height:1.7}
.rule-text .new{background:#FFF6D6;border-bottom:2px solid #F0C000}
.kv{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;font-size:13.5px}
.kv dt{color:var(--muted);font-weight:600}
.kv dd{margin:0}
.prod-list{font-size:13px;columns:1}
@media (min-width:700px){.prod-list.two{columns:2;column-gap:24px}}
.prod-list div{break-inside:avoid;padding:2px 0;border-bottom:1px dotted var(--line-2)}
.prod-list code{font-size:12px;color:var(--brand-ink)}

/* ---------- Mobile summary bar ---------- */
.mbar{position:fixed;left:0;right:0;bottom:0;background:var(--paper);border-top:1px solid var(--line);box-shadow:0 -4px 16px rgba(16,24,40,.08);padding:8px 12px calc(8px + env(safe-area-inset-bottom));display:flex;align-items:center;gap:10px;z-index:40}
.mbar .mb-risk{font-weight:800;font-size:15px}
.mbar .mb-t{font-family:var(--mono);font-size:13px;color:var(--ink-2)}
.mbar .grow{flex:1;min-width:0;overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
@media (min-width:1024px){.mbar{display:none}}
@media (prefers-reduced-motion:reduce){*{transition:none !important;animation:none !important}}
@media print{
  .hdr .tabs,.mbar,.summary-actions,.actions,.no-print{display:none !important}
  main{padding:0}.card{box-shadow:none;break-inside:avoid}
  .col-result{position:static;max-height:none;overflow:visible}
  body{background:#fff}
}
</style>
</head>
<body>
<header class="hdr">
  <div class="hdr-in">
    <h1>血脂治療決策工具 <span class="muted" style="font-weight:500;font-size:14px">Statin / Non-statin 用藥與健保給付判定</span></h1>
    <div class="sub">依《2025 台灣血脂管理臨床路徑共識》判定 ASCVD 風險分級與 LDL-C 目標，比對 115/9/1 修訂後健保降血脂藥物給付規定（表一）與 PCSK9 給付規定；所選 statin 品項若列於「不適用表一」清單，自動改依表二（原給付規定）判定；statin 強度分類採 2026 ACC/AHA 指引 Table 6。</div>
    <div class="src-badges">
      <span class="badge"><span class="dot"></span><b>共識</b> 2025 台灣血脂管理臨床路徑共識（內科學誌 2024;35:426-430）</span>
      <span class="badge"><span class="dot"></span><b>健保</b> 藥品給付規定 2.6.1–2.6.3 修訂（自 115/9/1 生效）</span>
      <span class="badge"><span class="dot"></span><b>健保</b> 降膽固醇藥物給付規定表二（原表 86/1/1–108/2/1；適用 116 個列表品項）</span>
      <span class="badge"><span class="dot"></span><b>健保</b> PCSK9 血脂調節劑 2.6.4（114/9/1 修訂）</span>
      <span class="badge"><span class="dot"></span><b>Statin 強度</b> 2026 ACC/AHA 多學會血脂異常管理指引 Table 6</span>
    </div>
  </div>
  <nav class="tabs" role="tablist" aria-label="頁面分區">
    <button class="tab" role="tab" aria-selected="true" data-tab="tool">決策工具</button>
    <button class="tab" role="tab" aria-selected="false" data-tab="statin">Statin 強度分類（ACC/AHA 2026）</button>
    <button class="tab" role="tab" aria-selected="false" data-tab="nhi">健保給付規定：表一（115/9/1 修訂）</button>
    <button class="tab" role="tab" aria-selected="false" data-tab="t2">健保表二（原給付規定）</button>
    <button class="tab" role="tab" aria-selected="false" data-tab="pcsk9">PCSK9 給付規定</button>
    <button class="tab" role="tab" aria-selected="false" data-tab="consensus">共識臨床路徑</button>
    <button class="tab" role="tab" aria-selected="false" data-tab="about">使用說明與判定邏輯</button>
  </nav>
</header>

<main>
<!-- ================= TOOL ================= -->
<section class="panel active" id="panel-tool" role="tabpanel">
<div class="notice info no-print" style="margin-top:0">
  <b>生效日提醒：</b>降血脂藥物給付規定表一／Ezetimibe／複方之修訂自 <b>民國 115 年 9 月 1 日（2026-09-01）</b>生效；2.6.1 所列 116 個 statin／複方品項不適用表一，仍依<b>表二（原給付規定）</b>——於步驟 5 選取品項即自動切換判定；PCSK9 規定為 114/9/1 修訂版。本工具為臨床決策輔助，最終處方與給付判定仍以醫師專業判斷及健保署最新公告為準。
</div>
<div class="grid">
<div class="col-form">

  <!-- Step 1 -->
  <div class="card" id="step1">
    <h2><span class="step-no">1</span>基本資料與血脂值</h2>
    <div class="hint">LDL-C 為判定必要欄位；TC 與 HDL-C 用於計算 non-HDL-C（次要目標）並自動判定 HDL-C 風險因子。選用不適用表一之品項時，表二另以 <b>TC</b> 作為起始／目標值判定依據（TC 建議一併輸入）。</div>
    <div class="field-row">
      <div class="field"><span class="lbl">性別</span>
        <div class="seg" role="group" aria-label="性別"><button type="button" data-seg="sex" data-val="M" aria-pressed="false">男</button><button type="button" data-seg="sex" data-val="F" aria-pressed="false">女</button></div>
      </div>
      <div class="field"><label for="age">年齡 <span class="u">歲</span></label><div class="inp"><input type="number" id="age" data-num="age" min="0" max="120" inputmode="numeric" placeholder="例 62"></div></div>
    </div>
    <div class="field-row four" style="margin-top:10px">
      <div class="field"><label for="ldl">LDL-C <span class="u">必填</span></label><div class="inp"><input type="number" id="ldl" data-num="ldl" min="0" max="1000" inputmode="decimal" placeholder="mg/dL"><span class="unit">mg/dL</span></div></div>
      <div class="field"><label for="tc">總膽固醇 TC</label><div class="inp"><input type="number" id="tc" data-num="tc" min="0" max="1500" inputmode="decimal" placeholder="mg/dL"><span class="unit">mg/dL</span></div></div>
      <div class="field"><label for="hdl">HDL-C</label><div class="inp"><input type="number" id="hdl" data-num="hdl" min="0" max="300" inputmode="decimal" placeholder="mg/dL"><span class="unit">mg/dL</span></div></div>
      <div class="field"><label for="tg">三酸甘油脂 TG</label><div class="inp"><input type="number" id="tg" data-num="tg" min="0" max="5000" inputmode="decimal" placeholder="mg/dL"><span class="unit">mg/dL</span></div></div>
    </div>
    <div class="inline-note" id="nonhdl-note" style="margin-top:8px"></div>
  </div>

  <!-- Step 2 -->
  <div class="card" id="step2">
    <h2><span class="step-no">2</span>動脈硬化心血管疾病（ASCVD）病史</h2>
    <div class="hint">勾選所有符合項目。次級預防族群（非常高／極高風險）之判定依共識與健保表一「ASCVD 風險等級定義」。勾選子項目會自動勾選其上層項目。</div>
    <div class="grp-title">冠狀動脈</div>
    <div class="chk-group">
      <label class="chk"><input type="checkbox" data-key="cad"><span class="box"></span><span class="txt">冠狀動脈疾病（CAD，經臨床或影像確診；含穩定型冠心病）</span></label>
      <label class="chk"><input type="checkbox" data-key="acs"><span class="box"></span><span class="txt">急性冠心症（ACS）病史<small>不穩定型心絞痛或心肌梗塞</small></span></label>
      <div class="sub">
        <label class="chk"><input type="checkbox" data-key="mi"><span class="box"></span><span class="txt">曾發生心肌梗塞（MI）</span></label>
        <div class="sub" data-show-if="mi">
          <label class="chk"><input type="checkbox" data-key="mi1y"><span class="box"></span><span class="txt">最近一次心肌梗塞在一年內</span></label>
          <label class="chk"><input type="checkbox" data-key="mi2"><span class="box"></span><span class="txt">≧兩次心肌梗塞病史</span></label>
        </div>
      </div>
      <label class="chk"><input type="checkbox" data-key="multivessel"><span class="box"></span><span class="txt">多支冠狀動脈阻塞</span></label>
      <label class="chk"><input type="checkbox" data-key="revasc"><span class="box"></span><span class="txt">曾接受冠狀動脈血管再通術（PCI 心導管介入或 CABG 繞道手術）</span></label>
    </div>
    <div class="grp-title">腦血管</div>
    <div class="chk-group">
      <label class="chk"><input type="checkbox" data-key="stroke"><span class="box"></span><span class="txt">動脈硬化相關之缺血性腦中風</span></label>
      <label class="chk"><input type="checkbox" data-key="tia"><span class="box"></span><span class="txt">短暫性腦缺血發作（TIA）合併動脈硬化相關疾病或病史</span></label>
    </div>
    <div class="grp-title">周邊／頸動脈</div>
    <div class="chk-group">
      <label class="chk"><input type="checkbox" data-key="pad"><span class="box"></span><span class="txt">周邊動脈疾病（PAD）<small>曾接受血管再通術、有肢體缺血相關症狀或截肢</small></span></label>
      <div class="sub" data-show-if="pad">
        <label class="chk"><input type="checkbox" data-key="padRevasc"><span class="box"></span><span class="txt">曾接受周邊動脈血管再通術</span></label>
      </div>
      <label class="chk"><input type="checkbox" data-key="carotid"><span class="box"></span><span class="txt">頸動脈狹窄<small>影像確認 ≧50% 直徑狹窄者亦符合「顯著斑塊負擔」之非常高風險定義</small></span></label>
      <div class="sub" data-show-if="carotid">
        <label class="chk"><input type="checkbox" data-key="carotidSym"><span class="box"></span><span class="txt">有症狀之頸動脈狹窄，且診斷經神經科醫師確立<small>表二「心血管疾病定義」之缺血型腦血管疾病項目（僅影響表二判定）</small></span></label>
      </div>
    </div>
    <div class="grp-title">影像</div>
    <div class="chk-group">
      <label class="chk"><input type="checkbox" data-key="imaging50"><span class="box"></span><span class="txt">影像檢查確認顯著斑塊負擔（≧50% 直徑狹窄率）<small>冠狀動脈血管攝影／冠狀動脈或周邊血管電腦斷層／頸動脈或周邊血管超音波</small></span></label>
    </div>
  </div>

  <!-- Step 3 -->
  <div class="card" id="step3">
    <h2><span class="step-no">3</span>高風險條件（初級預防）</h2>
    <div class="hint">未確診 ASCVD 者，符合任一項即為「高風險」；LDL-C ≧190 mg/dL 由步驟 1 之數值自動判定。</div>
    <div class="chk-group">
      <label class="chk"><input type="checkbox" data-key="dm"><span class="box"></span><span class="txt">糖尿病</span></label>
      <label class="chk"><input type="checkbox" data-key="ckd"><span class="box"></span><span class="txt">慢性腎臟病<small>進入透析治療前之 CKD：UACR ≧30 mg/g 或 eGFR &lt;60 mL/min/1.73m² 至少持續 3 個月</small></span></label>
      <label class="chk"><input type="checkbox" data-key="cac400"><span class="box"></span><span class="txt">冠狀動脈鈣化分數（CAC）≧400</span></label>
      <div class="chk disabled" id="ldl190-row"><span class="box" style="border-style:dashed"></span><span class="txt">LDL-C ≧190 mg/dL（自動判定）<small id="ldl190-note">請於步驟 1 輸入 LDL-C</small></span><span class="rf-status unk" id="ldl190-status">未輸入</span></div>
      <label class="chk"><input type="checkbox" data-key="xanthoma"><span class="box"></span><span class="txt">肌腱黃色瘤<small>用於提示家族性高膽固醇血症（FH）篩檢，不改變風險分級</small></span></label>
    </div>
  </div>

  <!-- Step 4 -->
  <div class="card" id="step4">
    <h2><span class="step-no">4</span>心血管風險因子（中／低風險判定）</h2>
    <div class="hint">未符合 ASCVD 或高風險條件者，以風險因子數量分級：≧2 項＝中風險、1 項＝低風險、0 項＝依健保表一「0 項心血管風險因子」列。年齡與 HDL-C 依步驟 1 數值自動判定。<br>表二（原給付規定）之危險因子定義略有不同：HDL-C &lt;40 mg/dL 不分性別、女性停經者計入年齡、不含代謝性症候群；選用不適用表一之品項時自動改依表二定義計算。</div>
    <div class="chk-group">
      <label class="chk"><input type="checkbox" data-key="htn"><span class="box"></span><span class="txt">高血壓</span></label>
      <div class="chk disabled"><span class="box" style="border-style:dashed"></span><span class="txt">年齡：男性 ≧45 歲、女性 ≧55 歲（自動判定）</span><span class="rf-status unk" id="rf-age-status">未輸入</span></div>
      <div class="sub hide" data-show-sex="F"><label class="chk"><input type="checkbox" data-key="menopause"><span class="box"></span><span class="txt">已停經<small>表二年齡危險因子為「女性 ≧55 歲或停經者」；表一與共識僅計年齡</small></span></label></div>
      <label class="chk"><input type="checkbox" data-key="fhx"><span class="box"></span><span class="txt">早發性冠心病家族史<small>男性 ≦55 歲、女性 ≦65 歲</small></span></label>
      <div class="chk disabled"><span class="box" style="border-style:dashed"></span><span class="txt">HDL-C：男性 &lt;40 mg/dL、女性 &lt;50 mg/dL（自動判定）</span><span class="rf-status unk" id="rf-hdl-status">未輸入</span></div>
      <label class="chk"><input type="checkbox" data-key="smoking"><span class="box"></span><span class="txt">抽菸</span></label>
    </div>
    <div class="grp-title" style="display:flex;align-items:center;gap:8px">代謝性症候群（符合以下至少三項即計為 1 項風險因子）<span class="rf-status" id="ms-status">0／5 項</span></div>
    <div class="chk-group">
      <label class="chk"><input type="checkbox" data-key="ms_waist"><span class="box"></span><span class="txt">腹部肥胖<small>男性腰圍 ≧90 cm、女性 ≧80 cm</small></span></label>
      <label class="chk" id="ms_bp_row"><input type="checkbox" data-key="ms_bp"><span class="box"></span><span class="txt">血壓偏高<small>≧130/85 mmHg 或使用高血壓藥物（勾選高血壓時自動符合）</small></span></label>
      <label class="chk" id="ms_fpg_row"><input type="checkbox" data-key="ms_fpg"><span class="box"></span><span class="txt">空腹血糖偏高<small>≧100 mg/dL 或使用糖尿病藥物（勾選糖尿病時自動符合）</small></span></label>
      <label class="chk" id="ms_tg_row"><input type="checkbox" data-key="ms_tg"><span class="box"></span><span class="txt">空腹 TG 偏高<small>≧150 mg/dL（依步驟 1 自動判定）或使用治療 TG 之血脂藥物（請手動勾選）</small></span></label>
      <div class="chk disabled"><span class="box" style="border-style:dashed"></span><span class="txt">HDL-C 偏低：男性 &lt;40、女性 &lt;50 mg/dL（自動判定）</span><span class="rf-status unk" id="ms-hdl-status">未輸入</span></div>
    </div>
  </div>

  <!-- Step 5 -->
  <div class="card" id="step5">
    <h2><span class="step-no">5</span>目前降血脂治療狀態</h2>
    <div class="hint">用於判定共識路徑之下一步，以及 Ezetimibe（2.6.2）、複方（2.6.3）與 PCSK9（2.6.4）之給付條件。</div>
    <div class="seg block wrap" role="group" aria-label="治療狀態">
      <button type="button" data-seg="status" data-val="naive" aria-pressed="true">尚未使用降血脂藥物</button>
      <button type="button" data-seg="status" data-val="statin" aria-pressed="false">statin 單一治療中</button>
      <button type="button" data-seg="status" data-val="statin_eze" aria-pressed="false">statin＋ezetimibe 併用中</button>
      <button type="button" data-seg="status" data-val="intolerant" aria-pressed="false">statin 不耐受／禁忌症</button>
      <button type="button" data-seg="status" data-val="pcsk9" aria-pressed="false">已使用 PCSK9 抑制劑</button>
    </div>

    <div class="tx-block" id="prodBlock">
      <h4>Statin 品項（擬處方或目前使用）— 判定適用表一或表二</h4>
      <div class="inline-note" style="margin-left:0">輸入品名或健保代碼。列於 2.6.1「不適用表一」清單之 116 個品項 → statin 給付自動改依<b>表二（原給付規定）</b>判定，並帶入成分與劑量；未列者適用表一。亦可查詢 ezetimibe／複方之列表品項（3 個月規定）。</div>
      <div class="inp search-box"><input type="text" id="prodSearch" placeholder="例：Crestor、Livalo、Roty、AC58282100、Ezetimibe Sandoz" autocomplete="off"></div>
      <div class="search-res" id="prodRes"></div>
      <div id="prodSel" class="prod-sel hide"></div>
    </div>

    <div class="tx-block" data-status="naive">
      <h4>尚未用藥</h4>
      <label class="chk"><input type="checkbox" data-key="lifestyleDone"><span class="box"></span><span class="txt">已進行 3–6 個月生活型態改變（非藥物治療）並處置心血管風險因子，複檢血脂仍未達標<small>表一：中／低／0 項風險因子之給藥前提；表二：危險因子各列「給藥前應有 3–6 個月非藥物治療」</small></span></label>
    </div>

    <div class="tx-block hide" data-status="statin statin_eze pcsk9">
      <h4>目前使用之 statin</h4>
      <div class="field-row">
        <div class="field"><label for="statinDrug">Statin 成分</label><div class="inp"><select id="statinDrug" data-sel="statinDrug">
          <option value="">— 選擇 —</option>
          <option value="atorvastatin">Atorvastatin</option>
          <option value="rosuvastatin">Rosuvastatin</option>
          <option value="simvastatin">Simvastatin</option>
          <option value="pravastatin">Pravastatin</option>
          <option value="lovastatin">Lovastatin</option>
          <option value="fluvastatin">Fluvastatin</option>
          <option value="pitavastatin">Pitavastatin</option>
          <option value="other">其他／不確定</option>
        </select></div></div>
        <div class="field"><label for="statinDose">每日劑量</label><div class="inp"><select id="statinDose" data-sel="statinDose"><option value="">— 先選成分 —</option></select></div></div>
      </div>
      <div class="inline-note" id="intensity-note" style="margin:6px 0 4px 0"></div>
      <label class="chk"><input type="checkbox" data-key="statinMax"><span class="box"></span><span class="txt">此劑量已是病人可耐受之最大劑量（最大耐受劑量 statin）</span></label>
      <div class="field" style="margin-top:6px"><label for="statinDur">目前 statin 治療期間（PCSK9 條件需連續 ≧3 個月；ezetimibe 併用門檻為單一治療 6–8 週）</label><div class="inp"><select id="statinDur" data-sel="statinDur">
        <option value="">— 請選擇 —</option>
        <option value="lt6w">未滿 6 週</option>
        <option value="6to8w">6–8 週</option>
        <option value="8wto3m">超過 8 週但未滿 3 個月</option>
        <option value="ge3m">3 個月以上</option>
      </select></div></div>
    </div>

    <div class="tx-block hide" data-status="statin_eze pcsk9">
      <h4>Ezetimibe 10 mg 併用</h4>
      <div class="field"><label for="ezeDur">Ezetimibe 併用期間（PCSK9 條件：statin 治療後再合併 ezetimibe ≧3 個月）</label><div class="inp"><select id="ezeDur" data-sel="ezeDur">
        <option value="lt3m">未滿 3 個月</option>
        <option value="ge3m">3 個月以上</option>
      </select></div></div>
    </div>

    <div class="tx-block hide" data-status="intolerant">
      <h4>Statin 不耐受／禁忌症之類型</h4>
      <label class="chk"><input type="checkbox" data-key="ci"><span class="box"></span><span class="txt">Statin 禁忌症<small>藥物過敏（需說明成分、品名、健保代碼、過敏反應與佐證）或活動性肝病變（需附佐證）</small></span></label>
      <label class="chk"><input type="checkbox" data-key="intolConfirmed"><span class="box"></span><span class="txt">確診 statin 不耐受（依中華民國血脂及動脈硬化學會 2019 共識）<small>確認為嚴重橫紋肌溶解症（一種 statin 即可診斷）；或肌肉／肝臟相關副作用（Myalgia score &gt;8 分）且對「兩種」statin 不耐受，其中一種為最低有效劑量（rosuvastatin 5、atorvastatin 10、pravastatin 10、lovastatin 20、fluvastatin 20、pitavastatin 1、simvastatin 5 mg）</small></span></label>
      <label class="chk"><input type="checkbox" data-key="intolADR"><span class="box"></span><span class="txt">對 statin 發生無法耐受之藥物不良反應（如 severe myalgia、myositis）<small>Ezetimibe 2.6.2 第 1 款之要件</small></span></label>
      <label class="chk"><input type="checkbox" data-key="ezeOn"><span class="box"></span><span class="txt">目前使用 ezetimibe 10 mg（或含 ezetimibe 之其他降血脂藥物）</span></label>
      <div class="sub" data-show-if="ezeOn">
        <div class="field"><label for="ezeDur2">Ezetimibe 持續治療期間</label><div class="inp"><select id="ezeDur2" data-sel="ezeDur2">
          <option value="lt3m">未滿 3 個月</option>
          <option value="ge3m">3 個月以上</option>
        </select></div></div>
      </div>
    </div>

    <div class="tx-block hide" data-status="statin statin_eze intolerant pcsk9">
      <h4>PCSK9 給付相關（2.6.4）</h4>
      <label class="chk"><input type="checkbox" data-key="event1y"><span class="box"></span><span class="txt">符合「發生重大心血管事件後一年內」之要件<small>申請表：首次申請限給付於在發病（心肌梗塞／冠狀動脈或其他動脈血管再通術／動脈硬化相關之缺血性腦中風）後一年內開始使用最大耐受劑量 statin 之病人</small></span></label>
      <label class="chk"><input type="checkbox" data-key="hofh"><span class="box"></span><span class="txt">同合子家族性高膽固醇血症（HoFH）<small>另有 evolocumab HoFH 給付途徑</small></span></label>
      <div class="sub" data-show-if="hofh">
        <label class="chk"><input type="checkbox" data-key="hofh6m"><span class="box"></span><span class="txt">已使用最高忍受劑量之 statin＋ezetimibe 合併治療 6 個月，LDL-C 仍高於 130 mg/dL</span></label>
        <label class="chk"><input type="checkbox" data-key="hofhCriteria"><span class="box"></span><span class="txt">符合 HoFH 診斷要件之一<small>基因檢測為同合子或多重不同基因異常且台灣 FH 診斷標準評分 &gt;8 分；或未檢出者至少符合三項臨床徵狀（10 歲前皮膚／肌腱黃色瘤；未治療 LDL-C &gt;500 且治療後 &gt;330 mg/dL；父母高膽固醇血症 TC &gt;250；20 歲前發生冠心病）</small></span></label>
      </div>
    </div>

    <div class="tx-block hide" data-status="pcsk9">
      <h4>PCSK9 續用評估</h4>
      <div class="field-row">
        <div class="field"><span class="lbl">使用藥物</span>
          <div class="seg" role="group"><button type="button" data-seg="pcsk9Drug" data-val="evolocumab" aria-pressed="false">Evolocumab</button><button type="button" data-seg="pcsk9Drug" data-val="alirocumab" aria-pressed="false">Alirocumab</button></div>
        </div>
        <div class="field"><label for="preLdl">PCSK9 開始使用前 LDL-C</label><div class="inp"><input type="number" id="preLdl" data-num="preLdl" min="0" max="1000" inputmode="decimal" placeholder="mg/dL"><span class="unit">mg/dL</span></div></div>
      </div>
      <div class="inline-note" style="margin-left:0">步驟 1 之 LDL-C 視為目前治療中之最新值；續用門檻：較用藥前下降 ≧30%（HoFH：連續二次未達 ≧18% 即不同意續用）。</div>
    </div>

    <div class="actions"><button type="button" class="btn" id="btnReset">清除全部輸入</button></div>
  </div>
</div>

<div class="col-result" id="resultCol">
  <div id="result"></div>
</div>
</div>
</section>

<!-- ================= STATIN INTENSITY ================= -->
<section class="panel" id="panel-statin" role="tabpanel">
<div class="card">
  <h2>Statin 強度分類與藥物（學名／每日劑量）</h2>
  <p class="muted" style="font-size:13px;margin:4px 0 6px">來源：2026 ACC/AHA/AACVPR/ABC/ACPM/ADA/AGS/APhA/ASPC/NLA/PCNA Guideline on the Management of Dyslipidemia（JACC 2026;87:2624-2757）Table 6「High-, Moderate-, and Low-Intensity Statin Therapy」。高強度預期降低 LDL-C ≧50%、中強度 30–49%、低強度 &lt;30%。</p>
  <div class="stat-grid">
    <div class="stat-col hi"><div class="h">高強度 High-Intensity<small>預期 LDL-C 降幅 ≧50%</small></div><div class="b">
      <div class="lbl">PREFERRED STATINS（首選）</div>
      <ul><li><span class="rct">Atorvastatin</span> (40 mg) <span class="rct">80 mg</span></li><li><span class="rct">Rosuvastatin 20 mg</span> (40 mg)</li></ul>
      <div class="lbl">OTHER STATINS</div><ul><li class="muted">—</li></ul>
    </div></div>
    <div class="stat-col mod"><div class="h">中強度 Moderate-Intensity<small>預期 LDL-C 降幅 30–49%</small></div><div class="b">
      <div class="lbl">PREFERRED STATINS（首選）</div>
      <ul><li><span class="rct">Atorvastatin 10 mg</span> (20 mg)</li><li><span class="rct">Rosuvastatin</span> (5 mg) <span class="rct">10 mg</span></li></ul>
      <div class="lbl">OTHER STATINS</div>
      <ul><li>Fluvastatin XL 80 mg</li><li><span class="rct">Fluvastatin 40 mg BID</span></li><li><span class="rct">Lovastatin 40 mg</span> (80 mg)</li><li><span class="rct">Pitavastatin</span> 1, 2, <span class="rct">4 mg</span></li><li><span class="rct">Pravastatin 40 mg</span> (80 mg)</li><li><span class="rct">Simvastatin 20, 40 mg</span>‡</li></ul>
    </div></div>
    <div class="stat-col lo"><div class="h">低強度 Low-Intensity<small>預期 LDL-C 降幅 &lt;30%</small></div><div class="b">
      <div class="lbl">PREFERRED STATINS</div><ul><li class="muted">—</li></ul>
      <div class="lbl">OTHER STATINS</div>
      <ul><li>Fluvastatin 20, 40 mg</li><li><span class="rct">Lovastatin 20 mg</span></li><li>Pravastatin 10, 20 mg</li><li>Simvastatin 10 mg</li></ul>
    </div></div>
  </div>
  <div class="legend">
    <b>粗體（虛線底線）</b>＝於評估 ASCVD 事件降低之安慰劑對照 RCT 及 CTT 2010 統合分析中被評估過之特定 statin 與劑量（表中 Boldface）；括號內劑量為同強度之其他劑量。<br>
    ‡ Simvastatin 80 mg 雖曾於 RCT 評估，但因肌病變（含橫紋肌溶解症）風險增加，FDA 不建議起始或調升至 80 mg。<br>
    * 預期降幅為大型族群之估計值：atorvastatin、rosuvastatin、simvastatin 依 VOYAGER 資料庫中位數降幅估計；fluvastatin、lovastatin、pitavastatin、pravastatin 依 FDA 核准仿單。個別病人反應變異度大。BID＝每日兩次；XL＝緩釋劑型。
  </div>
</div>
<div class="card">
  <h2>依學名快速查詢：劑量 → 強度</h2>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>學名</th><th>低強度（&lt;30%）</th><th>中強度（30–49%）</th><th>高強度（≧50%）</th></tr></thead>
    <tbody>
      <tr><td>Atorvastatin</td><td class="c muted">—</td><td><b>10 mg</b>、20 mg</td><td>40 mg、<b>80 mg</b></td></tr>
      <tr><td>Rosuvastatin</td><td class="c muted">—</td><td>5 mg、<b>10 mg</b></td><td><b>20 mg</b>、40 mg</td></tr>
      <tr><td>Simvastatin</td><td>10 mg</td><td><b>20 mg、40 mg</b></td><td class="c muted">—（80 mg 不建議）</td></tr>
      <tr><td>Pravastatin</td><td>10 mg、20 mg</td><td><b>40 mg</b>、80 mg</td><td class="c muted">—</td></tr>
      <tr><td>Lovastatin</td><td><b>20 mg</b></td><td><b>40 mg</b>、80 mg</td><td class="c muted">—</td></tr>
      <tr><td>Fluvastatin</td><td>20 mg、40 mg</td><td>XL 80 mg、<b>40 mg BID</b></td><td class="c muted">—</td></tr>
      <tr><td>Pitavastatin</td><td class="c muted">—</td><td>1 mg、2 mg、<b>4 mg</b></td><td class="c muted">—</td></tr>
    </tbody>
  </table></div>
  <div class="legend">粗體＝Table 6 中以粗體標示（RCT 評估過）之劑量。健保 PCSK9 規定所稱之「高強度 statin」舉例為 rosuvastatin 20 mg 或 atorvastatin 40 mg（含）以上，與本表一致。</div>
</div>
<div class="card">
  <h2>Non-statin 藥物之預期 LDL-C 降幅（同指引 4.2.1.2 節）</h2>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>藥物</th><th>預期 LDL-C 降幅</th><th>備註（指引原文摘要）</th></tr></thead>
    <tbody>
      <tr><td>Ezetimibe 10 mg</td><td>平均 18%（加於 statin 上額外約 25%）</td><td>副作用發生率低</td></tr>
      <tr><td>PCSK9 單株抗體（evolocumab、alirocumab）</td><td>45–64%</td><td>加於 statin 可降低極高風險病人之 ASCVD 事件</td></tr>
      <tr><td>Inclisiran（siRNA PCSK9 抑制劑）</td><td>48–52%</td><td>耐受性佳，多項心血管結果試驗進行中</td></tr>
      <tr><td>Bempedoic acid（ATP citrate lyase 抑制劑）</td><td>單用 21–24%；加於最大耐受 statin 額外 17–18%</td><td>用於 statin 相關副作用者；與足量高強度 statin 併用之研究不足</td></tr>
    </tbody>
  </table></div>
  <div class="legend">指引並指出：non-statin 與低／中強度 statin 併用可達 ≧50% 之 LDL-C 降幅。本頁僅摘錄與 LDL-C 降幅估計相關之敘述，供選擇藥物類別參考；台灣健保對 inclisiran 與 bempedoic acid 之給付條件不在本工具所收錄之文件範圍。</div>
</div>
</section>

<!-- ================= NHI RULES ================= -->
<section class="panel" id="panel-nhi" role="tabpanel">
<div class="card">
  <h2>健保「藥品給付規定」第 2 節心臟血管及腎臟藥物 2.6.1–2.6.3 修訂（自 115/9/1 生效）</h2>
  <div class="notice warn"><b>修訂重點</b>
    <ol style="margin:4px 0 0">
      <li>2.6.1 降血脂藥物給付規定表新增<b>表一</b>（依 ASCVD 風險等級訂定起始藥物治療血脂值、主要／次要血脂目標值與處方規定）；原給付規定表改稱<b>表二</b>，僅適用於所列之特定品項（116 項 statin／複方，見下方清單）。表二全文見「健保表二（原給付規定）」頁籤；決策工具於選取列表品項時自動改依表二判定。</li>
      <li>2.6.2 Ezetimibe：與 statin 併用之門檻由「statin 單一治療 3 個月未達目標」縮短為「<b>6–8 週</b>未達目標」；惟所列 4 個品項仍須 3 個月。刪除「符合全民健康保險降血脂藥物給付規定表」之前置文字。</li>
      <li>2.6.3 含 ezetimibe 及 statin 之複方：門檻同樣改為 statin 單一治療 <b>6–8 週</b>未達目標（所列 10 個品項仍須 3 個月）；不得與 gemfibrozil 併用之規定維持。</li>
    </ol>
  </div>
  <h3 style="font-size:15px;color:var(--brand-ink);margin-top:14px">全民健康保險降膽固醇藥物給付規定表一（115/9/1）</h3>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>ASCVD 風險等級</th><th>非藥物治療</th><th>起始藥物治療血脂值</th><th>主要／（次要）血脂目標值</th></tr></thead>
    <tbody>
      <tr><td><b style="color:var(--r-ext)">極高風險</b></td><td rowspan="2">處置各項可改善心血管風險因子與藥物治療並行</td><td>LDL-C ≧55 mg/dL</td><td>LDL-C &lt;55 mg/dL（non-HDL-C &lt;85 mg/dL）</td></tr>
      <tr><td><b style="color:var(--r-vh)">非常高風險</b></td><td>LDL-C ≧70 mg/dL</td><td>LDL-C &lt;70 mg/dL（non-HDL-C &lt;100 mg/dL）</td></tr>
      <tr><td><b style="color:var(--r-h)">高風險</b></td><td>生活型態改變與藥物治療並行</td><td>LDL-C ≧100 mg/dL</td><td>LDL-C &lt;100 mg/dL（non-HDL-C &lt;130 mg/dL）</td></tr>
      <tr><td><b style="color:var(--r-m)">中風險</b></td><td rowspan="3">給藥前應有 3–6 個月生活型態改變，並處置心血管風險因子</td><td>LDL-C ≧115 mg/dL</td><td>LDL-C &lt;115 mg/dL（non-HDL-C &lt;145 mg/dL）</td></tr>
      <tr><td><b style="color:var(--r-l)">低風險</b></td><td>LDL-C ≧130 mg/dL</td><td>LDL-C &lt;130 mg/dL（non-HDL-C &lt;160 mg/dL）</td></tr>
      <tr><td><b style="color:var(--r-z)">0 項心血管風險因子</b></td><td>LDL-C ≧160 mg/dL</td><td>LDL-C &lt;160 mg/dL</td></tr>
    </tbody>
  </table></div>
  <details class="acc" open><summary>處方規定：極高、非常高風險</summary><div class="body rule-text">
    一、起始治療：依據基線血脂值、用藥史和臨床狀況，給予中至高強度 statin 或合併 ezetimibe。<br>
    二、經起始治療 6~8 週後，檢測血脂指標，如治療達標，則維持治療，並應每 6 個月追蹤血脂指標；如血脂值未達標，檢視服藥狀況，並考慮調整至高強度 statin 或最大耐受 statin 劑量，同時考慮合併 non-statin 治療，包含：ezetimibe、PCSK9 單株抗體、siRNA、ATP citrate lyase 抑制劑。<br>
    三、更動治療 1~3 個月內需追蹤血脂值是否達標，如治療達標，則維持治療，並應每 6 個月追蹤血脂指標；如血脂值未達標，檢視服藥狀況，並考慮調整藥物組合。
  </div></details>
  <details class="acc" open><summary>處方規定：高風險</summary><div class="body rule-text">
    一、起始治療：依據基線血脂值與臨床狀況，給予中至高強度 statin 或合併 ezetimibe；同時進行生活型態改變。<br>
    二、經起始治療 6~8 週後，檢測血脂指標，如治療達標，則維持治療，並應每 6 個月追蹤血脂指標；如血脂值未達標，檢視服藥狀況，並考慮使用高強度 statin 或最大耐受 statin 劑量或同時合併 non-statin 治療，包含：ezetimibe、PCSK9 單株抗體、siRNA、ATP citrate lyase 抑制劑。<br>
    三、更動治療 1~3 個月內需追蹤血脂值是否達標，如治療達標，則維持治療，並應每 6 個月追蹤血脂指標；如血脂值未達標，檢視服藥狀況，並考慮調整藥物組合。
  </div></details>
  <details class="acc" open><summary>處方規定：中、低風險</summary><div class="body rule-text">
    一、起始治療：進行生活型態改變，並處置心血管風險因子。<br>
    二、經起始治療 3~6 個月後，檢測血脂指標，如治療達標，則維持治療，並應每 6-12 個月追蹤血脂指標；如血脂值未達標，給予中強度 statin。<br>
    三、中強度 statin 治療 6~8 週後追蹤血脂值是否達標，如治療達標，則維持治療，並應每 6-12 個月追蹤血脂指標；如血脂值未達標，檢視服藥狀況，並可給予高強度 statin 或最大耐受 statin 劑量或合併 non-statin 治療。
  </div></details>
  <details class="acc"><summary>ASCVD 風險等級定義（表一）</summary><div class="body rule-text">
    <b>一、極高風險：</b>(一) 冠狀動脈疾病合併下列任一臨床狀況：1. 一年內曾經歷心肌梗塞。2. ≧兩次心肌梗塞病史。3. 多支冠狀動脈阻塞。4. 急性冠心症合併糖尿病。5. 周邊動脈疾病或頸動脈狹窄。(二) 周邊動脈疾病合併下列任一臨床狀況：1. 冠狀動脈疾病。2. 頸動脈狹窄。<br>
    <b>二、非常高風險：</b>(一) 經臨床檢查確診為動脈硬化心血管疾病，包含：1. 急性冠心症病史。2. 接受血管再通術（心導管介入治療或外科冠狀動脈繞道手術）。3. 缺血性中風／短暫性腦缺血發作合併動脈硬化相關疾病或病史。4. 周邊動脈疾病（曾接受血管再通術、有肢體缺血相關症狀或截肢）。(二) 經影像檢查確認有顯著斑塊負擔，定義為 ≧50% 直徑狹窄率，包含：1. 冠狀動脈血管攝影。2. 冠狀動脈或周邊血管電腦斷層攝影。3. 頸動脈或周邊血管超音波。<br>
    <b>三、高風險：</b>(一) 糖尿病。(二) 慢性腎臟病（進入透析治療前的慢性腎臟病，包括 UACR ≧30 mg/g or eGFR &lt;60 mL/min/1.73m² 至少持續 3 個月）。(三) LDL-C ≧190 mg/dL。(四) 冠狀動脈鈣化分數（CAC）≧400。<br>
    <b>四、中風險：</b>2 項（含）以上心血管風險因子。<b>五、低風險：</b>1 項心血管風險因子。<br>
    <b>心血管風險因子定義：</b>一、高血壓。二、男性 ≧45 歲，女性 ≧55 歲。三、早發性冠心病家族史（男性 ≦55 歲，女性 ≦65 歲）。四、HDL-C：男性 &lt;40 mg/dL，女性 &lt;50 mg/dL。五、抽菸。六、代謝性症候群（符合以下至少三項）：(一) 腹部肥胖（男性 ≧90 cm，女性 ≧80 cm）。(二) 血壓偏高（≧130/85 mmHg 或使用高血壓藥物）。(三) 空腹血糖偏高（≧100 mg/dL 或使用糖尿病藥物）。(四) 空腹 TG 偏高（≧150 mg/dL 或使用治療 TG 血脂藥物）。(五) HDL-C 偏低（男性 &lt;40 mg/dL，女性 &lt;50 mg/dL）。
  </div></details>
  <details class="acc"><summary>各風險等級評估建議 與 non-HDL-C 次要標的（表一）</summary><div class="body rule-text">
    <b>一、極高風險、非常高風險：</b>(一) 初始評估應檢測完整血脂指標，並應於急性病人入院後 24 小時內完成血脂檢驗。(二) 處置各項可改善心血管風險因子，包含：血壓、HbA1c、肥胖、抽菸、酒精攝取、生活型態。<br>
    <b>二、高風險、中風險、低風險：</b>(一) 給予完整血脂指標檢測，辨識各項可改善心血管風險因子，包含：血壓、HbA1c、肥胖、抽菸、酒精攝取、生活型態。(二) ASCVD 風險分級為高風險，當有嚴重高膽固醇血症、肌腱黃色瘤、早發心血管疾病或家族病史時，應依照台灣家族性高膽固醇血症診斷標準進行家族性膽固醇血症篩檢。(三) 若未符合上述高風險條件，應以列在低至中風險欄位的心血管風險因子數量作為風險評估。<br>
    ● 當 LDL-C 達到理想治療目標後，非高密度脂蛋白-膽固醇（non-HDL-C）可作為血脂治療次要標的，其計算方式為總膽固醇數值減掉 HDL-C 數值，尤其適用於合併有高三酸甘油脂、糖尿病、或肥胖的病人以做進一步的心血管風險評估。
  </div></details>
</div>

<div class="card">
  <h2>2.6.2 Ezetimibe（94/6/1、115/9/1）</h2>
  <div class="rule-text">
    限用於原發性高膽固醇血症、同型接合子家族性高膽固醇血症、同型接合子性麥脂醇血症（植物脂醇血症）患者，並符合下列條件之一者：<br>
    1. 對 statins 類藥品發生無法耐受藥物不良反應（如 Severe myalgia、Myositis）者。（94/6/1、115/9/1）<br>
    2. 經使用 statins 類藥品單一治療 <span class="new">6-8 週</span>未達治療目標者，得合併使用本類藥品與 statins 類藥品。<span class="new">但下表所列項目，需經使用 statins 類藥品單一治療 3 個月未達治療目標者，始得與 statins 類藥品併用。</span>（115/9/1）
  </div>
  <div class="prod-list" style="margin-top:6px" id="ezeList"></div>
  <details class="acc" style="margin-top:8px"><summary>原給付規定（修訂前）對照</summary><div class="body rule-text">2.6.2 Ezetimibe（如 Ezetrol Tablets）：（94/6/1）原發性高膽固醇血症、同型接合子家族性高膽固醇血症、同型接合子性麥脂醇血症（植物脂醇血症）患者並符合下列條件之一者：1. 符合全民健康保險降血脂藥物給付規定表且對 Statins 類藥品發生無法耐受藥物不良反應（如 Severe myalgia、Myositis）者。2. 符合全民健康保險降血脂藥物給付規定表經使用 Statins 類藥品單一治療 3 個月未達治療目標者，得合併使用本案藥品與 Statins 類藥品。</div></details>
</div>

<div class="card">
  <h2>2.6.3 含 ezetimibe 及 statin 類之複方製劑（95/12/1、106/8/1、111/11/1、112/12/1、115/9/1）</h2>
  <div class="rule-text">
    1. 限用於原發性高膽固醇血症、同型接合子家族性高膽固醇血症（HOFH）病患。（106/8/1、115/9/1）<br>
    2. 經使用 statin 類藥品單一治療 <span class="new">6-8 週</span>未達治療目標者，得使用本類藥品。<span class="new">但下表所列項目，需經使用 statin 類藥品單一治療 3 個月未達治療目標者，始得使用。</span>（115/9/1）<br>
    3. 本品不得與 gemfibrozil 併用。（106/8/1）
  </div>
  <div class="prod-list two" style="margin-top:6px" id="fdcList"></div>
  <details class="acc" style="margin-top:8px"><summary>原給付規定（修訂前）對照</summary><div class="body rule-text">2.6.3 含 ezetimibe 及 statin 類之複方製劑（如 Vytorin、Atozet、Cretrol、Tonvasca）：1. 限用於原發性高膽固醇血症、同型接合子家族性高膽固醇血症（HOFH）病患並符合全民健康保險降血脂藥物給付規定表，經使用 statin 類藥品單一治療 3 個月未達治療目標者。（106/8/1）2. 本品不得與 gemfibrozil 併用。（106/8/1）</div></details>
</div>

<div class="card">
  <h2>不適用表一、僅適用表二之品項（2.6.1 所列，共 <span id="t2count"></span> 項）</h2>
  <p class="muted" style="font-size:13px">「降膽固醇藥物，適用全民健康保險降膽固醇藥物給付規定表一。但下表所列項目不適用表一，僅適用全民健康保險降膽固醇藥物給付規定表二。(115/9/1)」表二＝原給付規定表（86/1/1、87/4/1、87/7/1、91/9/1、93/9/1、97/7/1、102/8/1、108/2/1、115/9/1），全文見 <a href="#" data-goto="t2">健保表二（原給付規定）</a> 頁籤。於決策工具步驟 5 選取下列品項，statin 給付即自動改依表二判定。</p>
  <div class="inp search-box" style="max-width:420px"><input type="text" id="t2Search" placeholder="篩選：品名、成分或健保代碼"></div>
  <div id="t2List" style="margin-top:8px"></div>
</div>
</section>

<!-- ================= TABLE 2 (ORIGINAL RULES) ================= -->
<section class="panel" id="panel-t2" role="tabpanel">
<div class="card">
  <h2>2.6.1 全民健康保險降血脂藥物給付規定表（86/1/1、87/4/1、87/7/1、91/9/1、93/9/1、97/7/1、102/8/1、108/2/1）— 表二（原給付規定）</h2>
  <div class="notice warn"><b>適用範圍：</b>115/9/1 修訂後，降膽固醇藥物適用表一；但 2.6.1 所列 116 個品項（見「健保給付規定：表一」頁之清單，或於決策工具步驟 5 查詢）<b>不適用表一，僅適用表二</b>。本頁為原給付規定表全文；決策工具於選取列表品項時自動改依本表判定 statin 給付。</div>
  <h3 style="font-size:15px;color:var(--brand-ink);margin-top:14px">全民健康保險降膽固醇藥物給付規定表（表二）</h3>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>對象</th><th>非藥物治療</th><th>起始藥物治療血脂值</th><th>血脂目標值</th><th>處方規定</th></tr></thead>
    <tbody>
      <tr><td>1. 有急性冠狀動脈症候群病史<br>2. 曾接受心導管介入治療或外科冠動脈搭橋手術之冠狀動脈粥狀硬化患者（108/2/1）</td><td>與藥物治療可並行</td><td>LDL-C ≧70 mg/dL</td><td>LDL-C &lt;70 mg/dL</td><td rowspan="5">第一年應每 3-6 個月抽血檢查一次，第二年以後應至少每 6-12 個月抽血檢查一次，同時請注意副作用之產生如肝功能異常，橫紋肌溶解症。</td></tr>
      <tr><td>心血管疾病或糖尿病患者</td><td>與藥物治療可並行</td><td>TC ≧160 mg/dL 或 LDL-C ≧100 mg/dL</td><td>TC &lt;160 mg/dL 或 LDL-C &lt;100 mg/dL</td></tr>
      <tr><td>2 個危險因子或以上</td><td>給藥前應有 3-6 個月非藥物治療</td><td>TC ≧200 mg/dL 或 LDL-C ≧130 mg/dL</td><td>TC &lt;200 mg/dL 或 LDL-C &lt;130 mg/dL</td></tr>
      <tr><td>1 個危險因子</td><td>給藥前應有 3-6 個月非藥物治療</td><td>TC ≧240 mg/dL 或 LDL-C ≧160 mg/dL</td><td>TC &lt;240 mg/dL 或 LDL-C &lt;160 mg/dL</td></tr>
      <tr><td>0 個危險因子</td><td>給藥前應有 3-6 個月非藥物治療</td><td>LDL-C ≧190 mg/dL</td><td>LDL-C &lt;190 mg/dL</td></tr>
    </tbody>
  </table></div>
  <details class="acc" open><summary>心血管疾病定義（表二）</summary><div class="body rule-text">
    (一) 冠狀動脈粥狀硬化患者包含：心絞痛病人，有心導管證實或缺氧性心電圖變化或負荷性試驗陽性反應者（附檢查報告）<br>
    (二) 缺血型腦血管疾病病人包含：1. 腦梗塞。2. 暫時性腦缺血患者（TIA）。（診斷須由神經科醫師確立）3. 有症狀之頸動脈狹窄。（診斷須由神經科醫師確立）
  </div></details>
  <details class="acc" open><summary>危險因子定義（表二）</summary><div class="body rule-text">
    1. 高血壓<br>2. 男性 ≧45 歲，女性 ≧55 歲或停經者<br>3. 有早發性冠心病家族史（男性 ≦55 歲，女性 ≦65 歲）<br>4. HDL-C &lt;40 mg/dL<br>5. 吸菸（因吸菸而符合起步治療準則之個案，若未戒菸而要求藥物治療，應以自費治療）。
  </div></details>
</div>

<div class="card">
  <h2>全民健康保險降三酸甘油酯藥物給付規定表（同文件）</h2>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>對象</th><th>非藥物治療</th><th>起始藥物治療三酸甘油酯值</th><th>三酸甘油酯目標值</th><th>處方規定</th></tr></thead>
    <tbody>
      <tr><td>心血管疾病或糖尿病病人</td><td>與藥物治療可並行</td><td>TG ≧200 mg/dL 且（TC/HDL-C &gt;5 或 HDL-C &lt;40 mg/dL）</td><td>TG &lt;200 mg/dL</td><td rowspan="3">第一年應每 3-6 個月抽血檢查一次，第二年以後應至少每 6-12 個月抽血檢查一次，同時請注意副作用之產生如肝功能異常，橫紋肌溶解症。</td></tr>
      <tr><td>無心血管疾病病人</td><td>給藥前應有 3-6 個月非藥物治療</td><td>TG ≧200 mg/dL 且（TC/HDL-C &gt;5 或 HDL-C &lt;40 mg/dL）</td><td>TG &lt;200 mg/dL</td></tr>
      <tr><td>無心血管疾病病人</td><td>與藥物治療可並行</td><td>TG ≧500 mg/dL</td><td>TG &lt;500 mg/dL</td></tr>
    </tbody>
  </table></div>
  <div class="legend">本工具之判定對象為降膽固醇藥物（statin 等）；此表僅於選用含 fenofibrate 之列表品項（Pravafen）時於結果中附帶參考判定，其餘降三酸甘油酯藥物之給付不在本工具範圍。</div>
</div>

<div class="card">
  <h2>表一（115/9/1 新制）與表二（原給付規定）差異對照</h2>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th style="width:16%">項目</th><th>表一（新制）</th><th>表二（原規定）</th></tr></thead>
    <tbody>
      <tr><td>適用品項</td><td>未列於 2.6.1 排除清單之降膽固醇藥物</td><td>2.6.1 所列 116 個品項（statin 單方、pravastatin＋fenofibrate 複方、atorvastatin＋amlodipine 複方）</td></tr>
      <tr><td>對象分級</td><td>ASCVD 風險等級：極高／非常高／高／中／低／0 項心血管風險因子（定義同 2025 共識）</td><td>① 急性冠狀動脈症候群病史或曾接受心導管介入／外科冠動脈搭橋手術之冠狀動脈粥狀硬化患者；② 心血管疾病或糖尿病；③ 2 個危險因子或以上；④ 1 個；⑤ 0 個</td></tr>
      <tr><td>起始藥物治療血脂值</td><td>LDL-C ≧55／≧70／≧100／≧115／≧130／≧160 mg/dL</td><td>LDL-C ≧70；TC ≧160 或 LDL-C ≧100；TC ≧200 或 LDL-C ≧130；TC ≧240 或 LDL-C ≧160；LDL-C ≧190 mg/dL</td></tr>
      <tr><td>血脂目標值</td><td>LDL-C &lt;55／&lt;70／&lt;100／&lt;115／&lt;130／&lt;160（次要 non-HDL-C &lt;85／&lt;100／&lt;130／&lt;145／&lt;160）</td><td>LDL-C &lt;70；TC &lt;160 或 LDL-C &lt;100；TC &lt;200 或 LDL-C &lt;130；TC &lt;240 或 LDL-C &lt;160；LDL-C &lt;190（無 non-HDL-C 目標）</td></tr>
      <tr><td>非藥物治療</td><td>極高／非常高：處置心血管風險因子與藥物治療並行；高：生活型態改變與藥物治療並行；中／低／0 項：給藥前應有 3–6 個月生活型態改變並處置心血管風險因子</td><td>ACS／PCI-CABG、心血管疾病或糖尿病：與藥物治療可並行；危險因子各列：給藥前應有 3–6 個月非藥物治療</td></tr>
      <tr><td>心血管疾病定義</td><td>依 ASCVD 風險等級定義（含 PAD、頸動脈狹窄、影像確認 ≧50% 狹窄之顯著斑塊負擔等）</td><td>冠狀動脈粥狀硬化（心絞痛病人，有心導管證實或缺氧性心電圖變化或負荷性試驗陽性，附檢查報告）；缺血型腦血管疾病（腦梗塞、TIA、有症狀之頸動脈狹窄；診斷須由神經科醫師確立）。<b>未列 PAD</b></td></tr>
      <tr><td>危險因子定義</td><td>高血壓；男 ≧45／女 ≧55 歲；早發性冠心病家族史（男 ≦55／女 ≦65）；HDL-C 男 &lt;40／女 &lt;50 mg/dL；抽菸；代謝性症候群（五項符合至少三項）</td><td>高血壓；男 ≧45 歲、女 ≧55 歲<b>或停經者</b>；早發性冠心病家族史（男 ≦55／女 ≦65）；HDL-C &lt;40 mg/dL（<b>不分性別</b>）；吸菸（<b>因吸菸而符合者未戒菸應自費</b>）。<b>不含代謝性症候群</b></td></tr>
      <tr><td>處方規定／追蹤</td><td>起始（或中強度 statin）治療 6–8 週後檢測；達標維持並每 6（中／低：6–12）個月追蹤；未達標檢視服藥狀況、調整至高強度／最大耐受 statin 或合併 non-statin；更動治療 1–3 個月內追蹤</td><td>第一年應每 3–6 個月抽血檢查一次，第二年以後應至少每 6–12 個月抽血檢查一次；注意肝功能異常、橫紋肌溶解症</td></tr>
      <tr><td>藥物強度規範</td><td>極高／非常高／高：中至高強度 statin 或合併 ezetimibe；中／低：中強度 statin 起始</td><td>無強度規範</td></tr>
    </tbody>
  </table></div>
</div>

<div class="card">
  <h2>本工具之表二判定邏輯（輸入欄位對應）</h2>
  <ul style="font-size:14px">
    <li><b>啟用時機</b>：步驟 5 選取之 statin 品項列於 2.6.1「不適用表一」清單時，「健保給付判定」中之 Statin 項目改依表二；未選品項或品項未列於清單者依表一。Ezetimibe（2.6.2）、複方（2.6.3）與 PCSK9（2.6.4）之判定不受表一／表二影響。</li>
    <li><b>對象分類（依序）</b>：① 勾選 ACS／MI 或冠狀動脈再通術 → 「急性冠狀動脈症候群病史／PCI-CABG」列（LDL-C ≧70）；② 勾選 CAD／多支阻塞（冠狀動脈粥狀硬化）、缺血性腦中風（腦梗塞）、TIA、有症狀之頸動脈狹窄，或糖尿病 → 「心血管疾病或糖尿病」列；③ 其餘依表二危險因子個數（高血壓、年齡［男 ≧45；女 ≧55 或已停經］、早發性冠心病家族史、HDL-C &lt;40、吸菸）分為 2 個以上／1 個／0 個。</li>
    <li><b>不計入表二心血管疾病者</b>：周邊動脈疾病、單純影像斑塊負擔（≧50% 狹窄）、無症狀頸動脈狹窄——工具會於結果註明。冠狀動脈粥狀硬化須附心導管／缺氧性心電圖／負荷性試驗檢查報告；TIA 與有症狀頸動脈狹窄之診斷須由神經科醫師確立。</li>
    <li><b>起始值與目標值</b>：TC 與 LDL-C 以「或」並列之列，符合其一即計；未輸入 TC 時僅以 LDL-C 判定並註明。危險因子各列於未勾選「已進行 3–6 個月非藥物治療」時判為「有條件」。</li>
    <li><b>吸菸註記</b>：危險因子列之個案若「因吸菸而符合起步治療準則」（不計吸菸即不符合），依表二規定若未戒菸而要求藥物治療應以自費治療，工具會加註提示。</li>
    <li><b>治療中病人</b>：表二未訂調整處方之細則，工具顯示是否達表二目標值與處方規定（追蹤頻率）；臨床調整仍依共識路徑。</li>
    <li><b>對照資訊</b>：改依表二判定時，另列出「若改用適用表一之品項」的表一判定結果，供選藥參考。</li>
  </ul>
</div>
</section>

<!-- ================= PCSK9 ================= -->
<section class="panel" id="panel-pcsk9" role="tabpanel">
<div class="card">
  <h2>2.6.4 PCSK9 血脂調節劑</h2>
  <h3 style="font-size:15px;color:var(--brand-ink);margin-top:8px">2.6.4.1 Evolocumab（如 Repatha）：（107/3/1、108/5/1、109/4/1、114/9/1）</h3>
  <div class="rule-text">
    <b>1. 使用於發生重大心血管事件之病人</b><br>
    (1) 須經事前審查核准後使用（請詳附表二-D），每次申請得核准使用 12 個月，再次申請須檢附評估報告，若血中 LDL-C 較本藥物開始使用前下降程度未達 30%，即屬療效不佳，則不再給付。（114/9/1）<br>
    (2) 限給付於發生重大心血管事件之後一年內且使用最大耐受劑量 statin 之病人，如心肌梗塞、接受冠狀動脈或其他動脈血管再通術（revascularization）、動脈硬化相關之缺血性腦中風等之動脈粥狀硬化心血管疾病之成人病人，且符合下列條件之一者：（114/9/1）<br>
    　I. 經使用高強度 statin（如 rosuvastatin 20mg 或 atorvastatin 40 mg（含）以上）或病人可耐受之最大劑量的 statin 三個月（含）以上且之後再合併使用 ezetimibe 10 mg 三個月（含）以上，LDL-C 仍高於 100 mg/dL 者。<br>
    　II. 對 statin 有禁忌症或確診為對 statin 不耐受之病人，經其他降血脂藥物（至少需有 ezetimibe 10 mg）持續治療 3 個月，LDL-C 仍高於 100 mg/dL 者。<br>
    (3) 最高劑量為每兩週使用 1 支。 (4) 不可同時使用其他 PCSK9 血脂調節劑。<br>
    <b>2. 使用於同合子家族性高膽固醇血症之病人</b><br>
    (1) 限經使用最高忍受劑量之 statin+ezetimibe 合併治療 6 個月，LDL-C 仍高於 130mg/dL 者，且符合下列各項條件之一患者使用：<br>
    　I. 經遺傳基因檢測為同合子基因變異或多重不同基因異常，其作用似同合子基因變異，且確診為同合子家族性高膽固醇血症之患者：依中華民國血脂及動脈硬化學會「臺灣血脂異常防治共識節錄─家族性高膽固醇血症之診斷與治療」之「台灣 FH 建議診斷標準」評分總和超過 8 分（108/5/1）。<br>
    　II. 經遺傳基因檢測未檢出同合子基因變異或多重不同基因異常之同合子家族性高膽固醇血症患者，至少須符合以下三種臨床徵狀：（108/5/1、109/4/1）i. 10 歲前出現皮膚或肌腱黃色瘤。ii. 未經藥物治療之 LDL-C &gt;500 mg/dL 且經降高血脂藥物治療後 &gt;330mg/dL。iii. 父母有高膽固醇血症（未經藥物治療之 TC &gt;250mg/dL）。iv. 20 歲前發生冠心病。<br>
    (2) 需經事前審查核准使用，每次申請之療程以 6 個月為限。 (3) 使用後需每 6 個月評估一次 LDL-C，若 LDL-C 連續二次未較治療前降低 18% 以上，則不予同意再使用。 (4) 限每 4 週使用 1 次，每次最多使用 3 支，或每 2 週使用 1 支。（109/4/1）
  </div>
  <h3 style="font-size:15px;color:var(--brand-ink);margin-top:14px">2.6.4.2 Alirocumab（如 Praluent）（109/1/1、114/9/1）</h3>
  <div class="rule-text">
    限使用於發生重大心血管事件之病人：<br>
    1. 須經事前審查核准後使用（請詳附表二-D），每次申請得核准使用 12 個月，再次申請須檢附評估報告，若血中 LDL-C 較本藥物開始使用前下降程度未達 30%，即屬療效不佳，則不再給付。（114/9/1）<br>
    2. 限給付於發生重大心血管事件之後一年內且使用最大耐受劑量 statin 之病人，如心肌梗塞、接受冠狀動脈或其他動脈血管再通術（revascularization）、動脈硬化相關之缺血性腦中風等之動脈粥狀硬化心血管疾病之成人病人，且符合下列條件之一者：（114/9/1）(1) 經使用高強度 statin（如 rosuvastatin 20mg 或 atorvastatin 40 mg（含）以上）或病人可耐受之最大劑量的 statin 三個月（含）以上且之後再合併使用 ezetimibe 10 mg 三個月（含）以上，LDL-C 仍高於 100 mg/dL 者。(2) 對 statin 有禁忌症或確診為對 statin 不耐受之病人，經其他降血脂藥物（至少需有 ezetimibe 10 mg）持續治療 3 個月，LDL-C 仍高於 100 mg/dL 者。<br>
    3. 最高劑量為每兩週使用 1 支。 4. 不可同時使用其他 PCSK9 血脂調節劑。
  </div>
  <div class="notice info" style="margin-top:12px"><b>注意：</b>依所收錄條文，同合子家族性高膽固醇血症（HoFH）之給付途徑僅列於 evolocumab（2.6.4.1 第 2 點）；alirocumab 限用於發生重大心血管事件之病人。</div>
</div>
<div class="card">
  <h2>附表二-D 使用健保給付 PCSK9 血脂調節劑事前審查申請表：重點</h2>
  <div class="rule-text">
    <b>3.1 重大心血管疾病（必要條件）</b>：以下診斷至少需符合一項，首次申請限給付於在發病後一年內開始使用最大耐受劑量 statin 之病人：□ 心肌梗塞　□ 動脈硬化相關之缺血性腦中風發作　□ 接受冠狀動脈或其他動脈血管再通術（Revascularization）；並填寫發病日期。<br>
    <b>3.2 符合 PCSK9 血脂調節劑原因（必要條件，至少符合一項）</b>：<br>
    (1) 經使用高強度 statin（如 rosuvastatin 20mg 或 atorvastatin 40 mg（含）以上）或病人可耐受之最大劑量的 statin 三個月（含）以上且之後再合併使用 ezetimibe 10 mg 三個月（含）以上，LDL-C 仍高於 100 mg/dL 之成人病人。（甲、statin 治療期間；如未達上述劑量，請詳述最大耐受劑量之 statin 和原因。乙、ezetimibe 治療期間。）<br>
    (2) 病人有下列 statin 禁忌症且持續使用 ezetimibe 治療三個月，LDL-C 仍高於 100 mg/dL：□ 藥物過敏（請說明使用之成分名稱、藥品名稱及健保代碼，和所提報之過敏反應及其發病過程佐證資料）□ 活動性肝病變（請詳附佐證資料）。<br>
    (3) 診斷為對 statin 不耐受之患者，且持續使用 ezetimibe 治療三個月，LDL-C 仍高於 100 mg/dL：甲、statin 之副作用：□ 確認為嚴重橫紋肌溶解症，只需一種 statin 即可以診斷 statin 不耐受（請詳附佐證資料）□ 肌肉或肝臟相關副作用或疾病（需符合中華民國血脂及動脈硬化學會 2019 年之共識規定，Myalgia score for statin intolerance 須大於 8 分，請附相關佐證資料）□ 其他。乙、同時是否有確認對「兩種」statin 產生上述副作用（檢附病歷紀錄），其中一種是在最低有效劑量下均有不耐受之情況（需註明藥品成分、藥品名稱及健保代碼）。每日最低有效劑量：rosuvastatin 5 mg、atorvastatin 10 mg、pravastatin 10 mg、lovastatin 20 mg、fluvastatin 20 mg、pitavastatin 1 mg、simvastatin 5 mg（可採每週累積之最低劑量計算）。<br>
    <b>3.3</b> 申請前一年內所有 LDL-C 之報告（首次申請者填寫，最多四次）。<b>3.4</b> 首次使用 PCSK9 調節劑治療前之 LDL-C 報告及前次治療期間所有 LDL-C 之報告（再次申請者填寫）。<br>
    <b>四、申請種類</b>：最高劑量為每兩週使用 1 支，本類藥品不可同時使用，僅得擇一申請：□ Praluent 保脂通（Alirocumab）　□ Repatha 瑞百安（Evolocumab）。
  </div>
</div>
</section>

<!-- ================= CONSENSUS ================= -->
<section class="panel" id="panel-consensus" role="tabpanel">
<div class="card">
  <h2>2025 台灣血脂管理臨床路徑共識：摘要</h2>
  <p class="muted" style="font-size:13px">李貽恒、石崇良，與中華民國心臟學會、中華民國血脂及動脈硬化學會、台灣介入性心臟血管醫學會、台灣內科醫學會、台灣腦中風學會、台灣家庭醫學醫學會、中華民國糖尿病學會、中華民國糖尿病衛教學會、台灣腎臟醫學會、衛生福利部中央健康保險署。內科學誌 2024;35:426-430。</p>
  <h3 style="font-size:15px;color:var(--brand-ink);margin-top:10px">風險分級與 LDL-C／non-HDL-C 治療目標</h3>
  <div class="tbl-wrap"><table class="tbl">
    <thead><tr><th>風險等級</th><th>目標對象定義</th><th>LDL-C 目標</th><th>non-HDL-C 目標（次要）</th></tr></thead>
    <tbody>
      <tr><td><b style="color:var(--r-l)">低</b></td><td>1 項心血管風險因子</td><td>&lt;130 mg/dL</td><td>&lt;160 mg/dL</td></tr>
      <tr><td><b style="color:var(--r-m)">中</b></td><td>≧2 項心血管風險因子</td><td>&lt;115 mg/dL</td><td>&lt;145 mg/dL</td></tr>
      <tr><td><b style="color:var(--r-h)">高</b></td><td>糖尿病；慢性腎臟病（透析前，UACR ≧30 mg/g 或 eGFR &lt;60 至少 3 個月）；LDL-C ≧190 mg/dL；CAC ≧400</td><td>&lt;100 mg/dL</td><td>&lt;130 mg/dL</td></tr>
      <tr><td><b style="color:var(--r-vh)">非常高</b></td><td>經臨床檢查確診 ASCVD（ACS 病史；血管再通術 PCI/CABG；缺血性中風／TIA 合併動脈硬化相關疾病病史；PAD 曾再通術／肢體缺血症狀／截肢）；或影像確認 ≧50% 直徑狹窄之顯著斑塊負擔（冠狀動脈攝影；冠狀動脈或周邊血管 CT；頸動脈或周邊血管超音波）</td><td>&lt;70 mg/dL</td><td>&lt;100 mg/dL</td></tr>
      <tr><td><b style="color:var(--r-ext)">極高</b></td><td>CAD 合併：一年內 MI；≧2 次 MI；多支冠狀動脈阻塞；ACS 合併糖尿病；PAD 或頸動脈狹窄。或 PAD 合併 CAD 或頸動脈狹窄</td><td>&lt;55 mg/dL</td><td>&lt;85 mg/dL</td></tr>
    </tbody>
  </table></div>
  <p style="font-size:14px">心血管風險因子：高血壓；年齡（男 ≧45、女 ≧55 歲）；早發性冠心病家族史（男 ≦55、女 ≦65 歲）；HDL-C（男 &lt;40、女 &lt;50 mg/dL）；抽菸；代謝性症候群（腹部肥胖、血壓偏高、空腹血糖偏高、空腹 TG 偏高、HDL-C 偏低五項符合至少三項）。除血脂控制外，居家血壓應控制在 &lt;130/80 mmHg，血糖 HbA1c &lt;7%（可個別化考量）。</p>
  <h3 style="font-size:15px;color:var(--brand-ink);margin-top:14px">初級預防臨床路徑（圖一）</h3>
  <ol style="font-size:14px">
    <li>評估：給予完整血脂指標檢測，辨識可改善之心血管風險因子（血壓、HbA1c、肥胖、抽菸、酒精攝取、生活型態）。符合糖尿病、慢性腎臟病或 LDL-C ≧190 mg/dL 屬高風險；有嚴重高膽固醇血症、肌腱黃色瘤、早發心血管疾病或家族病史時，應依台灣家族性高膽固醇血症診斷標準進行 FH 篩檢（可考慮基因檢測確認）。未符合高風險者以風險因子數量評估。</li>
    <li>高風險（LDL-C ≧100）：依基線 LDL-C 與臨床狀況給予<b>中至高強度 statin 或合併 ezetimibe</b>，同時進行生活型態改變 → 第 6–8 週檢測血脂 → 達標：維持治療，每 6 個月追蹤；未達標：檢視服藥狀況，可考慮高強度 statin 或最大耐受劑量或同時合併 non-statin（ezetimibe、PCSK9 單株抗體、siRNA、ATP citrate lyase 抑制劑）→ 更動治療 1–3 個月內追蹤。</li>
    <li>中風險（≧2 項風險因子且 LDL-C ≧115）／低風險（1 項且 LDL-C ≧130）：先進行生活型態改變並處置風險因子 → 3–6 個月後檢測血脂 → 未達標可考慮<b>中強度 statin</b>（醫病共享決策）→ 治療 6–8 週後追蹤 → 未達標：檢視服藥狀況，可使用高強度 statin 或最大耐受劑量或合併 non-statin。達標後每 6–12 個月追蹤。</li>
  </ol>
  <h3 style="font-size:15px;color:var(--brand-ink);margin-top:14px">次級預防臨床路徑（圖二）</h3>
  <ol style="font-size:14px">
    <li>初始評估應檢測完整血脂指標，急性病人入院後 24 小時內完成；處置各項可改善之心血管風險因子；應完整評估風險增強因子決定治療目標（非常高 &lt;70；極高 &lt;55 mg/dL）。</li>
    <li>起始治療：依基線 LDL-C、用藥史和臨床狀況，給予<b>中至高強度 statin 或合併 ezetimibe</b>。起始用藥選擇可依預期達到的 LDL-C 降幅、過去用藥史與臨床狀況決定；若臨床判斷單獨使用 statin 無法達到目標，可考慮<b>早期結合 non-statin 藥物</b>。</li>
    <li>第 6–8 週檢測血脂 → 達標：維持治療，每半年追蹤完整血脂指標；未達標：檢視服藥狀況，應考慮調整至高強度 statin 或最大耐受 statin 劑量，同時考慮合併 non-statin（ezetimibe、PCSK9 單株抗體、siRNA、ATP citrate lyase 抑制劑）→ 更動治療 1–3 個月內追蹤是否達標。</li>
  </ol>
  <h3 style="font-size:15px;color:var(--brand-ink);margin-top:14px">處置與監測、遵從度、其他血脂指標</h3>
  <ul style="font-size:14px">
    <li>起始治療後第 6–8 週檢測血脂；更動治療後 1–3 個月內再次追蹤，直至達標。達標後：高風險以上每 6 個月追蹤完整血脂指標；低至中風險原則上每 6–12 個月（可依臨床狀況決定）。</li>
    <li>肝功能：起始治療以及每次劑量增加後的 3 個月內同時追蹤，無變化者後續不需重複，除非有臨床需求。</li>
    <li>遵從度策略：治療開始時向病人說明其 LDL-C 目標；應用數位工具（如健保快易通）提升自我照護；提供衛教資訊與互動素材。每次返診重新評估藥物效果與遵從性。</li>
    <li>LDL-C 達標後以 non-HDL-C（TC − HDL-C）為次要標的（尤適合併高 TG、糖尿病或肥胖者），目標為 LDL-C 目標加 30 mg/dL（低至極高依序 &lt;160、&lt;145、&lt;130、&lt;100、&lt;85 mg/dL）。ApoB、Lipoprotein(a) 亦具獨立預測作用，可依臨床狀況與可近性納入評估。</li>
    <li>CTT 統合分析：LDL-C 每降低 1 mmol/L（38.7 mg/dL），約減少 22% 重大心血管事件、20% 冠心病死亡與 10% 全因死亡；效益隨治療時間累積。</li>
  </ul>
</div>
</section>

<!-- ================= ABOUT ================= -->
<section class="panel" id="panel-about" role="tabpanel">
<div class="card">
  <h2>使用說明</h2>
  <ol style="font-size:14px">
    <li>依序完成步驟 1–5（性別、年齡、LDL-C 為判定核心；TC/HDL-C 可算 non-HDL-C）。右側（手機為下方）結果即時更新。</li>
    <li>結果包含：ASCVD 風險分級與依據、LDL-C／non-HDL-C 目標與達標狀態、LDL-C 目標尺（可視化所需降幅與 statin 強度預期降幅）、共識用藥建議（是否用藥、藥物類別與強度、statin 學名劑量）、健保給付判定（statin 依表一，或於選取不適用表一之品項時自動改依表二；2.6.2 ezetimibe、2.6.3 複方、2.6.4 PCSK9）、追蹤時程與注意事項。</li>
    <li>「複製摘要」可將輸入與建議轉為純文字貼入病歷；「列印」輸出結果頁。</li>
    <li>可直接以單一 HTML 檔案部署於任何網頁伺服器或內網，無外部相依資源。</li>
  </ol>
</div>
<div class="card">
  <h2>判定邏輯與解讀說明（重要）</h2>
  <ul style="font-size:14px">
    <li><b>風險分級順序</b>：先判定極高 → 非常高（ASCVD）→ 高（糖尿病／CKD／LDL-C ≧190／CAC ≧400）→ 以風險因子數量判定中／低／0 項。極高與非常高之定義完全依共識表一與健保表一文字。</li>
    <li><b>冠狀動脈疾病之推定</b>：勾選 ACS、MI、多支阻塞或冠狀動脈再通術，即視為具「冠狀動脈疾病」（用於極高風險之「CAD 合併…」判定）。「急性冠心症合併糖尿病」由 ACS（含 MI）與糖尿病兩項自動判定。</li>
    <li><b>頸動脈狹窄</b>：單獨勾選時依「影像確認 ≧50% 直徑狹窄之顯著斑塊負擔（頸動脈超音波）」歸為非常高風險；與 CAD 或 PAD 併存時為極高風險。若狹窄程度未達 50%，請勿勾選此項。</li>
    <li><b>PAD 與 TIA</b>：PAD 定義為曾再通術、有肢體缺血相關症狀或截肢；TIA 須合併動脈硬化相關疾病或病史。PCSK9 之「重大心血管事件」僅計入心肌梗塞、冠狀動脈或其他動脈血管再通術與動脈硬化相關之缺血性腦中風（TIA 不計）。</li>
    <li><b>年齡與 HDL-C 風險因子</b>及代謝性症候群之 TG、HDL-C 項目由輸入數值自動判定；未輸入時不計入，並以「未輸入」提示。</li>
    <li><b>所需降幅與強度建議</b>：所需降幅＝（目前 LDL-C − 目標）／目前 LDL-C。強度預期降幅引自 2026 ACC/AHA Table 6（高 ≧50%、中 30–49%、低 &lt;30%），ezetimibe 加於 statin 之額外降幅約 25%（同指引 4.2.1.2 節）。此為族群估計值，個別反應差異大，僅供起始選藥參考；是否達標仍以 6–8 週後之實測值為準。</li>
    <li><b>健保判定</b>：表一 statin 之「符合」係指 LDL-C 達起始藥物治療血脂值（且中／低風險已完成 3–6 個月生活型態改變）。步驟 5 選取之品項若列於「不適用表一」清單（2.6.1 所列 116 項），statin 判定自動改依<b>表二（原給付規定）</b>：依表二之對象分類（ACS／PCI-CABG；心血管疾病或糖尿病；危險因子 2／1／0 個）、起始血脂值（含 TC）、非藥物治療要求與處方規定判定，詳見「健保表二」頁籤之判定邏輯說明。Ezetimibe／複方之判定依 statin 單一治療期間（6–8 週；列表品項 3 個月）與是否達標。PCSK9 依 2.6.4 各項要件逐一檢核並列出未符合之項目；本工具不涉及事前審查之實際核定。</li>
    <li><b>非本工具範圍</b>：降三酸甘油酯藥物之給付判定（僅於選用 Pravafen 時附帶參考）、inclisiran 與 bempedoic acid 之健保給付條件、兒童與孕婦。</li>
  </ul>
</div>
<div class="card">
  <h2>資料來源</h2>
  <ol style="font-size:14px">
    <li>李貽恒、石崇良等。2025 台灣血脂管理臨床路徑共識。內科學誌 2024;35:426-430。DOI:10.6314/JIMT.202412_35(6).04</li>
    <li>衛生福利部中央健康保險署。「藥品給付規定」修訂對照表 第 2 節 心臟血管及腎臟藥物（2.6.1 全民健康保險降血脂藥物給付規定表、2.6.2 Ezetimibe、2.6.3 含 ezetimibe 及 statin 類之複方製劑），自 115 年 9 月 1 日生效。</li>
    <li>衛生福利部中央健康保險署。藥品給付規定 2.6.1 全民健康保險降血脂藥物給付規定表（86/1/1、87/4/1、87/7/1、91/9/1、93/9/1、97/7/1、102/8/1、108/2/1；含降膽固醇藥物給付規定表〔表二〕與降三酸甘油酯藥物給付規定表）。</li>
    <li>衛生福利部中央健康保險署。藥品給付規定 2.6.4 PCSK9 血脂調節劑（2.6.4.1 Evolocumab、2.6.4.2 Alirocumab；114/9/1 修訂）及附表二-D 事前審查申請表。</li>
    <li>Blumenthal RS, et al. 2026 ACC/AHA/AACVPR/ABC/ACPM/ADA/AGS/APhA/ASPC/NLA/PCNA Guideline on the Management of Dyslipidemia. JACC 2026;87:2624-2757. Table 6（statin 強度）與 4.2.1.2 節（non-statin 降幅）。</li>
  </ol>
  <p class="muted" style="font-size:12.5px">本工具為臨床決策輔助與教育用途，不取代醫師之專業判斷；健保給付以健保署公告及審查結果為準。頁面版本：2026-08 v2（依 115/9/1 生效版本編製；含表二原給付規定）。</p>
</div>
</section>
</main>

<div class="mbar" id="mbar">
  <div class="grow"><span class="mb-risk" id="mbRisk">請輸入資料</span> <span class="mb-t" id="mbTarget"></span></div>
  <button type="button" class="btn primary small" id="mbBtn">查看建議</button>
</div>
<div class="toast" id="toast"></div>

<script>
/* ============================================================
   血脂治療決策工具 — 規則引擎（純函式，可獨立測試）
   ============================================================ */
(function(root){
'use strict';
const TABLE2_ONLY = [
  ["simvastatin","AC46402100","Simvatin film coating tablets 20mg"],
  ["simvastatin","AB47348100","Vatatin F.C. tablets 20mg \"STANDARD\""],
  ["simvastatin","BC24339100","Simvahexal film-coated tablets 40mg"],
  ["simvastatin","AC49672100","Simatin F.C. tablets 20mg"],
  ["simvastatin","AC49841100","Simpotin F.C. tablets 20 mg \"Weidar\""],
  ["simvastatin","AC47924100","Zostatin F.C. tablets 20 mg \"S.C.\""],
  ["simvastatin","BC23970100","Simvahexal film-coated tablets 20mg"],
  ["simvastatin","AC49360100","Bezostatin F.C. tablets 40 mg \"S.C.\""],
  ["simvastatin","AC48813100","Simvatenin F.C. tablets 20mg (simvastatin)"],
  ["simvastatin","AC56804100","Simvastatin F.C. tablets 20mg \"CYH\""],
  ["simvastatin","AC49699100","Simatin F.C. tablets 10mg"],
  ["simvastatin","AC47907100","Sinty F.C. tablets 20mg"],
  ["simvastatin","AC48926100","Simva F.C. tablets 20 mg"],
  ["simvastatin","AC49190100","Sivasin film coated tablets 40mg"],
  ["simvastatin","AC58207100","Simvatin film coating tablets 40mg"],
  ["simvastatin","AC48608100","Simva F.C. tablets 20mg \"Union\""],
  ["simvastatin","AC49997100","Simatin F.C. tablets 40 mg"],
  ["simvastatin","A055967100","Simva F.C. tablets 40mg \"Union\""],
  ["simvastatin","AC56806100","Sinty F.C. tablets 40mg"],
  ["lovastatin","AC39403100","Lozutin tablets 20mg (lovastatin)"],
  ["lovastatin","AC39307100","Delipic tablets 20mg \"Standard\" (lovastatin)"],
  ["lovastatin","A042389100","Lovatin tablets 20mg \"PANBIOTIC\""],
  ["pravastatin","BC23596100","Mevalotin protect 40mg tablets"],
  ["pravastatin","AC52581100","Joinlo tablets 40mg “EVEREST”"],
  ["pravastatin","AB49454100","Pratin tablets 40 mg (pravastatin sodium)"],
  ["pravastatin","AB48586100","Pavatin protect tablets 20mg \"Standard\" (pravastatin sodium)"],
  ["pravastatin","AB48681100","U-Chu Pavadin tablets 20 mg"],
  ["pravastatin","AB46029100","Pratin tablets 10mg (pravastatin sodium)"],
  ["pravastatin","AB48644100","Mechol tablets 20mg \"Yung Shin\""],
  ["pravastatin","AB49021100","Pratin tablets 20 mg"],
  ["pravastatin","BC23597100","Mevalotin protect 20mg tablets"],
  ["pravastatin","AC57126100","Pavatin protect tablets 40mg \"Standard\" (pravastatin sodium)"],
  ["pravastatin","AC48469100","Mechol tablets 10mg \"Yung Shin\""],
  ["pravastatin","AC57741100","Joinlo tablet 20mg EVEREST"],
  ["fluvastatin","BC23556100","Lescol XL film-coated tablets 80mg"],
  ["fluvastatin","BC26147100","Fluvastatin XL film-coated tablets 80mg"],
  ["fluvastatin","AC56629100","Lecitol XL film-coated Tablets 80mg"],
  ["atorvastatin","AC55272100","Atorva film-coated tablets 10mg \"Standard\" (atorvastatin)"],
  ["atorvastatin","BA25337100","Tulip 20mg film coated tablets"],
  ["atorvastatin","BA25200100","Tulip 10mg film coated tablets"],
  ["atorvastatin","AC48879100","Anxolipo F.C. tablet 10 mg"],
  ["atorvastatin","AC57267100","Atotin F.C. tablets 10mg"],
  ["atorvastatin","AC51598100","Atoty F.C. tablets 10 mg"],
  ["atorvastatin","AC58211100","Atotin F.C. tablets 20mg"],
  ["atorvastatin","AC49226100","Anxolightor F.C. tablets 20 mg"],
  ["atorvastatin","AC58517100","Atoroty F.C. tablets 20mg"],
  ["atorvastatin","AC57805100","Atorva F.C. tab. 20mg \"Standard\" (atorvastatin)"],
  ["atorvastatin","AA49543100","Atorin F.C. tablet 10mg"],
  ["atorvastatin","BA25201100","Tulip 40mg film coated tablets"],
  ["atorvastatin","AA57774100","Atover F.C. Tab. 10mg P.L."],
  ["atorvastatin","AC52530100","Atorin F.C. tablets 20mg"],
  ["atorvastatin","AC55583100","Atorcal F.C. tablets 20mg \"S.C.\""],
  ["atorvastatin","AC55895100","Atorcal F.C. tablets 10mg \"S.C.\""],
  ["atorvastatin","AA57950100","Atover F.C. tablets 20mg P.L."],
  ["atorvastatin","AC55268100","Atorva film-coated tablets 40mg \"Standard\"(atorvastatin)"],
  ["atorvastatin","AC55952100","Atoty F.C. tablets 20 mg"],
  ["atorvastatin","AA56739100","Anxolipo F.C. tablets 20mg"],
  ["atorvastatin","AC55956100","Lipiminus F.C. tablets 20mg"],
  ["atorvastatin","AB54967100","Atover F.C. tablets 40 mg \"P.L.\""],
  ["atorvastatin","AA49288100","Anxolipo F.C. tablets 40mg"],
  ["atorvastatin","AC56319100","Lipiminus F.C.tablets 10mg"],
  ["atorvastatin","AC57133100","Atotin F.C. tablets 40mg"],
  ["atorvastatin","AC52301100","Lipiminus F.C tablets 40mg"],
  ["atorvastatin","AC57930100","Atova F.C. tablets 10mg \"Yu Sheng\""],
  ["atorvastatin","AC56682100","Atoroty F.C. tablets 10mg"],
  ["atorvastatin","AC50086100","Atorcal F.C. tablets 40 mg \"S.C.\""],
  ["atorvastatin","AB57967100","Atorstin film coated tablets 10mg"],
  ["atorvastatin","AC58041100","Atoty F.C. tablets 40mg"],
  ["atorvastatin","AB57772100","Atorstin film coated tablets 40mg"],
  ["atorvastatin","AB58049100","Atorstin film coated tablets 20mg"],
  ["atorvastatin","AB51732100","Atorin F.C. tablets 40mg"],
  ["atorvastatin","AC58262100","Atoroty F.C. tablets 40mg"],
  ["rosuvastatin","AA57802100","Roty F.C. tablets 10mg"],
  ["rosuvastatin","AA57843100","Roty F.C. tablets 5mg"],
  ["rosuvastatin","BC24597100","Crestor 5mg film-coated tablets"],
  ["rosuvastatin","AC57803100","Roty F.C. tablets 20mg"],
  ["rosuvastatin","BC24129100","Crestor 20mg film-coated tablets"],
  ["rosuvastatin","AB57940100","Rosulator F.C. tablets 10mg \"S.C.\""],
  ["rosuvastatin","BC26543100","Alvostat film coated tablets 10mg"],
  ["rosuvastatin","AC59266100","Rostatin F.C. tablets 5mg \"Standard\""],
  ["rosuvastatin","AC58282100","Rostatin F.C. tablets 10mg \"Standard\""],
  ["rosuvastatin","AC58384100","Rosu F.C. tablets 10mg"],
  ["rosuvastatin","AC57130100","Rotlip film-coated tablets 10mg"],
  ["rosuvastatin","AC59652100","Rosulator F.C. tablets 5mg \"S.C.\""],
  ["rosuvastatin","AC57809100","Rolipostatin 10mg F.C. tablets \"Macro\""],
  ["rosuvastatin","BC26900100","Zyrova 20 (rosuvastatin tablets 20mg)"],
  ["rosuvastatin","BC27782100","Zyrova 5 (rosuvastatin tablets 5mg)"],
  ["rosuvastatin","AC58969100","Aladdin F.C. tablets 10mg"],
  ["rosuvastatin","BC27781100","Zyrova 10 (rosuvastatin tablets 10mg)"],
  ["rosuvastatin","AC58067100","Rosutor film-coated tablets 10mg"],
  ["rosuvastatin","BC26544100","Alvostat film coated tablets 20mg"],
  ["rosuvastatin","AC60114100","Rosutor film-coated tablets 5mg"],
  ["rosuvastatin","AC59649100","Rosulip F.C. tablets 5mg C.H."],
  ["rosuvastatin","AC58270100","Crosuty F.C. tablets 10mg"],
  ["rosuvastatin","AC58622100","Rotlip film-coated tablets 5mg"],
  ["rosuvastatin","AC58098100","Crosuty F.C. tablets 5mg"],
  ["rosuvastatin","AC60197100","Rosutor film-coated tablets 20mg"],
  ["pitavastatin","BC25350100","Livalo tablets 2mg"],
  ["pitavastatin","AA58648100","Pitarty F.C. tablets 2mg"],
  ["pitavastatin","BC27002100","Livalo OD tablets 2mg"],
  ["pitavastatin","AC58526100","Pitastatin F.C. tablets 2mg"],
  ["pitavastatin","AC58633100","Pitarty F.C. tablets 4mg"],
  ["pitavastatin","AC58525100","Pitastatin F.C. tablets 4mg"],
  ["pitavastatin","AC59398100","Pivas F.C. tablets 2mg"],
  ["pitavastatin","AC59192100","Pitanxo F.C. tablets 4mg"],
  ["pitavastatin","AC60561100","\"EVEREST\" Huiton F.C. tablets 2mg"],
  ["pitavastatin","AC61795100","Pistatin F.C. tablets 2mg"],
  ["pitavastatin","AC58078100","Pitavol F.C.tablets 2mg"],
  ["pitavastatin","AC60174100","Pitavastatin F.C. tablets 2mg \"CYH\""],
  ["pitavastatin","AC59193100","Pitanxo F.C. tablets 2mg"],
  ["pitavastatin","AC60290100","Lavitol film coated tablets 4mg"],
  ["pravastatin 及 fenofibrate 複方","BC26169100","Pravafen 40mg/160mg hard capsules"],
  ["atorvastatin 及 amlodipine 複方","BC24392100","Caduet 5mg/20mg tablet"],
  ["atorvastatin 及 amlodipine 複方","BC24391100","Caduet 5mg/10mg tablet"],
  ["atorvastatin 及 amlodipine 複方","AC59887100","Dualpress F.C. tablets 5mg/10mg"],
  ["atorvastatin 及 amlodipine 複方","AC60836100","Dualpress F.C. tablets 5mg/20mg"]
];
const T2_INFO = { // 不適用表一之品項：健保代碼 → [statin 成分, 每日劑量]（劑量由品名解析；複方以其 statin 成分之含量計）
  "AC46402100":["simvastatin","20 mg"], "AB47348100":["simvastatin","20 mg"], "BC24339100":["simvastatin","40 mg"], "AC49672100":["simvastatin","20 mg"],
  "AC49841100":["simvastatin","20 mg"], "AC47924100":["simvastatin","20 mg"], "BC23970100":["simvastatin","20 mg"], "AC49360100":["simvastatin","40 mg"],
  "AC48813100":["simvastatin","20 mg"], "AC56804100":["simvastatin","20 mg"], "AC49699100":["simvastatin","10 mg"], "AC47907100":["simvastatin","20 mg"],
  "AC48926100":["simvastatin","20 mg"], "AC49190100":["simvastatin","40 mg"], "AC58207100":["simvastatin","40 mg"], "AC48608100":["simvastatin","20 mg"],
  "AC49997100":["simvastatin","40 mg"], "A055967100":["simvastatin","40 mg"], "AC56806100":["simvastatin","40 mg"], "AC39403100":["lovastatin","20 mg"],
  "AC39307100":["lovastatin","20 mg"], "A042389100":["lovastatin","20 mg"], "BC23596100":["pravastatin","40 mg"], "AC52581100":["pravastatin","40 mg"],
  "AB49454100":["pravastatin","40 mg"], "AB48586100":["pravastatin","20 mg"], "AB48681100":["pravastatin","20 mg"], "AB46029100":["pravastatin","10 mg"],
  "AB48644100":["pravastatin","20 mg"], "AB49021100":["pravastatin","20 mg"], "BC23597100":["pravastatin","20 mg"], "AC57126100":["pravastatin","40 mg"],
  "AC48469100":["pravastatin","10 mg"], "AC57741100":["pravastatin","20 mg"], "BC23556100":["fluvastatin","XL 80 mg"], "BC26147100":["fluvastatin","XL 80 mg"],
  "AC56629100":["fluvastatin","XL 80 mg"], "AC55272100":["atorvastatin","10 mg"], "BA25337100":["atorvastatin","20 mg"], "BA25200100":["atorvastatin","10 mg"],
  "AC48879100":["atorvastatin","10 mg"], "AC57267100":["atorvastatin","10 mg"], "AC51598100":["atorvastatin","10 mg"], "AC58211100":["atorvastatin","20 mg"],
  "AC49226100":["atorvastatin","20 mg"], "AC58517100":["atorvastatin","20 mg"], "AC57805100":["atorvastatin","20 mg"], "AA49543100":["atorvastatin","10 mg"],
  "BA25201100":["atorvastatin","40 mg"], "AA57774100":["atorvastatin","10 mg"], "AC52530100":["atorvastatin","20 mg"], "AC55583100":["atorvastatin","20 mg"],
  "AC55895100":["atorvastatin","10 mg"], "AA57950100":["atorvastatin","20 mg"], "AC55268100":["atorvastatin","40 mg"], "AC55952100":["atorvastatin","20 mg"],
  "AA56739100":["atorvastatin","20 mg"], "AC55956100":["atorvastatin","20 mg"], "AB54967100":["atorvastatin","40 mg"], "AA49288100":["atorvastatin","40 mg"],
  "AC56319100":["atorvastatin","10 mg"], "AC57133100":["atorvastatin","40 mg"], "AC52301100":["atorvastatin","40 mg"], "AC57930100":["atorvastatin","10 mg"],
  "AC56682100":["atorvastatin","10 mg"], "AC50086100":["atorvastatin","40 mg"], "AB57967100":["atorvastatin","10 mg"], "AC58041100":["atorvastatin","40 mg"],
  "AB57772100":["atorvastatin","40 mg"], "AB58049100":["atorvastatin","20 mg"], "AB51732100":["atorvastatin","40 mg"], "AC58262100":["atorvastatin","40 mg"],
  "AA57802100":["rosuvastatin","10 mg"], "AA57843100":["rosuvastatin","5 mg"], "BC24597100":["rosuvastatin","5 mg"], "AC57803100":["rosuvastatin","20 mg"],
  "BC24129100":["rosuvastatin","20 mg"], "AB57940100":["rosuvastatin","10 mg"], "BC26543100":["rosuvastatin","10 mg"], "AC59266100":["rosuvastatin","5 mg"],
  "AC58282100":["rosuvastatin","10 mg"], "AC58384100":["rosuvastatin","10 mg"], "AC57130100":["rosuvastatin","10 mg"], "AC59652100":["rosuvastatin","5 mg"],
  "AC57809100":["rosuvastatin","10 mg"], "BC26900100":["rosuvastatin","20 mg"], "BC27782100":["rosuvastatin","5 mg"], "AC58969100":["rosuvastatin","10 mg"],
  "BC27781100":["rosuvastatin","10 mg"], "AC58067100":["rosuvastatin","10 mg"], "BC26544100":["rosuvastatin","20 mg"], "AC60114100":["rosuvastatin","5 mg"],
  "AC59649100":["rosuvastatin","5 mg"], "AC58270100":["rosuvastatin","10 mg"], "AC58622100":["rosuvastatin","5 mg"], "AC58098100":["rosuvastatin","5 mg"],
  "AC60197100":["rosuvastatin","20 mg"], "BC25350100":["pitavastatin","2 mg"], "AA58648100":["pitavastatin","2 mg"], "BC27002100":["pitavastatin","2 mg"],
  "AC58526100":["pitavastatin","2 mg"], "AC58633100":["pitavastatin","4 mg"], "AC58525100":["pitavastatin","4 mg"], "AC59398100":["pitavastatin","2 mg"],
  "AC59192100":["pitavastatin","4 mg"], "AC60561100":["pitavastatin","2 mg"], "AC61795100":["pitavastatin","2 mg"], "AC58078100":["pitavastatin","2 mg"],
  "AC60174100":["pitavastatin","2 mg"], "AC59193100":["pitavastatin","2 mg"], "AC60290100":["pitavastatin","4 mg"], "BC26169100":["pravastatin","40 mg"],
  "BC24392100":["atorvastatin","20 mg"], "BC24391100":["atorvastatin","10 mg"], "AC59887100":["atorvastatin","10 mg"], "AC60836100":["atorvastatin","20 mg"]
};
const EZE_LISTED = [
  ["AC60610100","Ezetity tablets 10mg"],
  ["BC27311100","Ezzicad (ezetimibe) 10mg Tablets"],
  ["BC28252100","Ezta 10 (ezetimibe Tablets 10mg)"],
  ["BC26552100","Ezetimibe Sandoz 10mg tablets"]
];
const FDC_LISTED = [
  ["AC59251100","Agitin tablets 10/20mg"],
  ["AC60402100","Sacure tablets 10/20mg"],
  ["BC28502100","Ezta-SM 10+20 (ezetimibe and simvastatin tablets 10mg/20mg)"],
  ["AC62052100","Zoliton tablets 10/20mg"],
  ["AC62053100","Zoliton tablets 10/10mg"],
  ["AC62140100","Zovastin tablets 10/10mg"],
  ["AC62139100","Zovastin tablets 10/20mg"],
  ["BC28181100","Cretrol Tab. 10/10 mg"],
  ["BC28182100","Cretrol Tab. 10/20 mg"],
  ["BC28884100","Livazebe combination tablets HD (for 4mg)"]
];

const STATIN_DOSES = {
  atorvastatin: [['10 mg','mod'],['20 mg','mod'],['40 mg','hi'],['80 mg','hi']],
  rosuvastatin: [['5 mg','mod'],['10 mg','mod'],['20 mg','hi'],['40 mg','hi']],
  simvastatin:  [['10 mg','lo'],['20 mg','mod'],['40 mg','mod'],['80 mg（FDA 不建議起始或調升）','mod']],
  pravastatin:  [['10 mg','lo'],['20 mg','lo'],['40 mg','mod'],['80 mg','mod']],
  lovastatin:   [['20 mg','lo'],['40 mg','mod'],['80 mg','mod']],
  fluvastatin:  [['20 mg','lo'],['40 mg','lo'],['40 mg BID','mod'],['XL 80 mg','mod']],
  pitavastatin: [['1 mg','mod'],['2 mg','mod'],['4 mg','mod']],
  other: [['未知／其他','']]
};
const INTENSITY_NAME = {hi:'高強度（預期 LDL-C 降幅 ≧50%）', mod:'中強度（預期 30–49%）', lo:'低強度（預期 <30%）'};
const STATIN_LISTS = {
  hi:  ['Atorvastatin 40–80 mg', 'Rosuvastatin 20–40 mg'],
  mod: ['Atorvastatin 10–20 mg', 'Rosuvastatin 5–10 mg', 'Simvastatin 20–40 mg', 'Pravastatin 40–80 mg', 'Lovastatin 40–80 mg', 'Fluvastatin XL 80 mg 或 40 mg BID', 'Pitavastatin 1–4 mg'],
  lo:  ['Simvastatin 10 mg', 'Pravastatin 10–20 mg', 'Lovastatin 20 mg', 'Fluvastatin 20–40 mg']
};
const TIERS = {
  EXT:{key:'EXT', name:'極高風險', short:'極高', ldl:55,  nonhdl:85,  group:'secondary'},
  VH: {key:'VH',  name:'非常高風險', short:'非常高', ldl:70, nonhdl:100, group:'secondary'},
  H:  {key:'H',   name:'高風險', short:'高', ldl:100, nonhdl:130, group:'high'},
  M:  {key:'M',   name:'中風險', short:'中', ldl:115, nonhdl:145, group:'lowmod'},
  L:  {key:'L',   name:'低風險', short:'低', ldl:130, nonhdl:160, group:'lowmod'},
  Z:  {key:'Z',   name:'0 項心血管風險因子', short:'0 項風險因子', ldl:160, nonhdl:null, group:'lowmod'}
};

function num(v){ return (v===null||v===undefined||v===''||isNaN(v)) ? null : Number(v); }
function doseMg(doseStr){ const m=/^(\d+(?:\.\d+)?)/.exec(String(doseStr||'').replace(/^XL\s*/,'')); return m?Number(m[1]):null; }
function intensityOf(drug, dose){
  const arr=STATIN_DOSES[drug]; if(!arr) return null;
  const f=arr.find(x=>x[0]===dose); return f? (f[1]||null) : null;
}
function isNhiHighIntensity(drug, dose){
  const mg=doseMg(dose);
  return (drug==='rosuvastatin' && mg!==null && mg>=20) || (drug==='atorvastatin' && mg!==null && mg>=40);
}

/* ---------- 風險分級 ---------- */
function classify(s){
  const c=s.checks||{}, sex=s.sex, age=num(s.age), ldl=num(s.ldl), hdl=num(s.hdl), tg=num(s.tg);
  const hasCAD = !!(c.cad||c.acs||c.mi||c.multivessel||c.revasc);
  const hasACS = !!(c.acs||c.mi);
  const hasPAD = !!(c.pad||c.padRevasc);
  const ext=[];
  if(hasCAD){
    if(c.mi1y) ext.push('冠狀動脈疾病，一年內曾經歷心肌梗塞');
    if(c.mi2) ext.push('冠狀動脈疾病，≧兩次心肌梗塞病史');
    if(c.multivessel) ext.push('多支冠狀動脈阻塞');
    if(hasACS && c.dm) ext.push('急性冠心症合併糖尿病');
    if(hasPAD) ext.push('冠狀動脈疾病合併周邊動脈疾病');
    if(c.carotid) ext.push('冠狀動脈疾病合併頸動脈狹窄');
  } else if(hasPAD && c.carotid){
    ext.push('周邊動脈疾病合併頸動脈狹窄');
  }
  const vh=[];
  if(c.cad) vh.push('經臨床檢查確診之冠狀動脈疾病');
  if(hasACS) vh.push('急性冠心症病史');
  if(c.revasc) vh.push('接受血管再通術（PCI／CABG）');
  if(c.stroke) vh.push('動脈硬化相關之缺血性中風');
  if(c.tia) vh.push('TIA 合併動脈硬化相關疾病或病史');
  if(hasPAD) vh.push('周邊動脈疾病');
  if(c.imaging50) vh.push('影像確認 ≧50% 直徑狹窄之顯著斑塊負擔');
  if(c.carotid && !hasCAD && !hasPAD) vh.push('頸動脈狹窄（影像 ≧50% 之顯著斑塊負擔）');
  const hi=[];
  if(c.dm) hi.push('糖尿病');
  if(c.ckd) hi.push('慢性腎臟病');
  if(ldl!==null && ldl>=190) hi.push('LDL-C ≧190 mg/dL（'+ldl+'）');
  if(c.cac400) hi.push('冠狀動脈鈣化分數 ≧400');

  const ageRF = (sex && age!==null) ? (sex==='M' ? age>=45 : age>=55) : null;
  const hdlRF = (sex && hdl!==null) ? (sex==='M' ? hdl<40 : hdl<50) : null;
  const ms = {
    waist: !!c.ms_waist,
    bp: !!(c.ms_bp||c.htn),
    fpg: !!(c.ms_fpg||c.dm),
    tg: !!(c.ms_tg||(tg!==null&&tg>=150)),
    hdl: hdlRF===true
  };
  const msCount = ['waist','bp','fpg','tg','hdl'].filter(k=>ms[k]).length;
  const metS = msCount>=3;
  const rf = [
    {k:'htn', name:'高血壓', met:!!c.htn},
    {k:'age', name:'年齡（男 ≧45／女 ≧55 歲）', met:ageRF===true, unknown:ageRF===null},
    {k:'fhx', name:'早發性冠心病家族史', met:!!c.fhx},
    {k:'hdl', name:'HDL-C 偏低（男 <40／女 <50）', met:hdlRF===true, unknown:hdlRF===null},
    {k:'smoking', name:'抽菸', met:!!c.smoking},
    {k:'ms', name:'代謝性症候群（'+msCount+'／5 項）', met:metS}
  ];
  const rfCount = rf.filter(x=>x.met).length;
  const unknowns = rf.filter(x=>x.unknown).map(x=>x.name);
  let tier, reasons;
  if(ext.length){ tier='EXT'; reasons=ext; }
  else if(vh.length){ tier='VH'; reasons=vh; }
  else if(hi.length){ tier='H'; reasons=hi; }
  else if(rfCount>=2){ tier='M'; reasons=['心血管風險因子 '+rfCount+' 項：'+rf.filter(x=>x.met).map(x=>x.name).join('、')]; }
  else if(rfCount===1){ tier='L'; reasons=['心血管風險因子 1 項：'+rf.filter(x=>x.met).map(x=>x.name).join('、')]; }
  else { tier='Z'; reasons=['未勾選任何 ASCVD／高風險條件，且心血管風險因子 0 項'+(unknowns.length?'（'+unknowns.join('、')+' 未輸入，無法自動判定）':'')]; }
  return {tier, reasons, rf, rfCount, unknowns, ms, msCount, metS, ageRF, hdlRF, hasCAD, hasACS, hasPAD, ldl190: ldl!==null&&ldl>=190};
}


/* ---------- 表二：原「全民健康保險降膽固醇藥物給付規定表」（86/1/1…108/2/1）---------- */
const T2ROWS = {
  ACS:{key:'ACS', name:'有急性冠狀動脈症候群病史，或曾接受心導管介入治療／外科冠動脈搭橋手術之冠狀動脈粥狀硬化患者', nondrug:'與藥物治療可並行', wait:false, start:{ldl:70}, goal:{ldl:70}, startTxt:'LDL-C ≧70 mg/dL', goalTxt:'LDL-C <70 mg/dL'},
  CVD:{key:'CVD', name:'心血管疾病或糖尿病患者', nondrug:'與藥物治療可並行', wait:false, start:{tc:160,ldl:100}, goal:{tc:160,ldl:100}, startTxt:'TC ≧160 mg/dL 或 LDL-C ≧100 mg/dL', goalTxt:'TC <160 mg/dL 或 LDL-C <100 mg/dL'},
  RF2:{key:'RF2', name:'2 個危險因子或以上', nondrug:'給藥前應有 3–6 個月非藥物治療', wait:true, start:{tc:200,ldl:130}, goal:{tc:200,ldl:130}, startTxt:'TC ≧200 mg/dL 或 LDL-C ≧130 mg/dL', goalTxt:'TC <200 mg/dL 或 LDL-C <130 mg/dL'},
  RF1:{key:'RF1', name:'1 個危險因子', nondrug:'給藥前應有 3–6 個月非藥物治療', wait:true, start:{tc:240,ldl:160}, goal:{tc:240,ldl:160}, startTxt:'TC ≧240 mg/dL 或 LDL-C ≧160 mg/dL', goalTxt:'TC <240 mg/dL 或 LDL-C <160 mg/dL'},
  RF0:{key:'RF0', name:'0 個危險因子', nondrug:'給藥前應有 3–6 個月非藥物治療', wait:true, start:{ldl:190}, goal:{ldl:190}, startTxt:'LDL-C ≧190 mg/dL', goalTxt:'LDL-C <190 mg/dL'}
};
const T2_RX = '第一年應每 3–6 個月抽血檢查一次，第二年以後應至少每 6–12 個月抽血檢查一次，同時請注意副作用之產生如肝功能異常、橫紋肌溶解症';
const T2_TG_RX = T2_RX;
function t2Info(code){ return T2_INFO[code] || null; }
function isT2Product(code){ return !!T2_INFO[code]; }
// 依表二之「心血管疾病定義」與「危險因子定義」分類（與表一／共識之分級互相獨立）
function classifyT2(s, opts){
  opts=opts||{}; const c=s.checks||{}, sex=s.sex, age=num(s.age), hdl=num(s.hdl);
  const smoking = opts.ignoreSmoking ? false : !!c.smoking;
  const hasACS=!!(c.acs||c.mi), revasc=!!c.revasc;
  const cad2=!!(c.cad||c.multivessel||hasACS||revasc);
  const cvdReasons=[];
  if(cad2) cvdReasons.push('冠狀動脈粥狀硬化患者');
  if(c.stroke) cvdReasons.push('腦梗塞');
  if(c.tia) cvdReasons.push('暫時性腦缺血（TIA）');
  if(c.carotid&&c.carotidSym) cvdReasons.push('有症狀之頸動脈狹窄');
  const cvd2 = cvdReasons.length>0;
  const ageRF = sex==='M' ? (age!==null ? age>=45 : null) : sex==='F' ? (c.menopause ? true : (age!==null ? age>=55 : null)) : null;
  const hdlRF = hdl!==null ? hdl<40 : null;
  const rf=[
    {k:'htn', name:'高血壓', met:!!c.htn},
    {k:'age', name:'年齡（男 ≧45 歲；女 ≧55 歲或停經者）', met:ageRF===true, unknown:ageRF===null},
    {k:'fhx', name:'早發性冠心病家族史（男 ≦55、女 ≦65 歲）', met:!!c.fhx},
    {k:'hdl', name:'HDL-C <40 mg/dL', met:hdlRF===true, unknown:hdlRF===null},
    {k:'smoking', name:'吸菸', met:smoking}
  ];
  const rfCount=rf.filter(x=>x.met).length, unknowns=rf.filter(x=>x.unknown).map(x=>x.name);
  const metNames=rf.filter(x=>x.met).map(x=>x.name);
  let row, reasons=[];
  if(hasACS||revasc){ row='ACS'; if(hasACS) reasons.push('急性冠狀動脈症候群病史'); if(revasc) reasons.push('曾接受心導管介入治療或外科冠動脈搭橋手術'); }
  else if(cvd2||c.dm){ row='CVD'; if(cvd2) reasons.push('心血管疾病：'+cvdReasons.join('、')); if(c.dm) reasons.push('糖尿病'); }
  else if(rfCount>=2){ row='RF2'; reasons.push('危險因子 '+rfCount+' 個：'+metNames.join('、')); }
  else if(rfCount===1){ row='RF1'; reasons.push('危險因子 1 個：'+metNames.join('、')); }
  else { row='RF0'; reasons.push('危險因子 0 個'+(unknowns.length?'（'+unknowns.join('、')+' 未輸入，無法自動判定）':'')); }
  const notes=[];
  if(!(hasACS||revasc||cvd2||c.dm)){
    if(c.pad||c.padRevasc) notes.push('表二之「心血管疾病定義」未列周邊動脈疾病，故 PAD 不計入表二之心血管疾病，改以危險因子個數判定');
    if(c.imaging50) notes.push('表二之心血管疾病須為「心絞痛且有心導管證實／缺氧性心電圖變化／負荷性試驗陽性」之冠狀動脈粥狀硬化，或缺血型腦血管疾病；單純影像斑塊負擔不計入。若屬心導管證實之冠狀動脈粥狀硬化，請勾選 CAD');
    if(c.carotid&&!c.carotidSym) notes.push('頸動脈狹窄僅於「有症狀且診斷經神經科醫師確立」時計入表二之缺血型腦血管疾病（請於步驟 2 勾選子項）');
  }
  if(row==='CVD' && cad2) notes.push('表二冠狀動脈粥狀硬化之認定為「心絞痛病人，有心導管證實或缺氧性心電圖變化或負荷性試驗陽性反應者」，需附檢查報告');
  if(row==='CVD' && (c.tia||(c.carotid&&c.carotidSym))) notes.push('TIA 與有症狀之頸動脈狹窄之診斷須由神經科醫師確立');
  if((row==='RF2'||row==='RF1'||row==='RF0') && sex==='F' && !c.menopause && age!==null && age<55) notes.push('女性停經者於表二計為年齡危險因子（表一不計）：如已停經請於步驟 4 勾選「已停經」');
  return {row, def:T2ROWS[row], reasons, rf, rfCount, unknowns, cvd2, hasACS, revasc, notes};
}
// 依表二某列之「起始藥物治療血脂值」與「血脂目標值」評估（TC 與 LDL-C 以「或」並列，符合其一即計；未輸入者不納入）
function evalT2(def, ldl, tc){
  const st=def.start, gl=def.goal; const sp=[], gp=[]; const sc=[], gc=[];
  if(st.tc!==undefined && tc!==null){ sc.push(tc>=st.tc); sp.push('TC '+tc+(tc>=st.tc?'（≧'+st.tc+' ✓）':'（未達 ≧'+st.tc+'）')); }
  if(ldl!==null){ sc.push(ldl>=st.ldl); sp.push('LDL-C '+ldl+(ldl>=st.ldl?'（≧'+st.ldl+' ✓）':'（未達 ≧'+st.ldl+'）')); }
  if(gl.tc!==undefined && tc!==null){ gc.push(tc<gl.tc); gp.push('TC '+tc+(tc<gl.tc?'（<'+gl.tc+' ✓）':'（未 <'+gl.tc+'）')); }
  if(ldl!==null){ gc.push(ldl<gl.ldl); gp.push('LDL-C '+ldl+(ldl<gl.ldl?'（<'+gl.ldl+' ✓）':'（未 <'+gl.ldl+'）')); }
  return { startMet: sc.length? sc.some(Boolean) : null, goalMet: gc.length? gc.some(Boolean) : null, startNow: sp.join('；'), goalNow: gp.join('；'), tcMissing: st.tc!==undefined && tc===null };
}

/* ---------- 全部評估 ---------- */
function pct(x){ return Math.round(x); }
function pctNeed(x){ return Math.max(1, Math.round(x)); } // LDL-C 未達標時所需降幅至少顯示 1%（LDL-C 恰等於目標值時避免顯示 0%）
function assess(s){
  const cls=classify(s);
  const tier=TIERS[cls.tier]; const c=s.checks||{};
  const ldl=num(s.ldl), tc=num(s.tc), hdl=num(s.hdl), age=num(s.age), preLdl=num(s.preLdl);
  const target=tier.ldl, nonhdlT=tier.nonhdl;
  const nonhdl=(tc!==null&&hdl!==null)?tc-hdl:null;
  const atGoal = ldl===null? null : ldl<target;
  const needPct = (ldl!==null && ldl>0) ? Math.max(0,(ldl-target)/ldl*100) : null;
  const status=s.status||'naive', group=tier.group;
  const intensity=intensityOf(s.statinDrug, s.statinDose);
  const nhiHigh=isNhiHighIntensity(s.statinDrug, s.statinDose);
  const durUnknown = !s.statinDur;
  const durOK68 = ['6to8w','8wto3m','ge3m'].includes(s.statinDur);
  const dur3m = s.statinDur==='ge3m';
  const P = s.product||null; const useT2 = !!(P && P.t2);
  const t2 = classifyT2(s);
  const R={cls, tier, target, nonhdlT, ldl, nonhdl, atGoal, needPct, status, group, intensity, nhiHigh, product:P, useT2, t2, alerts:[], decision:null, drugs:[], nonstatin:[], followup:[], nhi:[], summaryLines:[]};

  const fuMaintain = group==='lowmod' ? '達標後每 6–12 個月追蹤血脂指標' : '達標後每 6 個月追蹤完整血脂指標';
  const lft = '起始治療及每次劑量增加後 3 個月內追蹤肝功能，無變化者後續不需重複（除非臨床需要）';
  const needTxt = needPct!==null ? '所需降幅約 '+pctNeed(needPct)+'%' : '';

  function startAdvice(){
    const lines=[];
    if(needPct===null) return lines;
    if(group==='lowmod'){
      lines.push('共識路徑起始為中強度 statin（預期 LDL-C 降幅 30–49%）。');
      if(needPct>=50) lines.push(needTxt+'（≧50%）：中強度可能不足；6–8 週後未達標可提高至高強度或最大耐受劑量，或合併 non-statin。');
      else if(needPct>=30) lines.push(needTxt+'（30–49%）：中強度 statin 預期可達標，接近上限者建議選擇較高劑量。');
      else lines.push(needTxt+'（<30%）：中強度 statin 即可能達標。');
    } else {
      if(needPct<30) lines.push(needTxt+'（<30%）：中強度 statin 即可能達標（如 atorvastatin 10–20 mg、rosuvastatin 5–10 mg）；亦可依臨床狀況直接選高強度。');
      else if(needPct<50) lines.push(needTxt+'（30–49%）：中強度 statin 預期可達標；接近 49% 者建議直接使用高強度 statin。');
      else if(needPct<62) lines.push(needTxt+'（≧50%）：建議高強度 statin（atorvastatin 40–80 mg／rosuvastatin 20–40 mg）；若臨床判斷單用不足，可早期合併 ezetimibe。');
      else lines.push(needTxt+'：高強度 statin 單用預期不足（≧50%），建議起始即高強度 statin＋ezetimibe（共識：可早期結合 non-statin，ezetimibe 額外約 25%）；仍未達標再考慮 PCSK9 單株抗體／siRNA。');
    }
    return lines;
  }
  function escalateAdvice(){
    const lines=[];
    lines.push('檢視服藥順從性與生活型態。');
    if(intensity==='hi') lines.push('目前已為高強度 statin：確認順從性後，合併 non-statin 治療。');
    else if(intensity==='mod'||intensity==='lo') lines.push('目前為'+(intensity==='mod'?'中':'低')+'強度 statin：調整至高強度 statin（atorvastatin 40–80 mg／rosuvastatin 20–40 mg）或病人可耐受之最大劑量，並／或合併 non-statin。');
    else lines.push('調整至高強度 statin（atorvastatin 40–80 mg／rosuvastatin 20–40 mg）或病人可耐受之最大劑量，並／或合併 non-statin。');
    if(needPct!==null){
      if(status==='statin'){
        if(needPct<=25) lines.push(needTxt+'：加上 ezetimibe 10 mg（額外約 25%）即可能達標。');
        else if(needPct<=45) lines.push(needTxt+'：超過 ezetimibe 單獨加藥之預期，宜 statin 增量至高強度並合併 ezetimibe；仍未達標考慮 PCSK9 單株抗體（45–64%）／inclisiran（48–52%）。');
        else lines.push(needTxt+'：預期需 PCSK9 單株抗體（45–64%）或 inclisiran（48–52%）等；先完成高強度／最大耐受 statin＋ezetimibe 各 ≧3 個月以符合健保 PCSK9 要件。');
      } else {
        if(needPct<=20) lines.push(needTxt+'：可考慮 statin 增量至高強度／最大耐受劑量、bempedoic acid（額外約 17–18%）或 PCSK9 抑制劑。');
        else lines.push(needTxt+'：建議考慮 PCSK9 單株抗體（45–64%）或 inclisiran（48–52%）；bempedoic acid 額外約 17–18%。');
      }
    }
    lines.push('更動治療後 1–3 個月內複檢血脂，直至達標。');
    return lines;
  }
  const nonstatinAll = ['Ezetimibe 10 mg（額外約 25%；健保 2.6.2／2.6.3）','PCSK9 單株抗體 evolocumab／alirocumab（45–64%；健保 2.6.4 事前審查）','siRNA：inclisiran（48–52%）','ATP citrate lyase 抑制劑：bempedoic acid（單用 21–24%；加於最大耐受 statin 額外 17–18%）'];

  /* ---- 決策 ---- */
  let D;
  if(ldl===null){
    D={kind:'info', headline:'請輸入 LDL-C 以產生用藥建議', points:['已依勾選項目判定為「'+tier.name+'」，LDL-C 目標 <'+target+' mg/dL'+(nonhdlT?'（non-HDL-C <'+nonhdlT+' mg/dL）':'')+'。']};
  } else if(status==='naive'){
    if(group==='secondary'){
      if(ldl>=target){
        D={kind:'now', headline:'應立即開始降血脂藥物治療（次級預防）', points:[
          '起始治療：依基線 LDL-C、用藥史與臨床狀況，給予中至高強度 statin，或合併 ezetimibe。',
          ...startAdvice(),
          '同時處置各項可改善之心血管風險因子（血壓、HbA1c、肥胖、抽菸、酒精攝取、生活型態）；急性病人應於入院後 24 小時內完成血脂檢驗。'
        ]};
        R.drugs = needPct!==null && needPct<30 ? ['mod','hi'] : ['hi','mod'];
        R.nonstatin = nonstatinAll;
      } else {
        D={kind:'hold', headline:'目前 LDL-C 已低於此風險等級之目標值', points:[
          '目前 LDL-C '+ldl+' mg/dL < '+target+'：低於健保表一「起始藥物治療血脂值（LDL-C ≧'+target+'）」，不在表一起始給付條件內。',
          '共識對次級預防族群強調積極血脂控制與定期追蹤：每 6 個月追蹤完整血脂指標，並處置各項可改善之心血管風險因子；若後續 LDL-C ≧'+target+' 應即開始藥物治療。'
        ]};
      }
    } else if(group==='high'){
      if(ldl>=100){
        D={kind:'now', headline:'應開始降血脂藥物治療（高風險初級預防）', points:[
          '起始治療：依基線 LDL-C 與臨床狀況，給予中至高強度 statin 或合併 ezetimibe；同時進行生活型態改變（居家血壓 <130/80 mmHg；HbA1c <7%，可個別化）。',
          ...startAdvice()
        ]};
        R.drugs = needPct!==null && needPct<30 ? ['mod','hi'] : ['hi','mod'];
        R.nonstatin = nonstatinAll;
      } else {
        D={kind:'go', headline:'LDL-C 已達目標（<100 mg/dL），目前不需起始藥物', points:['維持生活型態改變並處置心血管風險因子；每 6 個月追蹤血脂指標。','若後續 LDL-C ≧100 mg/dL，即應開始中至高強度 statin（或合併 ezetimibe）。']};
      }
    } else { // lowmod
      if(ldl>=target){
        if(c.lifestyleDone){
          D={kind:'now', headline:'生活型態改變後仍未達標：可開始中強度 statin', points:[
            '中強度 statin（預期 LDL-C 降幅 30–49%），經醫病共享決策後開始，以強化治療與衛教遵從。',
            ...startAdvice(),
            '持續生活型態改變並處置心血管風險因子（血壓 <130/80 mmHg；HbA1c <7% 可個別化）。'
          ]};
          R.drugs=['mod'];
          R.nonstatin=[];
        } else {
          D={kind:'wait', headline:'先進行 3–6 個月生活型態改變，暫不起始藥物', points:[
            '處置心血管風險因子：健康飲食、規律運動、戒菸、控制體重；血壓 <130/80 mmHg、HbA1c <7%（可個別化）。',
            '3–6 個月後檢測血脂；未達標（LDL-C 仍 ≧'+target+'）→ 醫病共享決策後給予中強度 statin。',
            '健保表一：中／低風險給藥前應有 3–6 個月生活型態改變並處置心血管風險因子。'
          ]};
        }
      } else {
        D={kind:'go', headline:'LDL-C 已達目標，目前不需藥物治療', points:['維持生活型態並處置心血管風險因子；每 6–12 個月追蹤血脂指標。']};
      }
    }
  } else if(status==='statin'){
    if(atGoal){
      D={kind:'go', headline:'已達標：維持目前 statin 治療', points:[fuMaintain+'。', lft+'。', 'LDL-C 達標後可以 non-HDL-C 作為次要標的'+(nonhdlT?'（目標 <'+nonhdlT+' mg/dL）':'')+'。']};
    } else if(durUnknown){
      D={kind:'info', headline:'請選擇目前 statin 治療期間', points:['目前 LDL-C '+ldl+' 未達 <'+target+' mg/dL。共識於起始治療後第 6–8 週評估：未滿 6 週者維持治療並於 6–8 週複檢；已滿 6–8 週未達標者檢視服藥狀況，調整至高強度／最大耐受劑量 statin 並考慮合併 non-statin。', lft+'。']};
    } else if(!durOK68){
      D={kind:'wait', headline:'尚未到評估時點：維持治療，於起始後 6–8 週檢測血脂', points:[
        '目前 LDL-C '+ldl+' 未達 <'+target+'，但共識建議起始治療後第 6–8 週再評估是否達標。',
        ...(needPct!==null && intensity && ((intensity==='mod'&&needPct>=50)||(intensity==='lo'&&needPct>=30)) ? ['依目前 statin 強度（'+INTENSITY_NAME[intensity]+'）與所需降幅約 '+pctNeed(needPct)+'%，預期單用可能不足，可預先規劃 6–8 週後之增量或合併治療。'] : []),
        lft+'。'
      ]};
    } else {
      D={kind:'now', headline:'statin 單一治療 6–8 週以上仍未達標：強化治療', points:escalateAdvice()};
      R.drugs = intensity==='hi' ? [] : ['hi'];
      R.nonstatin = nonstatinAll;
    }
  } else if(status==='statin_eze'){
    if(atGoal){
      D={kind:'go', headline:'已達標：維持 statin＋ezetimibe', points:[fuMaintain+'。', lft+'。']};
    } else {
      D={kind:'now', headline:'statin＋ezetimibe 仍未達標：檢視順從性並考慮進一步 non-statin', points:escalateAdvice()};
      R.drugs = intensity==='hi' ? [] : ['hi'];
      R.nonstatin = nonstatinAll.slice(1);
    }
  } else if(status==='intolerant'){
    const pts=['Statin 不耐受／禁忌症者以 non-statin 治療：ezetimibe（健保 2.6.2 第 1 款）、PCSK9 單株抗體（2.6.4 途徑 II）、inclisiran、bempedoic acid。'];
    if(!c.intolConfirmed && !c.ci) pts.push('若欲申請 PCSK9，需符合「確診 statin 不耐受」（嚴重橫紋肌溶解症；或 Myalgia score >8 且對兩種 statin 不耐受，其中一種為最低有效劑量）或禁忌症之要件。');
    if(atGoal){ D={kind:'go', headline:'已達標：維持目前 non-statin 治療', points:[fuMaintain+'。']}; }
    else {
      if(needPct!==null){
        if(needPct<=18) pts.push(needTxt+'：ezetimibe 10 mg（平均約 18%）即可能達標。');
        else if(needPct<=24) pts.push(needTxt+'：ezetimibe（約 18%）可能不足，可考慮加上 bempedoic acid（單用 21–24%）或 PCSK9 抑制劑。');
        else pts.push(needTxt+'：預期需 PCSK9 單株抗體（45–64%）或 inclisiran（48–52%）；健保 PCSK9 途徑 II 需 ezetimibe（至少）持續 3 個月且 LDL-C 仍 >100 mg/dL。');
      }
      pts.push('更動治療後 1–3 個月內複檢。');
      D={kind:'now', headline:'statin 不耐受且未達標：以 non-statin 達標', points:pts};
      R.nonstatin = nonstatinAll;
    }
  } else if(status==='pcsk9'){
    const pts=[];
    if(preLdl!==null && ldl!==null && preLdl>0){
      const red=(preLdl-ldl)/preLdl*100;
      const th = c.hofh?18:30;
      pts.push('LDL-C 由用藥前 '+preLdl+' 降至 '+ldl+' mg/dL，下降 '+pct(red)+'%'+(red>=th?'（≧'+th+'%，符合續用之療效門檻）':'（未達 '+th+'%，屬療效不佳，依規定不再給付／不同意續用）')+'。');
      D={kind: red>=th?'go':'now', headline: red>=th?'PCSK9 療效達續用門檻':'PCSK9 療效未達續用門檻', points:pts};
    } else {
      D={kind:'info', headline:'請輸入 PCSK9 使用前 LDL-C 以評估續用', points:['續用要件：再次申請須檢附評估報告，LDL-C 較用藥前下降未達 30% 即屬療效不佳（HoFH：每 6 個月評估，連續二次未達 18% 不同意續用）。']};
    }
    pts.push(atGoal? '目前 LDL-C 已達目標 <'+target+' mg/dL；'+fuMaintain+'。' : '目前 LDL-C '+ldl+' 未達 <'+target+' mg/dL；持續最大耐受 statin＋ezetimibe，PCSK9 最高每兩週 1 支。');
  }
  R.decision=D;

  /* ---- 追蹤 ---- */
  if(group==='lowmod'){
    R.followup=['未用藥者：生活型態改變 3–6 個月後檢測血脂','起始 statin 後 6–8 週檢測血脂；達標維持，每 6–12 個月追蹤；未達標檢視服藥狀況並調整','更動治療後 1–3 個月內複檢',lft];
  } else {
    R.followup=['起始治療後 6–8 週檢測血脂指標','達標：維持治療並每 6 個月追蹤完整血脂指標；未達標：檢視服藥狀況，調整至高強度／最大耐受 statin 並考慮合併 non-statin','更動治療後 1–3 個月內複檢，直至達標',lft];
    if(group==='secondary') R.followup.unshift('急性病人入院後 24 小時內完成血脂檢驗；處置血壓、HbA1c、肥胖、抽菸、酒精、生活型態');
  }

  /* ---- 健保：Statin 表一（115/9/1 新制）---- */
  const ST_LABEL={ok:'符合', no:'不符合', cond:'有條件／尚未符合', na:'不適用／無需求'};
  function statinT1Item(){
    const it={name:'Statin（降膽固醇藥物給付規定表一，115/9/1）', st:'na', det:[], table:'T1'};
    if(ldl===null){ it.det.push('請輸入 LDL-C。'); }
    else if(status==='intolerant'){ it.st='na'; it.det.push('statin 不耐受／禁忌症者：改依 2.6.2 ezetimibe 第 1 款及 2.6.4 PCSK9 途徑 II 判定。'); }
    else if(status==='naive'){
      if(ldl>=target){
        if(group==='lowmod' && !c.lifestyleDone){ it.st='cond'; it.det.push('LDL-C '+ldl+' ≧ 起始藥物治療血脂值 '+target+' mg/dL，但中／低風險給藥前應有 3–6 個月生活型態改變並處置心血管風險因子；複檢未達標後給予中強度 statin。'); }
        else { it.st='ok'; it.det.push('LDL-C '+ldl+' ≧ 起始藥物治療血脂值 '+target+' mg/dL，符合表一起始藥物治療條件（'+(group==='lowmod'?'中強度 statin':'中至高強度 statin 或合併 ezetimibe')+'）。'); }
      } else { it.st='no'; it.det.push('LDL-C '+ldl+' < 起始藥物治療血脂值 '+target+' mg/dL，未達表一起始藥物治療條件。'); }
    } else {
      it.st='ok';
      it.det.push(atGoal ? '治療達標：維持治療，並'+(group==='lowmod'?'每 6–12 個月':'每 6 個月')+'追蹤血脂指標（表一處方規定）。' : '未達標：檢視服藥狀況，'+(group==='lowmod'?'可給予高強度 statin 或最大耐受劑量或合併 non-statin':'考慮調整至高強度 statin 或最大耐受劑量，同時考慮合併 non-statin')+'（表一處方規定）。');
    }
    return it;
  }
  /* ---- 健保：Statin 表二（原給付規定；僅適用 2.6.1 所列品項）---- */
  function statinT2Item(){
    const def=t2.def;
    const it={name:'Statin（表二：原降膽固醇藥物給付規定表）', st:'na', det:[], checklist:[], table:'T2', t2row:t2.row};
    it.det.push('所選品項「'+P.name+'」（'+P.code+'）列於 2.6.1「不適用表一」清單，僅適用表二；以下依表二判定。');
    it.det.push('表二對象：'+def.name+'（依據：'+t2.reasons.join('；')+'）。');
    if(ldl===null && tc===null){ it.det.push('請輸入 LDL-C（此列亦可以 TC 判定者，可另輸入 TC）。'); t2.notes.forEach(n=>it.det.push('註：'+n+'。')); return it; }
    if(status==='intolerant'){ it.det.push('statin 不耐受／禁忌症者：改依 2.6.2 ezetimibe 第 1 款及 2.6.4 PCSK9 途徑 II 判定。'); return it; }
    const ev=evalT2(def, ldl, tc);
    if(status==='naive'){
      it.checklist.push({t:'起始藥物治療血脂值：'+def.startTxt, m: ev.startMet===null?'q':(ev.startMet?'y':'n'), note: ev.startNow+(ev.tcMissing?'；未輸入 TC，僅以 LDL-C 判定':'')});
      it.checklist.push({t:'非藥物治療：'+def.nondrug, m: def.wait ? (c.lifestyleDone?'y':'n') : 'y', note: def.wait ? (c.lifestyleDone?'已完成 3–6 個月非藥物治療':'尚未完成／未勾選 3–6 個月非藥物治療（步驟 5）') : '不需先行非藥物治療期'});
    } else {
      it.checklist.push({t:'起始藥物治療血脂值：'+def.startTxt+'（適用於治療前基線值）', m:'q', note:'治療中：目前 '+ev.startNow.replace(/（[^）]*）/g,'')+' 為治療中數值，起始條件以治療前基線值為準，本工具不以目前值判定'});
    }
    it.checklist.push({t:'血脂目標值：'+def.goalTxt, m: ev.goalMet===null?'q':(ev.goalMet?'y':'n'), note: ev.goalNow+((def.goal.tc!==undefined && tc!==null && ldl!==null)?'（表二以「或」並列，符合其一即計）':'')});
    if(status==='naive'){
      if(ev.startMet===true){
        if(def.wait && !c.lifestyleDone){ it.st='cond'; it.det.push('血脂值已達表二起始藥物治療值，但此列規定給藥前應有 3–6 個月非藥物治療；完成後仍未達標即符合給付。'); }
        else { it.st='ok'; it.det.push('符合表二起始藥物治療條件。'); }
      } else if(ev.startMet===false){ it.st='no'; it.det.push('未達表二「起始藥物治療血脂值」（'+def.startTxt+'），不符合表二給付條件。'); }
      // 吸菸註記：因吸菸而符合起步治療準則者，若未戒菸而要求藥物治療，應以自費治療
      if(ev.startMet===true && c.smoking && (t2.row==='RF2'||t2.row==='RF1')){
        const t2b=classifyT2(s,{ignoreSmoking:true}); const evb=evalT2(t2b.def, ldl, tc);
        if(evb.startMet!==true){ it.selfPay=true; it.det.push('⚠ 本個案係「因吸菸而符合起步治療準則」（不計吸菸時為「'+t2b.def.name+'」，起始值 '+t2b.def.startTxt+' 未達）：若未戒菸而要求藥物治療，應以自費治療（表二危險因子定義第 5 點）。'); }
      }
    } else {
      it.st='ok';
      it.det.push('治療中：'+(ev.goalMet===true ? '目前血脂值已達表二血脂目標值，維持治療。' : ev.goalMet===false ? '目前血脂值未達表二血脂目標值；表二未訂調整處方之細則，臨床上依共識路徑調整。' : '請輸入血脂值以判定是否達表二目標。'));
    }
    it.det.push('處方規定：'+T2_RX+'。');
    t2.notes.forEach(n=>it.det.push('註：'+n+'。'));
    return it;
  }
  if(useT2){
    const it2=statinT2Item(); const it1=statinT1Item();
    if(ldl!==null && status!=='intolerant') it2.det.push('對照：若改用適用表一之品項，表一（'+tier.name+'，起始值 LDL-C ≧'+target+' mg/dL）判定為「'+ST_LABEL[it1.st]+'」。');
    R.nhi.push(it2);
    if(status!=='intolerant') R.alerts.push({k:'info', t:'所選品項「'+P.name+'」不適用表一（115/9/1 新制），statin 之給付判定已改依表二（原給付規定）；ezetimibe、複方與 PCSK9 之判定不受影響。共識之用藥建議與 LDL-C 目標仍為臨床依據，表二之血脂目標值僅為給付規定。'});
    if(it2.selfPay) R.alerts.push({k:'warn', t:'表二：本個案係因吸菸而符合起步治療準則，若未戒菸而要求藥物治療，應以自費治療。'});
  } else {
    const it1=statinT1Item();
    if(P && P.t2===false) it1.det.push('所輸入品項「'+P.name+'」未列於「不適用表一」清單，適用表一。');
    else if(!P) it1.det.push('未指定品項時以表一判定；如擬處方／目前使用之 statin 品項列於「不適用表一」清單（2.6.1 所列 116 項），請於步驟 5 選取品項，將自動改依表二判定。');
    R.nhi.push(it1);
  }

  /* ---- 健保：Ezetimibe 2.6.2 ---- */
  (function(){
    const it={name:'Ezetimibe 單方（2.6.2）', st:'na', det:[]};
    const listedNote='列表品項（Ezetity、Ezzicad、Ezta 10、Ezetimibe Sandoz）需 statin 單一治療 3 個月未達標。';
    if(status==='naive'){
      if(ldl!==null && ldl>=target){ it.st='cond'; it.det.push('尚未使用 statin：起始即合併 ezetimibe 不在 2.6.2 給付條件內；需經 statin 單一治療 6–8 週未達目標（列表品項 Ezetity、Ezzicad、Ezta 10、Ezetimibe Sandoz 需 3 個月），或對 statin 發生無法耐受之藥物不良反應。'); }
      else it.det.push('目前無給付需求。');
    } else if(status==='statin'){
      if(atGoal){ it.det.push('已達標，無加藥需求。'); }
      else if(durUnknown){ it.st='cond'; it.det.push('請選擇 statin 治療期間：單一治療 6–8 週未達目標得併用（列表品項需 3 個月）。'); }
      else if(!durOK68){ it.st='no'; it.det.push('statin 單一治療尚未滿 6–8 週，未符合併用條件（列表品項需 3 個月）。'); }
      else if(dur3m){ it.st='ok'; it.det.push('statin 單一治療 ≧3 個月未達目標：所有品項皆得併用 ezetimibe。'); }
      else { it.st='ok'; it.det.push('statin 單一治療 6–8 週未達目標：得併用非列表品項之 ezetimibe。'+listedNote); }
    } else if(status==='statin_eze'){
      it.st='ok'; it.det.push('使用中（原併用須符合 statin 單一治療 6–8 週／列表品項 3 個月未達目標之要件）；達標維持、未達標依表一處方規定調整。');
    } else if(status==='intolerant'){
      if(c.intolADR||c.intolConfirmed){ it.st='ok'; it.det.push('對 statin 發生無法耐受之藥物不良反應（如 severe myalgia、myositis）：符合 2.6.2 第 1 款。'); }
      else { it.st='cond'; it.det.push('請確認屬「對 statin 發生無法耐受藥物不良反應（如 severe myalgia、myositis）」以符合第 1 款；單純禁忌症未列於 2.6.2 條文。'); }
    } else if(status==='pcsk9'){
      it.st='ok'; it.det.push('PCSK9 申請要件已含 ezetimibe 治療；持續併用。');
    }
    it.det.push('限原發性高膽固醇血症、同型接合子家族性高膽固醇血症、同型接合子性麥脂醇血症患者。');
    R.nhi.push(it);
  })();

  /* ---- 健保：複方 2.6.3 ---- */
  (function(){
    const it={name:'Ezetimibe＋statin 複方（2.6.3）', st:'na', det:[]};
    const listedNote='列表品項（Agitin、Sacure、Ezta-SM、Zoliton、Zovastin、Cretrol、Livazebe）需 statin 單一治療 3 個月未達標。';
    if(status==='naive'){
      if(ldl!==null && ldl>=target){ it.st='cond'; it.det.push('需經 statin 單一治療 6–8 週未達目標（列表品項 Agitin、Sacure、Ezta-SM、Zoliton、Zovastin、Cretrol、Livazebe 需 3 個月），始得使用複方。'); } else it.det.push('目前無給付需求。');
    } else if(status==='statin'){
      if(atGoal){ it.det.push('已達標，無加藥需求。'); }
      else if(durUnknown){ it.st='cond'; it.det.push('請選擇 statin 治療期間：單一治療 6–8 週未達目標得使用（列表品項需 3 個月）。'); }
      else if(!durOK68){ it.st='no'; it.det.push('statin 單一治療尚未滿 6–8 週。'); }
      else if(dur3m){ it.st='ok'; it.det.push('statin 單一治療 ≧3 個月未達目標：所有複方品項皆得使用。'); }
      else { it.st='ok'; it.det.push('statin 單一治療 6–8 週未達目標：得使用非列表品項之複方。'+listedNote); }
    } else if(status==='statin_eze'){
      it.st='ok'; it.det.push('可改用含 ezetimibe 及 statin 之複方（前提：先前 statin 單一治療 6–8 週／列表品項 3 個月未達目標）。');
    } else if(status==='intolerant'){
      it.st='no'; it.det.push('複方含 statin，不適用 statin 不耐受／禁忌症者。');
    } else if(status==='pcsk9'){
      it.det.push('依現行 statin＋ezetimibe 組合決定，條件同上。');
    }
    it.det.push('限原發性高膽固醇血症、HoFH 病患；不得與 gemfibrozil 併用。');
    R.nhi.push(it);
  })();

  /* ---- 健保：PCSK9 2.6.4 ---- */
  (function(){
    const it={name:'PCSK9 單株抗體（2.6.4 evolocumab／alirocumab）', st:'na', det:[], checklist:[]};
    const majorEvent = !!(c.mi||c.revasc||c.padRevasc||c.stroke);
    const adult = age===null ? null : age>=18;
    const ldlGt100 = ldl!==null && ldl>100;
    const ezeDurOK = (status==='intolerant') ? (c.ezeOn && s.ezeDur2==='ge3m') : (s.ezeDur==='ge3m');
    const routeI = {
      applicable: (status==='statin_eze'||status==='pcsk9'||status==='statin'),
      c1: (nhiHigh||!!c.statinMax), c2: dur3m, c3: (status==='statin_eze'||status==='pcsk9') && s.ezeDur==='ge3m', c4: ldlGt100
    };
    const routeII = { applicable: status==='intolerant', d1: !!(c.ci||c.intolConfirmed), d2: !!(c.ezeOn && s.ezeDur2==='ge3m'), d3: ldlGt100 };
    const rI = routeI.applicable && routeI.c1 && routeI.c2 && routeI.c3 && routeI.c4;
    const rII = routeII.applicable && routeII.d1 && routeII.d2 && routeII.d3;
    if(status==='pcsk9'){
      const drugName = s.pcsk9Drug ? (s.pcsk9Drug==='evolocumab'?'Evolocumab（Repatha）':'Alirocumab（Praluent）') : 'PCSK9';
      if(preLdl!==null && ldl!==null && preLdl>0){
        const red=(preLdl-ldl)/preLdl*100; const th=c.hofh?18:30;
        it.st = red>=th?'ok':'no';
        it.det.push(drugName+'：LDL-C 較用藥前下降 '+pct(red)+'%'+(red>=th?'（≧'+th+'%）符合續用門檻；每次申請核准 '+(c.hofh?'6':'12')+' 個月，再次申請檢附評估報告。':'（未達 '+th+'%）屬療效不佳，依規定不再給付。'));
      } else { it.det.push('請輸入 PCSK9 使用前 LDL-C 以計算下降幅度（續用門檻 ≧30%；HoFH ≧18%）。'); }
      it.det.push('最高劑量每兩週 1 支；不可同時使用其他 PCSK9 血脂調節劑。');
      R.nhi.push(it); return;
    }
    if(ldl===null){ it.det.push('請輸入 LDL-C。'); R.nhi.push(it); return; }
    if(status==='naive'){
      if(majorEvent){ it.st='cond'; it.det.push('有重大心血管事件，但尚未用藥：需先使用高強度（rosuvastatin ≧20 mg／atorvastatin ≧40 mg）或最大耐受劑量 statin ≧3 個月，之後再合併 ezetimibe 10 mg ≧3 個月，LDL-C 仍 >100 mg/dL，且首次申請限發病後一年內開始使用最大耐受劑量 statin 之病人。'); }
      else { it.st='no'; it.det.push('無重大心血管事件（心肌梗塞／冠狀動脈或其他動脈血管再通術／動脈硬化相關之缺血性腦中風），不屬 2.6.4 給付對象。'); }
      R.nhi.push(it); return;
    }
    it.checklist.push({t:'重大心血管事件（心肌梗塞／冠狀動脈或其他動脈血管再通術／動脈硬化相關之缺血性腦中風）', m: majorEvent?'y':'n', note: majorEvent?'':'依步驟 2 之勾選，未達此要件（TIA、單純 ACS 或影像狹窄不計）'});
    it.checklist.push({t:'發病後一年內開始使用最大耐受劑量 statin（首次申請要件）', m: c.event1y?'y':'n'});
    it.checklist.push({t:'成人病人', m: adult===false?'n':(adult===null?'q':'y'), note: adult===null?'未輸入年齡':''});
    if(status==='intolerant'){
      it.checklist.push({t:'途徑 II：對 statin 有禁忌症或確診 statin 不耐受', m: routeII.d1?'y':'n'});
      it.checklist.push({t:'途徑 II：其他降血脂藥物（至少含 ezetimibe 10 mg）持續治療 ≧3 個月', m: routeII.d2?'y':'n'});
      it.checklist.push({t:'LDL-C 仍高於 100 mg/dL（目前 '+ldl+'）', m: ldlGt100?'y':'n'});
    } else {
      it.checklist.push({t:'途徑 I：高強度 statin（rosuvastatin ≧20 mg／atorvastatin ≧40 mg）或病人可耐受之最大劑量', m: routeI.c1?'y':'n', note: routeI.c1?'':'請選擇符合之 statin 劑量或勾選「最大耐受劑量」'});
      it.checklist.push({t:'途徑 I：上述 statin 使用 ≧3 個月', m: routeI.c2?'y':'n'});
      it.checklist.push({t:'途徑 I：之後再合併 ezetimibe 10 mg ≧3 個月', m: routeI.c3?'y':'n', note: status==='statin'?'尚未併用 ezetimibe：先依 2.6.2 加藥':''});
      it.checklist.push({t:'LDL-C 仍高於 100 mg/dL（目前 '+ldl+'）', m: ldlGt100?'y':'n'});
    }
    const core = majorEvent && c.event1y && adult!==false && (rI||rII);
    if(!majorEvent){ it.st='no'; it.det.push('無重大心血管事件，不屬 2.6.4「發生重大心血管事件之病人」給付對象。'); }
    else if(core){ it.st='ok'; it.det.push('符合 PCSK9 事前審查申請要件（'+(rI?'途徑 I':'途徑 II')+'）：須經事前審查核准（附表二-D），每次核准 12 個月；最高每兩週 1 支；不可同時使用兩種 PCSK9；再次申請 LDL-C 需較用藥前下降 ≧30%。'); }
    else { it.st='cond'; it.det.push('尚有未符合之要件（見下列檢核）。'); }
    if(c.hofh){
      const hofhOK = c.hofh6m && c.hofhCriteria && ldl>130;
      it.det.push('HoFH 途徑（僅 evolocumab）：'+(hofhOK?'符合（最高忍受劑量 statin＋ezetimibe 6 個月、LDL-C >130、符合診斷要件）；每次療程 6 個月，每 6 個月評估，連續二次未降 ≧18% 不同意續用；限每 4 週 1 次最多 3 支或每 2 週 1 支。':'尚未符合：需 statin＋ezetimibe 最高忍受劑量合併治療 6 個月且 LDL-C 仍 >130 mg/dL（目前 '+ldl+'），並符合基因／臨床診斷要件。'));
      if(it.st==='no' && hofhOK) it.st='ok';
      else if(it.st!=='ok' && c.hofh) it.st = hofhOK?'ok':it.st;
    }
    R.nhi.push(it);
  })();

  /* ---- 健保：降三酸甘油酯藥物給付規定表（同表二文件；僅於選用 pravastatin＋fenofibrate 複方時供參考）---- */
  if(P && P.code==='BC26169100'){
    const it={name:'降三酸甘油酯藥物給付規定表（同表二文件；本品含 fenofibrate，供參考）', st:'na', det:[], checklist:[], table:'TG'};
    const tg=num(s.tg); const ratio=(tc!==null&&hdl!==null&&hdl>0)? tc/hdl : null;
    const cvdOrDm = t2.row==='ACS' || t2.row==='CVD';
    if(tg===null){ it.det.push('請輸入 TG（並建議輸入 TC 與 HDL-C 以計算 TC/HDL-C）。'); }
    else {
      const c2 = (ratio!==null && ratio>5) || (hdl!==null && hdl<40);
      const c2Known = ratio!==null || hdl!==null;
      const nowTxt='TG '+tg+'；TC/HDL-C '+(ratio!==null?ratio.toFixed(2):'—')+'；HDL-C '+(hdl!==null?hdl:'—');
      let rowName, nondrug, wait=false, met=null, goalTxt;
      if(cvdOrDm){ rowName='心血管疾病或糖尿病病人'; nondrug='與藥物治療可並行'; goalTxt='TG <200 mg/dL'; met = tg>=200 ? (c2Known ? c2 : null) : false;
        it.checklist.push({t:'起始藥物治療三酸甘油酯值：TG ≧200 mg/dL 且（TC/HDL-C >5 或 HDL-C <40 mg/dL）', m: met===null?'q':(met?'y':'n'), note: nowTxt+(tg>=200&&!c2Known?'；需 TC/HDL-C 或 HDL-C 以判定':'')}); }
      else if(tg>=500){ rowName='無心血管疾病病人（TG ≧500 mg/dL）'; nondrug='與藥物治療可並行'; goalTxt='TG <500 mg/dL'; met=true;
        it.checklist.push({t:'起始藥物治療三酸甘油酯值：TG ≧500 mg/dL', m:'y', note:'TG '+tg}); }
      else { rowName='無心血管疾病病人'; nondrug='給藥前應有 3–6 個月非藥物治療'; wait=true; goalTxt='TG <200 mg/dL'; met = tg>=200 ? (c2Known ? c2 : null) : false;
        it.checklist.push({t:'起始藥物治療三酸甘油酯值：TG ≧200 mg/dL 且（TC/HDL-C >5 或 HDL-C <40 mg/dL）', m: met===null?'q':(met?'y':'n'), note: nowTxt+(tg>=200&&!c2Known?'；需 TC/HDL-C 或 HDL-C 以判定':'')}); }
      it.det.push('對象：'+rowName+'（心血管疾病依表二定義）；非藥物治療：'+nondrug+'；三酸甘油酯目標值：'+goalTxt+'。');
      if(wait) it.checklist.push({t:'非藥物治療：給藥前應有 3–6 個月非藥物治療', m: c.lifestyleDone?'y':'n', note: c.lifestyleDone?'已完成':'尚未完成／未勾選（步驟 5）'});
      if(met===true) it.st = (wait && !c.lifestyleDone) ? 'cond' : 'ok'; else if(met===false) it.st='no'; else it.st='cond';
      it.det.push('處方規定：'+T2_TG_RX+'。');
      if(status!=='naive'){ it.det.push('治療中：起始三酸甘油酯值以治療前基線值為準；上列以目前值判定僅供參考。'); }
    }
    it.det.push('註：2.6.1 將 Pravafen（pravastatin＋fenofibrate）列為不適用表一、僅適用表二之品項，其降膽固醇給付依上方表二判定；本表為同一文件所附之降三酸甘油酯藥物給付規定表，僅於以降 TG 為目的處方時供參考。');
    R.nhi.push(it);
  }

  /* ---- 提示 ---- */
  if(cls.unknowns.length && (cls.tier==='M'||cls.tier==='L'||cls.tier==='Z')) R.alerts.push({k:'warn', t:'尚有自動判定項目未輸入（'+cls.unknowns.join('、')+'），心血管風險因子數可能低估，分級可能偏低。'});
  if(ldl!==null && ldl>=190) R.alerts.push({k:'info', t:'LDL-C ≧190 mg/dL（嚴重高膽固醇血症）：已歸為高風險；應依台灣家族性高膽固醇血症診斷標準進行 FH 篩檢，可考慮基因檢測確認。'});
  else if(c.xanthoma || c.fhx) R.alerts.push({k:'info', t:(c.xanthoma?'肌腱黃色瘤':'早發性冠心病家族史')+'：建議依台灣 FH 診斷標準評估家族性高膽固醇血症之可能。'});
  if(c.hofh && s.pcsk9Drug==='alirocumab') R.alerts.push({k:'warn', t:'同合子家族性高膽固醇血症（HoFH）之 PCSK9 給付途徑僅列於 evolocumab（2.6.4.1 第 2 點）；alirocumab 限用於發生重大心血管事件之病人。'});
  if(cls.tier==='Z') R.alerts.push({k:'info', t:'共識僅定義低（1 項）與中（≧2 項）風險；「0 項心血管風險因子」之起始值／目標值（LDL-C ≧160／<160 mg/dL）引自健保表一。'});
  if(nonhdl!==null && nonhdlT && atGoal===true) R.alerts.push({k: nonhdl<nonhdlT?'ok':'warn', t:'LDL-C 已達標，次要標的 non-HDL-C '+nonhdl+' mg/dL'+(nonhdl<nonhdlT?' 亦達標（<'+nonhdlT+'）':' 未達 <'+nonhdlT+'（尤其合併高 TG、糖尿病或肥胖者需進一步評估）')+'。'});
  return R;
}

root.LipidEngine = {classify, classifyT2, evalT2, assess, TIERS, T2ROWS, STATIN_DOSES, STATIN_LISTS, INTENSITY_NAME, TABLE2_ONLY, T2_INFO, t2Info, isT2Product, EZE_LISTED, FDC_LISTED, intensityOf, isNhiHighIntensity, num, doseMg};
if(typeof module!=='undefined' && module.exports){ module.exports=root.LipidEngine; }
})(typeof window!=='undefined' ? window : globalThis);
</script>

<script>
/* ============================================================
   UI：狀態綁定、即時渲染、LDL-C 目標尺、品項查詢、摘要複製
   ============================================================ */
(function(){
'use strict';
const E=window.LipidEngine;
const $=(s,r)=>(r||document).querySelector(s);
const $$=(s,r)=>Array.from((r||document).querySelectorAll(s));
const esc=s=>String(s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));

const state={sex:null, age:'', ldl:'', tc:'', hdl:'', tg:'', preLdl:'', status:'naive', pcsk9Drug:null, statinDrug:'', statinDose:'', statinDur:'', ezeDur:'lt3m', ezeDur2:'lt3m', checks:{}, product:null};
const IMPLIES={mi:['acs'], mi1y:['mi','acs'], mi2:['mi','acs'], padRevasc:['pad']};
const CHILDREN={acs:['mi','mi1y','mi2'], mi:['mi1y','mi2'], pad:['padRevasc'], carotid:['carotidSym'], hofh:['hofh6m','hofhCriteria']};
const AUTO_ROWS={ms_bp:()=>!!state.checks.htn, ms_fpg:()=>!!state.checks.dm, ms_tg:()=>{const t=E.num(state.tg); return t!==null&&t>=150;}};
const TIER_COLOR={EXT:'var(--r-ext)',VH:'var(--r-vh)',H:'var(--r-h)',M:'var(--r-m)',L:'var(--r-l)',Z:'var(--r-z)'};
const ST_PILL={ok:['ok','符合'], no:['no','不符合'], cond:['warn','有條件／尚未符合'], na:['na','不適用／無需求']};

function setCheck(key,val){ state.checks[key]=!!val; if(val)(IMPLIES[key]||[]).forEach(k=>state.checks[k]=true); else (CHILDREN[key]||[]).forEach(k=>state.checks[k]=false); }

/* ---------- Tabs ---------- */
function showTab(name){
  $$('.tab').forEach(t=>t.setAttribute('aria-selected', t.dataset.tab===name?'true':'false'));
  $$('.panel').forEach(p=>p.classList.toggle('active', p.id==='panel-'+name));
  window.scrollTo({top:0,behavior:'smooth'});
}
$$('.tab').forEach(t=>t.addEventListener('click',()=>showTab(t.dataset.tab)));
document.addEventListener('click',e=>{ const a=e.target.closest('[data-goto]'); if(a){ e.preventDefault(); showTab(a.dataset.goto); } });

/* ---------- Inputs ---------- */
$$('[data-seg]').forEach(b=>b.addEventListener('click',()=>{
  const k=b.dataset.seg, v=b.dataset.val;
  state[k] = (k!=='status' && state[k]===v) ? null : v;
  if(k==='status') applyProductToStatin(false);
  syncSeg(k); syncBlocks(); syncChecks(); update();
}));
function syncSeg(k){ $$('[data-seg="'+k+'"]').forEach(b=>b.setAttribute('aria-pressed', state[k]===b.dataset.val?'true':'false')); }
$$('input[data-num]').forEach(i=>i.addEventListener('input',()=>{ state[i.dataset.num]=i.value; update(); }));
$$('select[data-sel]').forEach(sel=>sel.addEventListener('change',()=>{ state[sel.dataset.sel]=sel.value; if(sel.dataset.sel==='statinDrug'){ state.statinDose=''; populateDose(); if(state.product && state.product.generic && state.product.generic!==sel.value){ state.product=null; renderProdSel(); toast('成分與所選品項不一致，已清除品項選取'); } } update(); }));
$$('input[type=checkbox][data-key]').forEach(cb=>cb.addEventListener('change',()=>{ setCheck(cb.dataset.key, cb.checked); syncChecks(); update(); }));
function syncChecks(){
  $$('input[type=checkbox][data-key]').forEach(cb=>{ cb.checked=!!state.checks[cb.dataset.key]; });
  $$('[data-show-if]').forEach(el=>el.classList.toggle('hide', !state.checks[el.dataset.showIf]));
  $$('[data-show-sex]').forEach(el=>el.classList.toggle('hide', state.sex!==el.dataset.showSex));
}
function syncBlocks(){ $$('.tx-block[data-status]').forEach(el=>el.classList.toggle('hide', !el.dataset.status.split(' ').includes(state.status))); }
function populateDose(){
  const sel=$('#statinDose'); const arr=E.STATIN_DOSES[state.statinDrug];
  sel.innerHTML='';
  if(!arr){ sel.innerHTML='<option value="">— 先選成分 —</option>'; return; }
  sel.innerHTML='<option value="">— 選擇劑量 —</option>'+arr.map(x=>'<option value="'+esc(x[0])+'">'+esc(x[0])+(x[1]?'（'+({hi:'高',mod:'中',lo:'低'}[x[1]])+'強度）':'')+'</option>').join('');
  sel.value=state.statinDose||'';
}
function syncAutoRows(){
  Object.keys(AUTO_ROWS).forEach(k=>{
    const cb=$('input[data-key="'+k+'"]'); const row=cb.closest('.chk'); const auto=AUTO_ROWS[k]();
    row.classList.toggle('auto',auto); cb.disabled=auto; if(auto) cb.checked=true; else cb.checked=!!state.checks[k];
    let tag=row.querySelector('.tag'); if(auto){ if(!tag){ tag=document.createElement('span'); tag.className='tag'; tag.textContent='自動符合'; row.querySelector('.txt').appendChild(tag);} } else if(tag) tag.remove();
  });
}
function statusPill(el,txt,cls){ el.textContent=txt; el.className='rf-status '+cls; }

/* ---------- Ruler (signature) ---------- */
function ruler(R){
  const ldl=R.ldl, T=R.target;
  const W=640,H=118,x0=18,x1=W-18;
  const maxV=Math.max(220, ldl?Math.ceil(ldl*1.12/10)*10:0, T+40);
  const X=v=>x0+(x1-x0)*Math.min(v,maxV)/maxV;
  const tiers=[['EXT',55],['VH',70],['H',100],['M',115],['L',130],['Z',160]];
  const yBase=64;
  let s='<div class="ruler-wrap" data-mx="'+((ldl!==null&&ldl>0)?X(ldl):'')+'" data-w="'+W+'"><svg class="ruler" viewBox="0 0 '+W+' '+H+'" role="img" aria-label="LDL-C 目標尺">';
  s+='<rect x="'+x0+'" y="'+(yBase-9)+'" width="'+(X(T)-x0)+'" height="18" rx="3" fill="#E4F4EA"/>';
  s+='<rect x="'+X(T)+'" y="'+(yBase-9)+'" width="'+(x1-X(T))+'" height="18" rx="3" fill="#F3F5F7"/>';
  s+='<line x1="'+x0+'" y1="'+yBase+'" x2="'+x1+'" y2="'+yBase+'" stroke="#9AA5B1" stroke-width="1.5"/>';
  for(let v=0; v<=maxV; v+=20){ s+='<line x1="'+X(v)+'" y1="'+(yBase+9)+'" x2="'+X(v)+'" y2="'+(yBase+13)+'" stroke="#B9C2CC" stroke-width="1"/>'; if(v%40===0) s+='<text x="'+X(v)+'" y="'+(yBase+25)+'" text-anchor="middle" fill="#8A95A1">'+v+'</text>'; }
  tiers.forEach(([k,v])=>{ const act=k===R.tier.key; const col=TIER_COLOR[k];
    s+='<line x1="'+X(v)+'" y1="'+(yBase-(act?16:11))+'" x2="'+X(v)+'" y2="'+(yBase+9)+'" stroke="'+col+'" stroke-width="'+(act?3:1.5)+'"'+(act?'':' stroke-dasharray="3 2"')+'/>';
    s+='<text x="'+X(v)+'" y="'+(yBase-(act?21:15))+'" text-anchor="middle" class="'+(act?'active-lbl':'')+'" fill="'+col+'" style="font-weight:'+(act?'800':'500')+'">'+v+'</text>';
    if(act){ s+='<text x="'+X(v)+'" y="'+(yBase+38)+'" text-anchor="middle" class="tier-lbl active-lbl" fill="'+col+'">'+esc(R.tier.short)+' 目標 &lt;'+v+'</text>'; }
  });
  if(ldl!==null && ldl>0){
    const mx=X(ldl);
    // predicted bands
    const bands=[['hi', ldl*0.37, ldl*0.50, '#9E1B2A'],['mod', ldl*0.51, ldl*0.70, '#1F4FA3'],['combo', ldl*0.25, ldl*0.375, '#0B5563']];
    const by={hi:yBase+46, mod:yBase+46, combo:yBase+46};
    s+='<rect x="'+X(bands[1][1])+'" y="'+(yBase+42)+'" width="'+(X(bands[1][2])-X(bands[1][1]))+'" height="7" rx="2" fill="#1F4FA3" opacity=".55"/>';
    s+='<rect x="'+X(bands[0][1])+'" y="'+(yBase+42)+'" width="'+(X(bands[0][2])-X(bands[0][1]))+'" height="7" rx="2" fill="#9E1B2A" opacity=".55"/>';
    s+='<rect x="'+X(bands[2][1])+'" y="'+(yBase+42)+'" width="'+(X(bands[2][2])-X(bands[2][1]))+'" height="7" rx="2" fill="#0B5563" opacity=".45"/>';
    // marker
    s+='<g class="marker" transform="translate('+mx+',0)"><polygon points="0,'+(yBase-2)+' -7,'+(yBase-14)+' 7,'+(yBase-14)+'" fill="#1A2330"/><line x1="0" y1="'+(yBase-14)+'" x2="0" y2="16" stroke="#1A2330" stroke-width="1.5"/>';
    s+='<rect x="-34" y="2" width="68" height="16" rx="3" fill="#1A2330"/><text x="0" y="14" text-anchor="middle" fill="#fff" style="font-weight:700">LDL '+ldl+'</text></g>';
    if(R.atGoal===false){ s+='<text x="'+Math.min(mx+8,x1-90)+'" y="'+(yBase-30)+'" fill="#B3261E" style="font-weight:700">需降 '+Math.max(1,Math.round(R.needPct))+'% → &lt;'+T+'</text>'; }
    else { s+='<text x="'+Math.min(mx+8,x1-40)+'" y="'+(yBase-30)+'" fill="#1E7A4C" style="font-weight:700">已達標</text>'; }
  }
  s+='</svg></div>';
  const legend='<div class="ruler-legend"><span><i style="background:#E4F4EA;border:1px solid #BFE3CC"></i>達標區（&lt;'+T+'）</span>'+(ldl?'<span><i style="background:#1F4FA3;opacity:.55"></i>中強度 statin 預期落點（降 30–49%）</span><span><i style="background:#9E1B2A;opacity:.55"></i>高強度 statin（降 ≧50%，示意至 63%）</span><span><i style="background:#0B5563;opacity:.45"></i>高強度＋ezetimibe（估 ≧62%）</span>':'')+'</div>';
  return s+legend;
}

/* ---------- Render ---------- */
function isPristine(){ return !state.ldl && !state.age && !state.sex && !state.tc && !state.hdl && !state.tg && !Object.values(state.checks).some(Boolean) && state.status==='naive'; }
function renderDrugs(R){
  let h='';
  const cur = (state.status!=='naive' && state.status!=='intolerant' && state.statinDrug) ? ('目前：'+esc(cap(state.statinDrug))+(state.statinDose?' '+esc(state.statinDose):'')+(R.intensity?' → '+E.INTENSITY_NAME[R.intensity]:'（劑量未選）')) : '';
  if(R.drugs.length){
    h+='<div class="sec-title"><span class="n">Statin</span>建議之 statin 學名與每日劑量（2026 ACC/AHA 強度分類）</div>';
    if(cur) h+='<div class="inline-note" style="margin-left:0">'+cur+'</div>';
    h+='<ul class="drug-list">';
    R.drugs.forEach((k,i)=>{ h+='<li class="'+k+'"><b>'+esc(E.INTENSITY_NAME[k])+(i===0?'（優先）':'')+'</b>：'+esc(E.STATIN_LISTS[k].join('；'))+'</li>'; });
    h+='</ul>';
  } else if(cur){ h+='<div class="inline-note" style="margin-left:0;margin-top:8px">'+cur+'</div>'; }
  if(R.nonstatin.length){
    h+='<div class="sec-title"><span class="n">Non-statin</span>Non-statin 選項（依共識；括號為 2026 ACC/AHA 之預期 LDL-C 降幅）</div><ul class="drug-list">';
    R.nonstatin.forEach(x=>{ h+='<li class="ns">'+esc(x)+'</li>'; });
    h+='</ul>';
  }
  return h;
}
function cap(s){ return s? s.charAt(0).toUpperCase()+s.slice(1) : s; }
function renderResult(R){
  const box=$('#result');
  if(isPristine()){ box.innerHTML='<div class="card res-empty">請由左側（手機為上方）輸入病患資料，判定結果會即時顯示於此。<br><small>建議先完成：性別、年齡、LDL-C，再勾選病史與治療狀態。</small></div>'; return; }
  const t=R.tier, cls=R.cls;
  let h='';
  // Risk banner
  h+='<div class="risk t-'+t.key+'"><div class="eyebrow">ASCVD 風險分級（2025 共識／健保表一）</div><div class="name">'+esc(t.name)+'</div><div class="why"><b>依據：</b><ul>'+cls.reasons.map(r=>'<li>'+esc(r)+'</li>').join('')+'</ul>';
  if(t.group==='lowmod'){ h+='<div style="margin-top:6px;display:flex;flex-wrap:wrap;gap:4px">'+cls.rf.map(f=>'<span class="pill '+(f.met?'ok':(f.unknown?'warn':'na'))+'">'+esc(f.name)+(f.met?' ✓':(f.unknown?' ?':' –'))+'</span>').join('')+'</div>'; }
  h+='</div></div>';
  // Readouts
  const gcls = R.atGoal===null?'':(R.atGoal?'goal-ok':'goal-no');
  h+='<div class="card">';
  h+='<div class="readouts"><div class="ro"><div class="k">LDL-C 目標（主要）</div><div class="v">&lt;'+R.target+'<small> mg/dL</small></div></div>';
  h+='<div class="ro '+gcls+'"><div class="k">目前 LDL-C</div><div class="v">'+(R.ldl===null?'—':R.ldl)+'<small> mg/dL</small></div><div style="font-size:12px;color:var(--muted)">'+(R.atGoal===null?'請輸入':(R.atGoal?'已達標':'未達標，需降約 '+Math.max(1,Math.round(R.needPct))+'%'))+'</div></div>';
  h+='<div class="ro"><div class="k">non-HDL-C（次要）</div><div class="v">'+(R.nonhdl===null?'—':R.nonhdl)+'<small> mg/dL</small></div><div style="font-size:12px;color:var(--muted)">'+(R.nonhdlT?'目標 &lt;'+R.nonhdlT:'表一未訂')+(R.nonhdl===null?'（需 TC 與 HDL-C）':'')+'</div></div></div>';
  h+=ruler(R);
  h+='</div>';
  // Decision
  const D=R.decision;
  h+='<div class="card"><div class="sec-title"><span class="n">1</span>用藥決策（2025 台灣血脂管理臨床路徑共識）</div>';
  h+='<div class="dec '+D.kind+'"><div class="headline">'+esc(D.headline)+'</div><ul>'+D.points.map(p=>'<li>'+esc(p)+'</li>').join('')+'</ul></div>';
  h+=renderDrugs(R);
  h+='</div>';
  // NHI
  h+='<div class="card"><div class="sec-title"><span class="n">2</span>健保給付判定（藥品給付規定 2.6.1–2.6.4）</div>';
  if(R.useT2){ h+='<div class="notice no" style="margin:6px 0 8px"><b>依表二判定：</b>所選品項「'+esc(R.product.name)+'」'+(R.product.code?'（'+esc(R.product.code)+'）':'')+'列於 2.6.1「不適用表一」清單，statin 給付改依表二（原給付規定；對象＝'+esc(R.t2.def.name)+'）判定。</div>'; }
  else if(R.product && R.product.t2===false){ h+='<div class="notice ok" style="margin:6px 0 8px">品項「'+esc(R.product.name)+'」未列於「不適用表一」清單，statin 給付依表一判定。</div>'; }
  R.nhi.forEach(n=>{ const p=ST_PILL[n.st]; h+='<div class="nhi-item'+(n.table==='T2'?' t2':'')+'"><div class="top"><span class="nm">'+esc(n.name)+'</span><span class="pill '+p[0]+'">'+p[1]+'</span></div><div class="det"><ul>'+n.det.map(d=>'<li>'+esc(d)+'</li>').join('')+'</ul>';
    if(n.checklist&&n.checklist.length){ h+='<ul class="chk-list">'+n.checklist.map(c=>'<li><span class="m '+c.m+'">'+({y:'✓',n:'✕',q:'?'}[c.m])+'</span><span>'+esc(c.t)+(c.note?' <span class="muted">（'+esc(c.note)+'）</span>':'')+'</span></li>').join('')+'</ul>'; }
    h+='</div></div>'; });
  h+='<div class="inline-note" style="margin-left:0">修訂後 2.6.1–2.6.3 自 115/9/1 生效；PCSK9 2.6.4 為 114/9/1 修訂版。給付以健保署公告與審查為準。</div></div>';
  // Follow-up + alerts
  h+='<div class="card"><div class="sec-title"><span class="n">3</span>追蹤與監測</div><ul class="fu-list">'+R.followup.map(f=>'<li>'+esc(f)+'</li>').join('')+'</ul>';
  if(R.alerts.length){ h+='<div class="sec-title" style="margin-top:12px"><span class="n">4</span>提示</div>'+R.alerts.map(a=>'<div class="notice '+a.k+'" style="margin:6px 0">'+esc(a.t)+'</div>').join(''); }
  h+='<div class="summary-actions no-print"><button type="button" class="btn primary" id="btnCopy">複製摘要（純文字）</button><button type="button" class="btn" id="btnPrint">列印</button><button type="button" class="btn" data-goto="statin">查看 statin 強度表</button></div></div>';
  box.innerHTML=h;
  // 窄螢幕：目標尺可橫向捲動時，自動捲至病人 LDL-C 標記處
  const rw=box.querySelector('.ruler-wrap');
  if(rw && rw.dataset.mx && rw.scrollWidth>rw.clientWidth+4){ const svg=rw.querySelector('svg'); const scale=svg.clientWidth/Number(rw.dataset.w||640); rw.scrollLeft=Math.max(0, Number(rw.dataset.mx)*scale - rw.clientWidth*0.6); }
  $('#btnCopy').addEventListener('click',()=>copyText(summaryText(R)));
  $('#btnPrint').addEventListener('click',()=>window.print());
}
function summaryText(R){
  const L=[]; const d=new Date();
  L.push('【血脂治療決策摘要】'+d.getFullYear()+'/'+(d.getMonth()+1)+'/'+d.getDate()+'（依 2025 台灣血脂管理臨床路徑共識；健保給付規定 115/9/1 修訂版；statin 強度依 2026 ACC/AHA）');
  L.push('病人：'+(state.sex==='M'?'男':state.sex==='F'?'女':'性別未填')+'，'+(state.age?state.age+' 歲':'年齡未填')+'；LDL-C '+(R.ldl===null?'—':R.ldl)+' mg/dL'+(state.tc?'，TC '+state.tc:'')+(state.hdl?'，HDL-C '+state.hdl:'')+(state.tg?'，TG '+state.tg:'')+(R.nonhdl!==null?'，non-HDL-C '+R.nonhdl:''));
  L.push('風險分級：'+R.tier.name+'（依據：'+R.cls.reasons.join('；')+'）');
  L.push('目標：LDL-C <'+R.target+' mg/dL'+(R.nonhdlT?'；non-HDL-C <'+R.nonhdlT+' mg/dL':'')+'；目前 '+(R.atGoal===null?'未輸入':(R.atGoal?'已達標':'未達標，需降約 '+Math.max(1,Math.round(R.needPct))+'%')));
  L.push('治療狀態：'+({naive:'尚未使用降血脂藥物',statin:'statin 單一治療中',statin_eze:'statin＋ezetimibe 併用中',intolerant:'statin 不耐受／禁忌症',pcsk9:'已使用 PCSK9 抑制劑'}[state.status])+(state.statinDrug&&state.status!=='naive'&&state.status!=='intolerant'?'（'+cap(state.statinDrug)+' '+(state.statinDose||'劑量未選')+(R.intensity?'，'+E.INTENSITY_NAME[R.intensity]:'')+'）':''));
  if(state.product) L.push('Statin 品項：'+state.product.name+(state.product.code?'（'+state.product.code+'）':'')+(state.product.t2?' → 不適用表一，statin 給付依表二（原給付規定）判定；表二對象：'+R.t2.def.name:' → 未列於不適用表一清單，依表一判定'));
  L.push('用藥決策：'+R.decision.headline); R.decision.points.forEach(p=>L.push('  - '+p));
  if(R.drugs.length){ L.push('建議 statin：'); R.drugs.forEach(k=>L.push('  - '+E.INTENSITY_NAME[k]+'：'+E.STATIN_LISTS[k].join('；'))); }
  if(R.nonstatin.length){ L.push('Non-statin 選項：'+R.nonstatin.join('；')); }
  L.push('健保給付判定：'); R.nhi.forEach(n=>{ L.push('  - '+n.name+'：'+ST_PILL[n.st][1]+'。'+n.det.join(' ')); (n.checklist||[]).forEach(c=>L.push('      ['+({y:'✓',n:'✕',q:'?'}[c.m])+'] '+c.t+(c.note?'（'+c.note+'）':''))); });
  L.push('追蹤：'+R.followup.join('；'));
  R.alerts.forEach(a=>L.push('提示：'+a.t));
  L.push('※ 臨床決策輔助，最終以醫師判斷與健保署公告為準。');
  return L.join('\n');
}
function copyText(txt){
  const done=()=>toast('已複製摘要');
  if(navigator.clipboard && navigator.clipboard.writeText){ navigator.clipboard.writeText(txt).then(done, ()=>fallbackCopy(txt,done)); } else fallbackCopy(txt,done);
}
function fallbackCopy(txt,done){ const ta=document.createElement('textarea'); ta.value=txt; ta.style.position='fixed'; ta.style.opacity='0'; document.body.appendChild(ta); ta.select(); try{ document.execCommand('copy'); done(); }catch(e){ toast('複製失敗，請手動選取'); } document.body.removeChild(ta); }
let toastTimer=null;
function toast(msg){ const t=$('#toast'); t.textContent=msg; t.classList.add('show'); clearTimeout(toastTimer); toastTimer=setTimeout(()=>t.classList.remove('show'),1800); }

function renderMbar(R){
  const r=$('#mbRisk'), t=$('#mbTarget');
  if(isPristine()){ r.textContent='請輸入資料'; r.style.color=''; t.textContent=''; return; }
  r.textContent=R.tier.name; r.style.color=TIER_COLOR[R.tier.key];
  t.textContent='LDL-C 目標 <'+R.target+(R.ldl!==null?'｜目前 '+R.ldl+(R.atGoal?'（達標）':'（未達標）'):'');
}
$('#mbBtn').addEventListener('click',()=>{ $('#result').scrollIntoView({behavior:'smooth',block:'start'}); });

/* ---------- Auto-status rows in the form ---------- */
function syncFormStatus(){
  const ldl=E.num(state.ldl), age=E.num(state.age), hdl=E.num(state.hdl), tc=E.num(state.tc), sex=state.sex;
  // LDL 190
  const s190=$('#ldl190-status'); if(ldl===null) statusPill(s190,'未輸入','unk'); else statusPill(s190, ldl>=190?'符合（高風險）':'不符合', ldl>=190?'on':'');
  $('#ldl190-note').textContent = ldl===null?'請於步驟 1 輸入 LDL-C':('目前 LDL-C '+ldl+' mg/dL');
  // age RF
  const sa=$('#rf-age-status'); if(!sex||age===null) statusPill(sa,'未輸入性別／年齡','unk'); else { const m = sex==='M'?age>=45:age>=55; statusPill(sa, m?'符合':'不符合', m?'on':''); }
  // hdl RF
  const sh=$('#rf-hdl-status'), sh2=$('#ms-hdl-status'); if(!sex||hdl===null){ statusPill(sh,'未輸入性別／HDL-C','unk'); statusPill(sh2,'未輸入','unk'); } else { const m= sex==='M'?hdl<40:hdl<50; statusPill(sh, m?'符合':'不符合', m?'on':''); statusPill(sh2, m?'符合':'不符合', m?'on':''); }
  // MetS count
  const cls=E.classify(state); statusPill($('#ms-status'), cls.msCount+'／5 項'+(cls.metS?'（符合代謝性症候群）':''), cls.metS?'on':'');
  // non-HDL note
  const nn=$('#nonhdl-note'); if(tc!==null&&hdl!==null) nn.textContent='non-HDL-C = TC − HDL-C = '+(tc-hdl)+' mg/dL（LDL-C 達標後之次要標的）'; else nn.textContent='輸入 TC 與 HDL-C 可自動計算 non-HDL-C。';
  // intensity note
  const inote=$('#intensity-note');
  if(state.statinDrug && state.statinDose){ const it=E.intensityOf(state.statinDrug,state.statinDose); inote.innerHTML = it ? ('依 2026 ACC/AHA：<b>'+esc(E.INTENSITY_NAME[it])+'</b>'+(E.isNhiHighIntensity(state.statinDrug,state.statinDose)?'；符合健保 PCSK9 規定之「高強度 statin」舉例（rosuvastatin ≧20／atorvastatin ≧40 mg）':'')) : '此劑量未列於強度分類表'; }
  else inote.textContent = state.statinDrug==='other' ? '未知成分／劑量：無法自動判定強度，請自行對照 statin 強度表。' : '選擇成分與劑量後自動顯示強度分類。';
}

function update(){ syncAutoRows(); syncFormStatus(); const R=E.assess(state); renderResult(R); renderMbar(R); }

/* ---------- Product search ---------- */
function searchProducts(q){
  q=q.trim().toLowerCase(); if(q.length<2) return [];
  const hits=[];
  E.TABLE2_ONLY.forEach(([ing,code,name])=>{ if(name.toLowerCase().includes(q)||code.toLowerCase().includes(q)||ing.toLowerCase().includes(q)) hits.push({cat:'t2',ing,code,name}); });
  E.EZE_LISTED.forEach(([code,name])=>{ if(name.toLowerCase().includes(q)||code.toLowerCase().includes(q)||'ezetimibe'.includes(q)) hits.push({cat:'eze',code,name}); });
  E.FDC_LISTED.forEach(([code,name])=>{ if(name.toLowerCase().includes(q)||code.toLowerCase().includes(q)) hits.push({cat:'fdc',code,name}); });
  return hits;
}
const CAT_PILL={t2:['no','不適用表一（僅適用表二）'], eze:['warn','Ezetimibe 列表品項：需 statin 單一治療 3 個月'], fdc:['warn','複方列表品項：需 statin 單一治療 3 個月']};
const STATIN_STATUSES=['statin','statin_eze','pcsk9'];
// 品項選取：列表品項 → 依表二；並於治療中狀態帶入成分與劑量
function selectProduct(x){
  const info=E.t2Info(x.code);
  state.product={code:x.code, name:x.name, ing:x.ing||'', t2:true, generic:info?info[0]:'', dose:info?info[1]:''};
  applyProductToStatin(true);
  $('#prodSearch').value=''; $('#prodRes').innerHTML='';
  renderProdSel(); update();
}
function selectT1Product(name){ state.product={code:'', name:name, ing:'', t2:false, generic:'', dose:''}; $('#prodSearch').value=''; $('#prodRes').innerHTML=''; renderProdSel(); update(); }
function clearProduct(){ state.product=null; renderProdSel(); update(); }
function applyProductToStatin(notify){
  const P=state.product; if(!P || !P.t2 || !P.generic) return;
  if(!STATIN_STATUSES.includes(state.status)) return;
  const changed = state.statinDrug!==P.generic || state.statinDose!==P.dose;
  state.statinDrug=P.generic; state.statinDose=P.dose;
  $('#statinDrug').value=P.generic; populateDose(); $('#statinDose').value=P.dose;
  if(notify && changed) toast('已依品項帶入：'+cap(P.generic)+' '+P.dose);
}
function renderProdSel(){
  const el=$('#prodSel'); const P=state.product;
  if(!P){ el.classList.add('hide'); el.innerHTML=''; el.className='prod-sel hide'; return; }
  el.className='prod-sel '+(P.t2?'t2':'t1');
  el.innerHTML = '<span class="pill '+(P.t2?'no':'ok')+'">'+(P.t2?'不適用表一 → 依表二判定':'未列於清單 → 適用表一')+'</span><span class="nm">'+esc(P.name)+'</span>'+(P.code?'<code>'+esc(P.code)+'</code>':'')+(P.generic?'<span class="muted">'+esc(cap(P.generic))+' '+esc(P.dose)+'</span>':'')+'<button type="button" class="btn small" id="prodClear" style="margin-left:auto">清除品項</button>';
  $('#prodClear').addEventListener('click',clearProduct);
}
$('#prodSearch').addEventListener('input',e=>{
  const q=e.target.value; const box=$('#prodRes');
  if(q.trim().length<2){ box.innerHTML=''; return; }
  const hits=searchProducts(q);
  if(!hits.length){ box.innerHTML='<div class="hit"><span class="pill ok">未列於清單</span><span>「'+esc(q)+'」未列於「不適用表一」清單，亦非 ezetimibe／複方之 3 個月列表品項：statin 品項適用表一；ezetimibe／複方適用 6–8 週規定。請確認拼寫或改以健保代碼查詢。</span><button type="button" class="btn small" data-t1name="'+esc(q.trim())+'">記錄為適用表一之品項</button></div>'; return; }
  box.innerHTML=hits.slice(0,40).map(x=>'<div class="hit"><span class="pill '+CAT_PILL[x.cat][0]+'">'+CAT_PILL[x.cat][1]+'</span><span>'+esc(x.name)+(x.ing?' <span class="muted">（'+esc(x.ing)+'）</span>':'')+'</span><code>'+esc(x.code)+'</code>'+(x.cat==='t2'?'<button type="button" class="btn small primary" data-pick="'+esc(x.code)+'">選用此品項（依表二）</button>':'')+'</div>').join('')+(hits.length>40?'<div class="muted" style="font-size:12px">僅顯示前 40 筆，請縮小關鍵字。</div>':'');
});
$('#prodRes').addEventListener('click',e=>{
  const b=e.target.closest('button[data-pick]'); if(b){ const code=b.dataset.pick; const row=E.TABLE2_ONLY.find(r=>r[1]===code); if(row) selectProduct({ing:row[0],code:row[1],name:row[2]}); return; }
  const b1=e.target.closest('button[data-t1name]'); if(b1){ selectT1Product(b1.dataset.t1name); }
});

/* ---------- Reference lists ---------- */
function renderT2(filter){
  filter=(filter||'').trim().toLowerCase();
  const groups={}; E.TABLE2_ONLY.forEach(([ing,code,name])=>{ if(filter && !(name.toLowerCase().includes(filter)||code.toLowerCase().includes(filter)||ing.toLowerCase().includes(filter))) return; (groups[ing]=groups[ing]||[]).push([code,name]); });
  const order=['simvastatin','lovastatin','pravastatin','fluvastatin','atorvastatin','rosuvastatin','pitavastatin','pravastatin 及 fenofibrate 複方','atorvastatin 及 amlodipine 複方'];
  const keys=Object.keys(groups).sort((a,b)=>order.indexOf(a)-order.indexOf(b));
  const el=$('#t2List');
  if(!keys.length){ el.innerHTML='<div class="muted">無符合品項。</div>'; return; }
  el.innerHTML=keys.map(k=>'<details class="acc"'+(filter?' open':'')+'><summary>'+esc(k)+'（'+groups[k].length+' 項）</summary><div class="body"><div class="prod-list two">'+groups[k].map(([c,n])=>'<div><code>'+esc(c)+'</code>　'+esc(n)+'</div>').join('')+'</div></div></details>').join('');
}
$('#t2Search').addEventListener('input',e=>renderT2(e.target.value));
$('#t2count').textContent=E.TABLE2_ONLY.length;
$('#ezeList').innerHTML=E.EZE_LISTED.map(([c,n])=>'<div><code>'+esc(c)+'</code>　'+esc(n)+'</div>').join('');
$('#fdcList').innerHTML=E.FDC_LISTED.map(([c,n])=>'<div><code>'+esc(c)+'</code>　'+esc(n)+'</div>').join('');
renderT2('');

/* ---------- Reset ---------- */
$('#btnReset').addEventListener('click',()=>{
  Object.assign(state,{sex:null, age:'', ldl:'', tc:'', hdl:'', tg:'', preLdl:'', status:'naive', pcsk9Drug:null, statinDrug:'', statinDose:'', statinDur:'', ezeDur:'lt3m', ezeDur2:'lt3m', checks:{}, product:null});
  $$('input[data-num]').forEach(i=>i.value='');
  $$('select[data-sel]').forEach(s=>{ s.value=state[s.dataset.sel]||''; });
  populateDose(); ['sex','status','pcsk9Drug'].forEach(syncSeg); syncChecks(); syncBlocks(); $('#prodSearch').value=''; $('#prodRes').innerHTML=''; renderProdSel();
  update(); toast('已清除');
});

/* ---------- Init ---------- */
populateDose(); syncSeg('status'); syncBlocks(); syncChecks(); renderProdSel(); update();
})();
</script>
</body>
</html>
