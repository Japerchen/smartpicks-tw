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
Read actual Metricool Facebook Page Followers, Page Views, feed posts, Reels video views, and interactions. Separate new followers from views and business value. **No site visitor or conversion analytics are connected**; `utm_*` query parameters in Reels links are future measurement preparation, not proof of click count or revenue.

## Constraints and safeguards
- Metricool plan currently showed a 20-post monthly allowance; new post attempts should stop or reduce cadence as limits approach. This is a verified UI snapshot, not an assumption about future billing.
- No human review requested for Facebook scheduling; check sources, link validity, and risk automatically instead. If any safeguard cannot be passed, skip only the affected post and report why.
- Github Actions' automated pushes must handle concurrent commits and may require a retry if media is not publicly available before scheduling.
- The initial 12 evergreen video topics will eventually be exhausted. Do not repeat an old asset while pretending it is new; report that the library needs original new topics.
- Never change Shopee affiliate short URLs or reveal secret internal affiliate details.

## Initial launch
As of 2026-10-22, five Facebook product promotion posts and three original video Reels were scheduled. The original videos have been accepted and rehosted by Metricool, and the eight entries were independently confirmed as Pending. Initial Facebook Analytics indicates zero Page Followers. New posts cannot guarantee reach, follows, or purchases.
