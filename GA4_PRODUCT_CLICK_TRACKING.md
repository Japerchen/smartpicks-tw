# SmartPicksTW — GA4 個別商品點擊分析（V1 準備完成）

更新日期：2026-10-23，台灣時間

## 實際完成狀態
- `index.html` 中的 100 個蝦皮商品按鈕均已加入 `data-product-id` / `data-product-category` 作為非私人產品辨識資訊。
- 100 條 `https://s.shopee.tw/` 真實聯盟連結原樣保留，沒有添加中繼站、改寫短連結或自動跳轉。
- `guides.html` 的已知蝦皮商品連結也有獨立產品 ID。
- `analytics-config.js` 和 `outbound-analytics.js` 已加入首頁、指南與關於頁。
- **測量 ID 目前留空，GA4 未啟用。** 這時不會發送任何 GA4 事件，也不會載入 Google Analytics script。
- 若設定有效測量 ID，訪客首次進入時會看到分析同意或拒絕的選項；只有同意才會載入 Google script。使用者可在 `about.html` 修改偏好。
- 原本已接上的 Metricool 訪客統計保留，並不等同 GA4 產品事件。
- 目前尚未產生網站全體的商品點擊統計，也沒有蝦皮實際訂單／分潤資料。

## 讓正式數據開始計入（僅需 GA4 Measurement ID）
1. 進入 https://analytics.google.com ，使用自己管理的 Google 帳號。
2. 若沒有帳戶，建立 Google Analytics 帳戶，例如 `SmartPicksTW`。
3. 建立 GA4 資源（Property），時區選 `Asia/Taipei`、幣別選 `TWD`。
4. 建立 Web 資料串流，網址填 `https://japerchen.github.io/smartpicks-tw/`。
5. 在 Web data stream 詳細設定中複製 **Measurement ID**，例如 `G-XXXXXXXXXX`。此 ID 是公開的網站資料串流標識，不是 Google 密碼或 API 私鑰。
6. 由管理人員把這個 ID 寫進 GitHub 根目錄的 `analytics-config.js` 的 `measurementId` 欄位，其他檔案不需要再次安裝。
7. 同步調整 `about.html` 隱私聲明，說明 GA4 啟用與使用者同意；GitHub Pages 部署後，在無痕視窗確認同意選擇正常。
8. 使用 GA4 **Realtime／DebugView** 做測試；需點選「同意分析」再按一個商品按鈕才能有 `select_item` 事件。不要為測試購買商品。

官方說明：
- GA4 設定：https://support.google.com/analytics/answer/14183469
- 找 Measurement ID：https://support.google.com/analytics/answer/12270356
- 官方自動偵測離站點擊：https://support.google.com/analytics/answer/13566436

## GA4 事件與產品識別
- 名稱：`select_item`（**點擊選取商品，不代表訂單成交**）
- `item_list_name` = `SmartPicksTW catalog`
- `items[0].item_id` = 商品 ID，例如 `41251665857`
- `items[0].item_name` = 網站既有的公開商品標題
- `items[0].item_category` = 商品分類
- 無佣金、分潤率、帳號、使用者身份、購物車或付款資料。

建議在 GA4 Exploration 中，以 `Event name = select_item` 篩選，依 `Item ID`、`Item name` 或 `Item category` 統計事件數。若開啟 GA4 Web stream 的 Enhanced measurement，GA4 亦可自動產生 `click`（離站點擊），透過 `Link URL` 查各條完整分潤短連結。**不要把 `select_item` 與 `click` 的事件數直接相加**，因為同一次點擊可能各產生一筆不同類型事件。

## 數據可以做什麼
- 找出被點擊最多的商品和分類、比較隨時間的變化。
- 配合已連接的 Metricool `Web > Traffic` 資料，判斷網站訪問與商品點擊之間的差距。
- 持續使用原創 Reels 導流，避免依少量樣本直接認定某個商品一定賣得好。

## 數據不能做什麼
- 商品點擊數 ≠ 蝦皮有效訂單數、獲利或回饋佣金。
- 沒有測量 ID／使用者未同意／瀏覽器封鎖追蹤時，GA4 不會得到完整點擊事件，因此點擊數不是全部訪客的精確總數。
- 不得將 Metricool 頁面瀏覽數當成商品按鈕的點擊數。

## 推廣安全
- 不變更、轉碼、加參數到蝦皮的聯盟短網址。
- 不在公開網頁揭露個別佣金金額、分潤率或內部排名。
- 不需要額外的自動重新導向頁面；保護轉換流程與訪客體驗。
