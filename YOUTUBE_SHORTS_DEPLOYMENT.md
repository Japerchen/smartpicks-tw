# SmartPicksTW × Tech Finds Lab — YouTube Shorts Launch Kit

建立日期：2026-10-23（Asia/Taipei）。

## 總結

已核對 GitHub 具備以下五支**原創、約 20 秒、直式 MP4** 影片：`usb_c_hub.mp4`、`phone_stand.mp4`、`power_bank.mp4`、`usb_c_cable.mp4`、`hdmi_refresh.mp4`。

每支影片的搜尋友善標題、繁體中文說明、公開影片 URL、YouTube UTM 與揭露聲明均整理在：
- `youtube_shorts_manifest.json`（給程式／排程使用的 JSON）
- `youtube_shorts_upload.csv`（方便 Excel 審查的 UTF-8 BOM CSV）

**狀態：影片及文案準備完成，但沒有在 YouTube 或 Metricool 排程，也沒有公開上傳。** Metricool 目前已連接 Facebook 和網站，尚未連接 YouTube。

## 需要帳號管理人本人完成的唯一授權

1. 開啟 https://app.metricool.com/brands/connections?blogId=7545618
2. 在同一品牌 `Smartpickstw` 找到 `YouTube`，點 `Connect a YouTube channel`。
3. 在 Google 授權頁，以**原本 Tech Finds Lab YouTube 頻道的擁有者帳號**登入，選擇確實擁有的正確頻道，閱讀並授權所需功能。
4. 回到 Metricool Connections，確認 YouTube 區塊已由 Connect 狀態變為已連接頻道；不要連到無關的 Google／YouTube 帳號。
5. 連線完成後，方可從 `youtube_shorts_manifest.json` 自動安排真實影片。若未成功，則保留成品並回報錯誤，不能假裝 YouTube 已發文。

官方說明：https://help.metricool.com/how-to-connect-youtube-to-metricool-tqiwo

## 免費方案配額與日期

Metricool 免費方案每月最多**實際發布 20 篇**，同一內容發到 Facebook 及 YouTube 各計一篇。2026 年 11 月，依目前 Facebook 每週四篇配置加上 11/1 既有貼文，約有 18 篇 Facebook 內容。若所有 Facebook 排程都實際發布，則最多只剩 **2 篇 YouTube Shorts** 的額度。額度以 Metricool 實際狀態為準。

**建議的第一批 YouTube 測試：**

| 發布日期（台灣時間） | Shorts | 影片 |
|---|---|---|
| 2026-11-11 20:00 | USB-C Hub 插上卻沒畫面？ | `reels/usb_c_hub.mp4` |
| 2026-11-25 20:00 | 磁吸手機支架為何吸不牢？ | `reels/phone_stand.mp4` |

其餘三支為備用，**不能直接排滿**而超出免費方案的總篇數。若日期、平台連接或額度不允許，要延後而不是產生失敗中的排程。

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
- 未連接 YouTube 時，工作狀態必須保持 `NOT_SCHEDULED`。
- 記錄 Metricool 回傳的貼文 ID 與實際排程狀態，避免重複。
- 保留網站聯盟揭露，勿公布個別商品分潤率與佣金金額。
