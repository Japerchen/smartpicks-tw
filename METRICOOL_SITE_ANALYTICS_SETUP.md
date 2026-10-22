# SmartPicksTW 網站訪客分析串接 — Metricool

目前狀態（2026-10-23）：**尚未安裝 Metricool 網站追蹤程式碼**。以下是預備的操作步驟；追蹤資料不能事後回溯。

## 為什麼要做
目前只有 Facebook 貼文／Reels 的排程及社群指標，沒有可靠的網站訪客、來源、點擊或蝦皮結帳資料。
先完成網站訪客分析，可區分「Facebook 觸及」與「實際進入網站」。

## 使用已連接的 Metricool 品牌
1. 登入 [Metricool Connections](https://app.metricool.com/brands/connections?blogId=7545618)。
2. 在同一個 Smartpickstw 品牌找到 **Connect website**。
3. 選擇 **JavaScript tracking tag**，不要選 WordPress 或只有有限功能的 tracking pixel。
4. 複製 Metricool 給這個品牌產生的**完整追蹤碼**，傳給協助維護 SmartPicksTW GitHub Pages 的人員。
5. 把追蹤碼加入 `index.html` 和 `guides.html` 的 `</head>` 前，再推送 GitHub Pages。
6. 返回 Connections 按 **Verify connection**，用新瀏覽器視窗開啟公開網站確認。
7. 數據從安裝後開始記錄，網站即時訪問可在 Metricool 查看，完整分析通常次日可見；沒有任何歷史數據可補回。

官方步驟：https://help.metricool.com/how-to-connect-your-website-or-blog-to-metricool-ejuy1

## 建議 Facebook 導流網址
- 粉專網站按鈕：`https://japerchen.github.io/smartpicks-tw/?utm_source=facebook&utm_medium=profile&utm_campaign=page_button`
- 貼文到商品目錄：`https://japerchen.github.io/smartpicks-tw/?utm_source=facebook&utm_medium=post&utm_campaign=product_post`
- USB-C Hub Reel：`https://japerchen.github.io/smartpicks-tw/guides.html?utm_source=facebook&utm_medium=reels&utm_campaign=usb_c_hub`
- 磁吸支架 Reel：`https://japerchen.github.io/smartpicks-tw/guides.html?utm_source=facebook&utm_medium=reels&utm_campaign=phone_stand`
- 行動電源 Reel：`https://japerchen.github.io/smartpicks-tw/guides.html?utm_source=facebook&utm_medium=reels&utm_campaign=power_bank`

網站指南目前支援按已知 `utm_campaign` 自動定位到相關內容。UTM 只是在 URL 上標示來源；沒有正確部署網站追蹤工具之前，**不能憑 UTM 知道真實點擊或訪客數**。

## 分辨真正可量測的數據
| 指標 | 來源 | 現階段 |
|---|---|---|
| Facebook 粉絲 | Metricool Facebook Evolution | 可取得 |
| Facebook Reels 觀看 | Metricool Facebook Evolution | 發布並收集後可取得 |
| Website visits / URL 來源 | Metricool Website Analytics | 待安裝網站追蹤碼 |
| 點擊個別蝦皮連結的次數 | 需網站端額外事件追蹤 | 尚未建置 |
| 蝦皮訂單、分潤金額 | 蝦皮聯盟後台 | 不能由 Facebook 或網站訪客指標臆測 |

## 隱私及防護
Metricool 官方表示網站追蹤 JavaScript 不使用 cookies，但會以 IP 偵測國家與頁面訪問。安裝追蹤碼時應同步在網站上揭露訪問統計用途，並依適用法律提供資訊。
不能把追蹤碼與私人 API token 混淆；僅安裝 Metricool 指示放在公開網站的 JavaScript tracking tag，不應把帳戶秘密資料存到公開 GitHub。