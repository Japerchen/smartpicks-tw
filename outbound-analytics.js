/* SmartPicksTW outbound affiliate product event tracking (GA4 optional, opt-in). */
(function () {
  "use strict";
  const cfg = window.SPTW_ANALYTICS_CONFIG || {};
  const id = typeof cfg.measurementId === "string" ? cfg.measurementId.trim().toUpperCase() : "";
  const key = cfg.consentStorageKey || "smartpickstw_ga4_analytics_consent_v1";
  const valid = /^G-[A-Z0-9]{5,20}$/.test(id);
  let enabled = false;
  let banner = null;
  const read = () => { try { return localStorage.getItem(key); } catch (_) { return null; } };
  const write = value => { try { localStorage.setItem(key, value); } catch (_) {} };
  function enable() {
    if (!valid || enabled) return;
    enabled = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", id, { send_page_view: true });
    const script = document.createElement("script");
    script.async = true;
    script.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(id);
    document.head.appendChild(script);
    if (banner) { banner.remove(); banner = null; }
  }
  function closeBanner() { if (banner) { banner.remove(); banner = null; } }
  function setChoice(consent) {
    write(consent ? "granted" : "denied");
    closeBanner();
    if (consent) enable();
    else if (enabled) window.location.reload(); // Stop further Google requests on this page.
  }
  function showBanner() {
    if (!valid || banner || document.readyState === "loading") return;
    banner = document.createElement("aside");
    banner.setAttribute("role", "region");
    banner.setAttribute("aria-label", "網站分析偏好設定");
    Object.assign(banner.style, {
      position: "fixed", zIndex: "10000", bottom: "16px", left: "16px", right: "16px",
      margin: "auto", maxWidth: "680px", background: "#12233d", color: "#fff",
      borderRadius: "16px", padding: "18px 20px", boxShadow: "0 10px 35px #06101e66",
      font: '14px/1.65 system-ui,-apple-system,"Noto Sans TC",sans-serif'
    });
    const info = document.createElement("p");
    info.style.margin = "0 0 12px";
    info.textContent = "是否同意使用 Google Analytics 統計網站及商品按鈕的點擊？不同意仍可正常瀏覽與前往蝦皮，不影響原本的 Metricool 無 Cookie 訪問統計。";
    const row = document.createElement("div");
    row.style.cssText = "display:flex;flex-wrap:wrap;gap:10px;align-items:center";
    for (const [label, yes] of [["同意分析", true], ["不同意", false]]) {
      const b = document.createElement("button");
      b.type = "button"; b.textContent = label;
      b.style.cssText = "border:0;border-radius:8px;padding:9px 15px;cursor:pointer;font-weight:750;background:" + (yes ? "#fa7955;color:#fff" : "#e9eef5;color:#22344d");
      b.addEventListener("click", () => setChoice(yes));
      row.appendChild(b);
    }
    const policy = document.createElement("a");
    policy.href = "./about.html"; policy.textContent = "隱私說明";
    policy.style.cssText = "color:#c5d8ed;text-decoration:underline;margin-left:auto";
    row.appendChild(policy);
    banner.append(info, row);
    document.body.appendChild(banner);
  }
  function boot() {
    if (!valid) return;  // GA4 ID not configured: do not contact Google or show a banner.
    const decision = read();
    if (decision === "granted") enable();
    else if (decision !== "denied") showBanner();
  }
  document.addEventListener("click", function (ev) {
    if (!enabled || read() !== "granted" || typeof window.gtag !== "function") return;
    const origin = ev.target;
    const a = origin && origin.closest ? origin.closest('a[data-product-id][href^="https://s.shopee.tw/"]') : null;
    if (!a) return;
    const pid = a.getAttribute("data-product-id");
    if (!pid || !/^\d+$/.test(pid)) return;
    const card = a.closest(".card");
    const title = (a.getAttribute("data-product-name") || (card && card.querySelector(".name") && card.querySelector(".name").textContent) || "").slice(0,120);
    const category = a.getAttribute("data-product-category") || (card && card.getAttribute("data-category")) || "其他";
    // select_item is GA4's recommended e-commerce item-selection event. This is a click, NOT a sale.
    window.gtag("event", "select_item", {
      item_list_name: "SmartPicksTW catalog",
      items: [{ item_id: pid, item_name: title, item_category: category }],
      transport_type: "beacon"
    });
  }, true);
  window.SmartPicksAnalytics = {
    get ready() { return valid && enabled; },
    get configured() { return valid; },
    get consent() { return read(); },
    changeConsent: function () { if (!valid) return false; write(""); if (enabled) window.location.reload(); else showBanner(); return true; }
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot, { once: true });
  else boot();
})();
