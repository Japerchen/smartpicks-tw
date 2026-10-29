#!/usr/bin/env python3
"""Fail closed when planned Reels imply products absent from SmartPicksTW.

Standalone standard-library check, used in GitHub Actions before rendering.
This DOES NOT check retailer stock, live prices, product licensing, or sales.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TITLE_PATTERNS = {
    "phone_stand": re.compile(r"磁吸支架"),
    "power_bank": re.compile(r"行動電源"),
    "usb_c_cable": re.compile(r"充電線|傳輸線"),
    "usb_power": re.compile(r"充電線|傳輸線"),
    "usb_c_hub": re.compile(r"Hub|集線器|轉接", re.IGNORECASE),
    "sneaker_fit": re.compile(r"鞋|New Balance|adidas", re.IGNORECASE),
}
CATEGORY_MATCH = {
    "phone_stand": {"手機殼／支架"},
    "power_bank": {"行動電源"},
    "usb_c_cable": {"充電線／傳輸線"},
    "usb_power": {"充電線／傳輸線"},
    "usb_c_hub": {"USB Hub／轉接器"},
    "sneaker_fit": {"鞋款"},
}
SHORT = re.compile(r"^https://s\.shopee\.tw/[A-Za-z0-9]+$")


def check() -> None:
    source = (ROOT / "index.html").read_text(encoding="utf-8")
    match = re.search(
        r'<script\s+type="application/json"\s+id="inventory">([\s\S]*?)</script>',
        source,
    )
    if not match:
        raise ValueError("Missing embedded product inventory in index.html")
    inventory = json.loads(match.group(1))
    if not inventory:
        raise ValueError("Public inventory is empty")
    if any(p.get("price") == 1 for p in inventory):
        raise ValueError("NT$1 products must not be in the public inventory")
    if len(set(str(p["id"]) for p in inventory)) != len(inventory):
        raise ValueError("Duplicate product IDs")
    lookup = {str(p["id"]): p for p in inventory}

    mapping = json.loads((ROOT / "growth/reel_product_map.json").read_text(encoding="utf-8"))
    catalog = json.loads((ROOT / "reels_catalog.json").read_text(encoding="utf-8"))
    known_slugs = [x["slug"] for x in catalog["topics"]]
    rules = mapping["topics"]
    rule_slugs = [x["slug"] for x in rules]

    if len(set(known_slugs)) != len(known_slugs) or len(set(rule_slugs)) != len(rule_slugs):
        raise ValueError("Duplicate video-topic slugs")
    if set(rule_slugs) != set(known_slugs):
        raise ValueError("Video topics and product mapping must have the same slugs")
    matched = 0
    for rule in rules:
        slug = rule["slug"]
        valid = bool(rule["eligibleForAutomaticDirectProductPromotion"])
        ids = [str(x) for x in rule["productIds"]]
        if (rule["promotionMode"] == "product_related") != valid:
            raise ValueError(f"Invalid promotional flag for {slug}")
        if bool(ids) != valid:
            raise ValueError(f"Product-related topic must list actual product IDs; education-only must not: {slug}")
        if valid and slug not in TITLE_PATTERNS:
            raise ValueError(f"Unknown product category matching rule for {slug}")
        for product_id in ids:
            p = lookup.get(product_id)
            if p is None:
                raise ValueError(f"{slug}: missing real product ID {product_id}")
            if p.get("flags"):
                raise ValueError(f"{slug}: product {product_id} has verification flags")
            if p.get("category") not in CATEGORY_MATCH.get(slug, set()):
                raise ValueError(f"{slug}: product {product_id} has unexpected category {p.get('category')}")
            if not SHORT.fullmatch(p.get("affiliate_url", "")):
                raise ValueError(f"{slug}: product {product_id} has no approved affiliate short URL")
            if not TITLE_PATTERNS[slug].search(p.get("title", "")):
                raise ValueError(f"{slug}: product {product_id} title does not support subject")
            matched += 1

    print(f"PASS: {len(inventory)} products, {len(rules)} topics, {matched} verified topic-product matches.")
    print("Educational-only videos will not be treated as actual inventory recommendations.")


if __name__ == "__main__":
    try:
        check()
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print("FAIL: SmartPicksTW promotion inventory mapping:", exc, file=sys.stderr)
        sys.exit(1)
