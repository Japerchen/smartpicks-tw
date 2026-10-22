# SmartPicksTW × Tech Finds Lab — YouTube Shorts Launch Kit

建立日期：2026-10-23（Asia/Taipei）。

## 總結

已核對 GitHub 具備以下五支**原創、約 20 秒、直式 MP4** 影片：`usb_c_hub.mp4`、`phone_stand.mp4`、`power_bank.mp4`、`usb_c_cable.mp4`、`hdmi_refresh.mp4`。

每支影片的搜尋友善標題、繁體中文說明、公開影片 URL、YouTube UTM 與揭露聲明均整理在：
- `youtube_shorts_manifest.json`（給程式／排程使用的 JSON）
- `youtube_shorts_upload.csv`（方便 Excel 審查的 UTF-8 BOM CSV）

**狀態（2026-10-23）：Metricool 已連接 SmartPicksTW YouTube 頻道（ID 與先前 YouTube Studio 截圖一致）。已安排兩支 Short 並核對均為 Auto Publish=true、Pending；未到發布日期，尚未公開。** 剩下三支素材未排程。

## YouTube 授權已完成

Metricool `getBrandSettings` 已回傳 `youtubeData` 指向使用者先前 YouTube Studio 中的頻道 ID。兩支 Shorts 已經由 `createScheduledPost` 成功排入並再次由 `getScheduledPosts` 查證。

使用者的 YouTube 公開頁面截圖當時仍顯示正式名稱 **Tech Finds Lab**，但 Handle 已為 `@SmartPicksTW`、大頭貼與封面已換成 SmartPicksTW。此命名同步問題**不影響相同頻道 ID 的連線及排程**。使用者應到 YouTube Studio → 自訂 → 個人資料，核對正式頻道名稱已儲存並按「發布」；公開頁面可能需要刷新。

官方說明：https://help.metricool.com/how-to-connect-youtube-to-metricool-tqiwo

## 免費方案配額與日期

Metricool 免費方案每月最多**實際發布 20 篇**，同一內容發到 Facebook 及 YouTube 各計一篇。2026 年 11 月，依目前 Facebook 每週四篇配置加上 11/1 既有貼文，約有 18 篇 Facebook 內容。若所有 Facebook 排程都實際發布，則最多只剩 **2 篇 YouTube Shorts** 的額度。額度以 Metricool 實際狀態為準。

**已確認的第一批 YouTube 自動排程：**

| 發布日期（台灣時間） | Shorts | 影片 |
|---|---|---|
| 2026-11-11 20:00 | USB-C 線材都一樣？ | `reels/usb_c_cable.mp4` |
| 2026-11-25 20:00 | 磁吸手機支架為何吸不牢？ | `reels/phone_stand.mp4` |

已成功回查 11/11 的 Metricool Post ID `403442945`、11/25 的 Post ID `403438751`，兩篇 `PENDING` 且 `autoPublish=true`、`youtubeData.type=short`。其餘三支為備用，**不能直接排滿**而超出免費方案的總篇數。若平台額度不足，應停止後續新排程；已排定不等於已公開。

官方配額：https://help.metricool.com/main-differences-between-free-and-paid-plans-bl0v9

## 發布設定
- 平台：YouTube Shorts（原創直式 MP4）。
- 標題：取 manifest 的 `title`，在 100 個字元限制內。
- 說明：取 `description`，保留 `utm_source=youtube&utm_medium=shorts` 的導流網址和聯盟揭露。
- 影片：取 `originalVideoUrl`（GitHub 公開直式 MP4；已核對 Github 中實體影片存在）。
- 公開設定：`PUBLIC`，但只在指定日期發布。
- 觀眾：`Not made for kids`（一般科技選購教學）。
- AI/合成內容揭露：依實際內容與 YouTube 及 Metricool 顯示的最新定義設定。這些影片是合成文字動畫，不應宣稱是實拍或測試；如出現需要針對逼真的合成或改造內容標示的情形則如實標註。
- 不額外插入未經授權的商品圖片、剪輯或音樂。影片只有原創動畫與原創合成背景音樂。
- 發布後在 YouTube Studio 確認公開狀態及 Analytics，不能把 `PENDING` 當成已上線。

官方發文說明：https://help.metricool.com/schedule-and-publish-on-youtube-gof0k

## 怎麼看成效
1. 在 GA4 中檢查 YouTube UTM 流量是否增加，來源應有 `youtube / shorts`，有瀏覽才有資料。
2. 在 YouTube Studio / Metricool 看 Shorts 觀看與停留，不要把 YouTube 觀看數直接換算網站訪客或成交。
3. 商品選取事件 `select_item` 只追蹤同意 Google Analytics 的訪客點擊，仍不代表蝦皮訂單或分潤。
4. 每週比較 Reels / Shorts 的不同題目，引導到網站的成效，避免因單一測試觀看過少便認定某款商品表現最好。

## 防呆
- 請勿修改既有八筆 Facebook 排程。
- YouTube 已連線；使用 `youtube_shorts_manifest.json` 中逐篇 `metricoolStatus` 去重，兩篇預定中的狀態為 `SCHEDULED_PENDING`，其他三篇為 `NOT_SCHEDULED`。
- 記錄 Metricool 回傳的貼文 ID 與實際排程狀態，避免重複。
- 保留網站聯盟揭露，勿公布個別商品分潤率與佣金金額。

## 2026-10-23 更正：USB-C Hub 並非現有導購商品
已重新檢索網站 100 筆庫存：沒有 USB-C Hub／集線器。原本 11/11 的 USB-C Hub 教學 Short 已在 Metricool 原地更新成《USB-C 線材都一樣？》原創影片，保留 20:00 自動發布，新的 Metricool ID 為 `403442945`。文案只連結實際存在的 Type-C 充電線商品 `21295904242`（`https://s.shopee.tw/4LKIFe9whm`），明確區分知識內容與非實測商品，未改動蝦皮短網址。USB-C Hub 題材保留為未排程的純知識備稿，不能當作 100 商品中的商品推薦。
