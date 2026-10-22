# SmartPicksTW Organic Growth Runbook

_Started 2026-10-22 · Asia/Taipei · No paid advertising authorized._

## Goal
Turn a newly launched Facebook Page with zero followers into an audience that trusts original electronics-shopping education. Use educational Reels for discovery, original buying guides for trust, and 100-product catalog for optional purchases. No artificial followers or engagement.

## Public resources
- Catalog: https://japerchen.github.io/smartpicks-tw/
- Original buyer guides: https://japerchen.github.io/smartpicks-tw/guides.html
- Inventory: `index.html` embedded JSON (`inventory`, 100 records)
- Post/reel de-duplication history: `social_automation_state.json`
- Original Reel creative catalog: `reels_catalog.json`
- Cloud rendering: `growth/reels_cloud.py`
- GitHub Actions: `.github/workflows/generate-reels.yml`
- Hosted original videos: `reels/*.mp4`

## Publish pipeline
1. GitHub Actions runs every Sunday around 00:30 Asia/Taipei to generate up to two previously unpublished Reel videos from evergreen original tech lessons. Rendering may fail or exhaust content; do not invent successful uploads.
2. The connected weekly ChatGPT Automation then checks the public inventory, catalog, history, and Metricool availability before scheduling.
3. Proposed ongoing mix **two promotional Facebook posts (Mon/Fri) plus two educational Facebook Reels (Tue/Sat) weekly at 20:00 Asia/Taipei**. Existing Oct 23–Nov 1 schedules are retained.
4. Facebook posts must use genuine affiliate links and never display individual commission rates/amounts. Reels use original videos, not third-party product clips.
5. Confirm via Metricool returned IDs and independent `getScheduledPosts` read. Pending means scheduled, **not** published.
6. Save new successful scheduled topic/product IDs in the public history JSON. Never write credentials, buyer identities, commissions, or non-public account details.

## Organic discovery principles
- First seconds: a problem-led headline (USB-C compatible?; 4K 60Hz?; Wh vs mAh?).
- Teach one useful technical concept; avoid overstated test claims, health claims, product safety promises, or unverified retailer prices.
- Link to the original buyer guide, clearly disclose affiliate status, and encourage followership.
- Do not buy followers, engagement, or ads without a separate approved budget.
- Only share in groups when moderators permit relevant posts; avoid spam.

## Weekly check
Read actual Metricool Facebook Page Followers, Page Views, feed posts, Reels video views, and interactions. Separate new followers from views and business value. **Metricool website tracking has been installed and its Realtime display has shown a test visitor. GA4 measurement G-GLD8BQ37MK has also been configured, and a consented test sent `select_item` successfully.** Still distinguish test events from real acquisition, do not assume website visits, affiliate orders or sales from Facebook Reels impressions. Real GA4 click counts can lag and are not a purchase confirmation.

## Constraints and safeguards
- Metricool plan currently showed a 20-post monthly allowance; new post attempts should stop or reduce cadence as limits approach. This is a verified UI snapshot, not an assumption about future billing.
- No human review requested for Facebook scheduling; check sources, link validity, and risk automatically instead. If any safeguard cannot be passed, skip only the affected post and report why.
- Github Actions' automated pushes must handle concurrent commits and may require a retry if media is not publicly available before scheduling.
- The initial 12 evergreen video topics will eventually be exhausted. Do not repeat an old asset while pretending it is new; report that the library needs original new topics.
- Never change Shopee affiliate short URLs or reveal secret internal affiliate details.


## YouTube Shorts expansion (prepared, not connected)
- Five original ~20s educational video files were confirmed in GitHub: `reels/usb_c_hub.mp4`, `reels/phone_stand.mp4`, `reels/power_bank.mp4`, `reels/usb_c_cable.mp4`, `reels/hdmi_refresh.mp4`.
- `youtube_shorts_manifest.json` contains verified video references, Traditional Chinese Shorts metadata, UTM guides links, affiliate disclosures, and optional dates.
- `youtube_shorts_upload.csv` contains spreadsheet-friendly publishing metadata; `YOUTUBE_SHORTS_DEPLOYMENT.md` has full operator steps.
- **YouTube connected as of 2026-10-23.** Two Metricool YouTube Shorts were accepted for auto-publication: 2026-11-11 20:00 (`403442945`, USB-C cable buying guide with real catalog item 21295904242) and 2026-11-25 20:00 (`403438751`, magnetic phone stand), Asia/Taipei. Both were independently confirmed PENDING, meaning not yet public. Leave remaining 3 prepared videos unscheduled unless there is a confirmed spare posting allowance.
- Metricool Free counts 20 posts **published** per month across social networks. Each social network counts separately. In Nov 2026 the intended Facebook plan is about 18 posts including Nov 1, leaving room for up to two YouTube Shorts if no additional posts consume allowance. Suggested Shorts slots: Nov 11/25 at 20:00 Taiwan. Query actual posts and account status before scheduling.

## Initial launch
As of 2026-10-22, five Facebook product promotion posts and three original video Reels were scheduled. The original videos have been accepted and rehosted by Metricool, and the eight entries were independently confirmed as Pending. Initial Facebook Analytics indicates zero Page Followers. New posts cannot guarantee reach, follows, or purchases.

_Update: 2026-10-23 · GA4 click tracking verified in user's realtime screenshot; YouTube authenticated and two original Shorts pending auto-publication on Nov 11/25._

## 2026-10-23 product-catalog correction
Actual public 100-product inventory contains zero USB-C Hub products. To keep promotional content aligned with actual products, Facebook 2026-10-24 20:00 Reel now uses the original USB-C cable explainer (Metricool Post ID `403444733`), and YouTube 2026-11-11 20:00 uses the same authentic cable educational video (ID `403442945`). Both are confirmed PENDING and autoPublish. Copy links to actual product ID `21295904242`, not a fabricated Hub product. The original Hub tutorial remains unscheduled educational material only. reels_catalog.json omits Hub to prevent the weekly automation from putting it back.
