# SmartPicksTW 網站訪客分析串接 — Metricool

目前狀態（2026-10-23）：**已將 Metricool 官方提供的 JavaScript 追蹤碼安裝到 GitHub 儲存庫的 index.html、guides.html、about.html**，並驗證各頁僅安裝一次。**尚待使用者在 Metricool Connections 完成網站驗證，並確認 GitHub Pages 部署後有實際訪客數據。** 追蹤資料無法事後回溯。

## 為什麼要做
目前只有 Facebook 貼文／Reels 的排程及社群指標，沒有可靠的網站訪客、來源、點擊或蝦皮結帳資料。
先完成網站訪客分析，可區分「Facebook 觸及」與「實際進入網站」。

## 目前只需確認網站連線
1. 開啟 [Metricool Connections](https://app.metricool.com/brands/connections?blogId=7545618)。
2. 點選 **Web** 區塊，選擇 Verify connection／Connect／驗證（依畫面顯示）。不要再產生或重複插入另一份追蹤碼。
3. 在無痕視窗實際訪問首頁和指南頁各一次，使追蹤碼有機會執行。
4. 待 GitHub Pages 更新後，在 Metricool 的 Website/Analytics 查看是否出現訪客統計。Connect 成功不等於已累積有效流量。
5. 如驗證失敗，檢查網站部署是否已反映最新 GitHub 提交，並檢查瀏覽器是否有阻擋分析追蹤的設定；不要直接宣稱已驗證。

網站已安裝的三個頁面：
- `index.html` — 商品首頁
- `guides.html` — 原創選購指南
- `about.html` — 聯盟與隱私說明

原始追蹤碼與 Metricool 品牌 `7545618` 的 hash 經過比對一致。已同步更新網站隱私聲明，未公開個別商品佣金資訊。

## 建議 Facebook 導流網址
- 粉專網站按鈕：`https://japerchen.github.io/smartpicks-tw/?utm_source=facebook&utm_medium=profile&utm_campaign=page_button`
- 貼文到商品目錄：`https://japerchen.github.io/smartpicks-tw/?utm_source=facebook&utm_medium=post&utm_campaign=product_post`
- USB-C Hub Reel：`https://japerchen.github.io/smartpicks-tw/guides.html?utm_source=facebook&utm_medium=reels&utm_campaign=usb_c_hub`
- 磁吸支架 Reel：`https://japerchen.github.io/smartpicks-tw/guides.html?utm_source=facebook&utm_medium=reels&utm_campaign=phone_stand`
- 行動電源 Reel：`https://japerchen.github.io/smartpicks-tw/guides.html?utm_source=facebook&utm_medium=reels&utm_campaign=power_bank`

網站指南目前支援按已知 `utm_campaign` 自動定位到相關內容。UTM 只是在 URL 上標示來源；**追蹤碼已寫入，仍須平台部署、成功載入並於 Metricool 產生資料後，才能報告真實訪客數**。

## 分辨真正可量測的數據
| 指標 | 來源 | 現階段 |
|---|---|---|
| Facebook 粉絲 | Metricool Facebook Evolution | 可取得 |
| Facebook Reels 觀看 | Metricool Facebook Evolution | 發布並收集後可取得 |
| Website visits / URL 來源 | Metricool Website Analytics | 追蹤碼已加入儲存庫；等待網站驗證與訪客資料 |
| 點擊個別蝦皮連結的次數 | 需網站端額外事件追蹤 | 尚未建置 |
| 蝦皮訂單、分潤金額 | 蝦皮聯盟後台 | 不能由 Facebook 或網站訪客指標臆測 |

## 隱私及防護
網站已在 about.html 揭露 Metricool 訪問統計用途、資料處理可能涉及裝置、來源及網路連線資訊，並提醒訪客參考第三方隱私政策。網站實際部署後仍須確認符合適用隱私法規及平台政策。
不能把追蹤碼與私人 API token 混淆；僅安裝 Metricool 指示放在公開網站的 JavaScript tracking tag，不應把帳戶秘密資料存到公開 GitHub。