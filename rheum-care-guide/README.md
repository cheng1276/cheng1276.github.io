# 風濕免疫生活照護圖解

網址：https://cheng1276.github.io/rheum-care-guide/

給病友與家屬的生活照護衛教網站。內容涵蓋痛風、慢性蕁麻疹、類風濕性關節炎、僵直性脊椎炎、紅斑性狼瘡、乾燥症，以及六種疾病都適用的共通照護。每一則建議下方都標出它來自哪一份臨床指引或研究，以及建議強度。

內文中有虛線底線的專有名詞（例如「有氧運動」「UVA」「類固醇」），點一下就會跳出白話解釋；全部 125 個名詞也收在「名詞小辭典」分頁，可以搜尋、依類別瀏覽，並看到每個詞出現在哪些頁面。每個解釋都附上 PubMed 收錄的指引或文獻出處。

## 內容狀態

- 審閱醫師：台南市立醫院 免疫風濕科 鄭傑夫醫師；審閱完成：2026 年 10 月 8 日。
- 試用版，歡迎回饋。
- 最後更新：2026 年 10 月 9 日（經審閱醫師同意修改三頁：類風濕性關節炎迷思不再說運動不會讓 X 光變差，並加上大關節嚴重損傷者的提醒；紅斑性狼瘡紫外線提醒先說明平常就要防曬；乾燥症拿掉「開冷氣」，並更正一筆文獻年份）。

## 資料來源與整理方式

- 文獻檢索：PubMed，以及各學會指引的原文。
- 優先採用最新的臨床指引（ACR、EULAR、ASAS、BSR、NICE、WHO、國際蕁麻疹指引、台灣共識）；指引沒寫到的細節，才採用系統性回顧或重要研究。
- 每一句網站文字都對應到原文引述。另一套獨立查核流程逐句比對了 224 則網站文字與約 348 則引述，未發現事實錯誤；不夠精確或遺漏注意事項之處已修正。
- 名詞解釋：每個詞先由一組 AI 依撰寫規則查找 PubMed 收錄的定義並逐字引述，再由另一組 AI 獨立核對全部引述（PMC 全文或 PubMed 摘要）、書目資料與白話解釋是否超出原文；查核結果與修改紀錄都在 `evidence/glossary/`。
- 內容由 AI（Claude）協助檢索、整理與查核。每篇文獻的 PubMed 與 DOI 連結列在網站各頁的「本頁參考文獻」與每個名詞的「出處」。

## 檔案說明

| 路徑 | 內容 |
|---|---|
| `index.html` | 網站本體，單一檔案，可直接開啟 |
| `og.png` | 分享連結時顯示的預覽圖 |
| `src/content/*.json` | 各疾病的網站文字，以及每一句所依據的原文引述、出處與建議強度 |
| `src/glossary/glossary.json` | 名詞解釋（白話解釋、例子、補充、出處與原文引述），由 `evidence/glossary/merge.py` 產生 |
| `src/template.html` | 版面、插圖與互動程式（含點選解釋與名詞小辭典） |
| `src/build.py` | 由內容產生 `index.html`：`python3 src/build.py` |
| `evidence/research/` | 各疾病的文獻證據檔（含原文引述、建議強度與無法查證的項目） |
| `evidence/drafting/` | 撰寫規則 |
| `evidence/verification/` | 獨立查核的規則與報告 |
| `evidence/review-tables/` | 網站文字與原文的逐句對照表 |
| `evidence/glossary/research/` | 名詞清單、各詞在網站上的語境、查證規則與各組查證結果 |
| `evidence/glossary/verification/` | 名詞解釋的獨立查核規則與七份查核報告 |
| `evidence/glossary/occurrences.md` | 每個名詞在網站上出現的句子，以及哪一次會變成可點的連結 |

## 修改內容

1. 編輯 `src/content/<疾病>.json` 裡的文字或依據。
2. 名詞解釋：修改 `evidence/glossary/research/` 的查證檔或 `evidence/glossary/postfix.py` 的修訂後，執行 `python3 evidence/glossary/merge.py`，再用 `python3 evidence/glossary/occ.py --md evidence/glossary/occurrences.md` 檢查連結位置。
3. 執行 `python3 src/build.py`，重新產生 `index.html`。
4. 提交並推送後，GitHub Pages 會在幾分鐘內更新。

連結規則：同一張卡片裡，每個名詞只有第一次出現會變成可點的連結；「指引」、出處機構縮寫等很常出現的詞，每頁只連結第一次。

## 使用前請先了解

本網站提供一般衛教資訊，不能取代醫師診療，也不提供個別的診斷或用藥建議。用藥調整請和醫師討論，不要自行停藥。緊急狀況請撥打 119 或到急診。
