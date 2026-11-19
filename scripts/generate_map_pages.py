#!/usr/bin/env python3
"""Generate per-map wiki pages for Trackmania Galaxy.

Sources
-------
1. ManiaPlanet Feedback episode pages (the official server map list with ratings):
   https://feedback.prod.live.maniaplanet.com/votes/display/<episode>
2. ManiaExchange API (author, environment, map type, upload date, MX id):
   https://tm.mania.exchange/api/maps/get_map_info/id/<UID>

Output
------
- docs/maps/<slug>.md  — one page per map (gallery + record history live in the
  page's front matter, so community entries are never overwritten by a re-run)
- data/maps.json       — cached source data, so pages can be regenerated offline

Usage
-----
    python3 scripts/generate_map_pages.py                     # fetch + generate
    python3 scripts/generate_map_pages.py --offline --cache data/maps.json
    python3 scripts/generate_map_pages.py --episodes 106 107  # several playlists
    python3 scripts/generate_map_pages.py --limit 5           # smoke test

Only stdlib is required. Existing pages are left untouched unless --refresh is
passed (which needs PyYAML and still preserves screenshots/records/body text).
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FEEDBACK_URL = "https://feedback.prod.live.maniaplanet.com/votes/display/{episode}"
MX_URL = "https://tm.mania.exchange/api/maps/get_map_info/id/{uid}"
UA = {"User-Agent": "Mozilla/5.0 (GalaxyWiki-MapGenerator/1.0)"}

MODE_BY_MAPTYPE = {
    "PursuitArena": "Pursuit",
    "GoalHuntArena": "Goal Hunt",
    "HuntersArena": "Hunters",
}
GENERATED_KEYS = {
    "layout", "title", "parent", "nav_exclude", "search_exclude", "map",
    "uid", "map_name", "mode", "map_type", "environment", "mapper",
    "mx_url", "mx_id", "thumbnail", "uploaded", "titlepack", "feedback",
}


def http_get(url: str, timeout: int = 45) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", "replace")


def parse_feedback(page: str, episode: int) -> list[dict]:
    """Split the feedback page into map cards and pull name, UID, hash, ratings."""
    maps = []
    for card in re.split(r'(?=<div class="m-2" style="max-width: 250px;">)', page):
        img = re.search(
            r'<img src="https://files-v4\.live\.maniaplanet\.com/maps/([0-9a-f]+)/([^"]+)\.jpg"',
            card,
        )
        if not img:
            continue
        hash_, uid = img.group(1), img.group(2)
        title = re.search(r'<h6 class="card-title[^"]*" title="([^"]*)"', card)
        name = html.unescape(title.group(1)).strip() if title else uid

        def rating(label: str):
            sec = re.search(label + r".*?</h6>(.*?)</div>\s*</div>", card, re.S)
            if not sec:
                return None, None
            hit = re.search(r"([\d.]+)\s*\((\d+)\)", sec.group(1))
            return (float(hit.group(1)), int(hit.group(2))) if hit else (None, None)

        yn_rating, yn_votes = rating("YES/NO")
        stars_avg, stars_total = rating("5 STARS")
        maps.append({
            "name": name,
            "uid": uid,
            "hash": hash_,
            "thumbnail": f"https://files-v4.live.maniaplanet.com/maps/{hash_}/{uid}.jpg",
            "yn_rating": yn_rating,
            "yn_votes": yn_votes,
            "stars_avg": stars_avg,
            "stars_total": stars_total,
            "source_episode": episode,
        })
    return maps


def mx_info(uid: str, retries: int = 3) -> dict:
    for attempt in range(retries):
        try:
            data = json.loads(http_get(MX_URL.format(uid=uid), timeout=20))
            return data if isinstance(data, dict) and data.get("TrackID") else {}
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return {}
            time.sleep(0.6 * (attempt + 1))
        except Exception:
            time.sleep(0.6 * (attempt + 1))
    return {}


def sanitize(raw: str) -> str:
    """Drop control characters (MX usernames can carry them) — they break YAML front matter."""
    return "".join(ch for ch in raw if unicodedata.category(ch)[0] != "C")


def clean_name(raw: str) -> str:
    """Strip ManiaPlanet formatting codes ($s, $fff, $i, $z, ...) and tidy spaces."""
    name = sanitize(raw)
    name = re.sub(r"\$[0-9a-fA-F]{3}", "", name)
    name = re.sub(r"\$[a-zA-Z]", "", name)
    name = name.replace("''", "'")
    return re.sub(r"\s+", " ", name).strip()


def slugify(name: str, uid: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    slug = re.sub(r"-{2,}", "-", slug)[:60].strip("-")
    return slug or f"map-{uid[:8].lower()}"


def yaml_str(value: str) -> str:
    value = sanitize(str(value))
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def wr_record(mx: dict) -> str | None:
    """Seed the record table with the ManiaExchange world-record replay, when present."""
    if not mx.get("ReplayWRTime") or not mx.get("ReplayWRID"):
        return None
    ms = int(mx["ReplayWRTime"])
    time_str = f"{ms // 60000}:{(ms % 60000) // 1000:02d}.{ms % 1000:03d}"
    player = json.dumps(mx.get("ReplayWRUsername") or "unknown")
    return (
        "records:\n"
        f"  - player: {player}\n"
        f"    time: {json.dumps(time_str)}\n"
        '    mode: ""\n'
        f"    replay: \"https://tm.mania.exchange/replays/{mx['ReplayWRID']}\"\n"
        '    note: "World record on ManiaExchange (date not published)"\n'
    )


def page_front_matter(m: dict, slug: str) -> str:
    mx = m.get("mx") or {}
    name = clean_name(m.get("name") or mx.get("Name") or m["uid"])
    map_type = mx.get("MapType") or ""
    uploaded = (mx.get("UploadedAt") or "")[:10]
    lines = [
        "---",
        "layout: default",
        f"title: {yaml_str(name)}",
        "parent: Maps",
        "nav_exclude: true",
        "map: true",
        f"uid: {yaml_str(m['uid'])}",
        f"map_name: {yaml_str(name)}",
        f"mode: {yaml_str(MODE_BY_MAPTYPE.get(map_type, ''))}",
        f"map_type: {yaml_str(map_type)}",
        f"environment: {yaml_str(mx.get('EnvironmentName') or '')}",
        f"mapper: {yaml_str(mx.get('Username') or mx.get('AuthorLogin') or '')}",
        f"mx_url: {yaml_str('https://tm.mania.exchange/maps/' + str(mx['TrackID']) if mx.get('TrackID') else '')}",
        f"mx_id: {mx.get('TrackID') or 0}",
        f"thumbnail: {yaml_str(m.get('thumbnail') or '')}",
        f"uploaded: {yaml_str(uploaded)}",
        f"titlepack: {yaml_str(mx.get('TitlePack') or '')}",
        "feedback:",
        f"  yn_rating: {m.get('yn_rating') if m.get('yn_rating') is not None else 'null'}",
        f"  yn_votes: {m.get('yn_votes') if m.get('yn_votes') is not None else 'null'}",
        f"  stars_avg: {m.get('stars_avg') if m.get('stars_avg') is not None else 'null'}",
        f"  stars_total: {m.get('stars_total') if m.get('stars_total') is not None else 'null'}",
        "",
        "# Community content below — a generator re-run never overwrites these.",
        "screenshots: []",
        wr_record(mx) or "records: []",
        "---",
        "",
    ]
    return "\n".join(lines)


PAGE_BODY = """# {{ page.map_name | escape }}
{: .no_toc }

{% if page.thumbnail != "" %}
<img src="{{ page.thumbnail }}" alt="{{ page.map_name | escape }} thumbnail" style="max-width: 420px; width: 100%; border-radius: 8px;">
{% endif %}

| | |
|---|---|
| **Mode** | {{ page.mode | default: "unclassified" }}{% if page.map_type != "" %} (`{{ page.map_type }}`){% endif %} |
| **Environment** | {{ page.environment | default: "unknown" }} |
| **Mapper** | {{ page.mapper | default: "unknown" }} |
{% if page.uploaded != "" %}| **Uploaded** | {{ page.uploaded }} |
{% endif %}{% if page.mx_url != "" %}| **ManiaExchange** | [Map page]({{ page.mx_url }}) |
{% endif %}{% if page.feedback.stars_avg %}| **Community rating** | {{ page.feedback.stars_avg }}/5 ({{ page.feedback.stars_total }} votes){% if page.feedback.yn_rating %} · YES/NO {{ page.feedback.yn_rating }}/5 ({{ page.feedback.yn_votes }}){% endif %} |
{% endif %}

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## About the map

_No description yet — add layout notes, routes, zones and tactics here._

---

## Screenshots

{% if page.screenshots and page.screenshots.size > 0 %}
<div style="display: flex; flex-wrap: wrap; gap: 12px;">
{% for s in page.screenshots %}
  <figure style="width: 48%; margin: 0;">
    <img src="{% if s.url contains 'http' %}{{ s.url }}{% else %}{{ s.url | relative_url }}{% endif %}" alt="{{ s.caption | default: page.map_name }}" style="width: 100%; border-radius: 8px;">
    <figcaption style="font-size: 0.85rem; opacity: 0.8;">{{ s.caption }}{% if s.author %} — {{ s.author }}{% endif %}{% if s.date %} ({{ s.date }}){% endif %}</figcaption>
  </figure>
{% endfor %}
</div>
{% else %}
{: .highlight }
> No screenshots yet. Add yours with the button below — a link to an image is enough.
{% endif %}

---

## Record history

{% if page.records and page.records.size > 0 %}
| Player | Time | Date | Mode | Replay | Clip | Note |
|--------|------|------|------|--------|------|------|
{% for r in page.records %}| {{ r.player }} | `{{ r.time }}` | {{ r.date }} | {{ r.mode | default: page.mode }} | {% if r.replay %}{% if r.replay contains 'http' %}[link]({{ r.replay }}){% else %}[file]({{ r.replay | relative_url }}){% endif %}{% else %}—{% endif %} | {% if r.clip %}{% if r.clip contains 'http' %}[clip]({{ r.clip }}){% else %}[file]({{ r.clip | relative_url }}){% endif %}{% else %}—{% endif %} | {{ r.note | default: "" }} |
{% endfor %}

{: .note }
> A replay or clip link makes a record verifiable; unlinked times may be marked as unverified.
{% else %}
{: .highlight }
> No records yet. Be the first to submit a time.
{% endif %}

---

## Add your screenshot or record

[Submit a screenshot or record](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-record.yml&labels=map-record&title=%5BMap%5D%20{{ page.map_name | url_encode }}){: .btn .btn-primary }
[Edit this page on GitHub](https://github.com/tomekdot/trackmania-galaxy/edit/main/{{ page.path }}){: .btn }

Replays and clips can be **linked or attached** — a ManiaExchange replay page, a YouTube/Twitch clip, or the `.replay.gbx` file itself (attach it to the issue, or add it under `assets/replays/` in a pull request).
"""


def refresh_existing(path: str, m: dict, slug: str) -> bool:
    """Update generated metadata while keeping community front matter and body."""
    try:
        import yaml  # optional dependency, only needed for --refresh
    except ImportError:
        print("ERROR: --refresh needs PyYAML (pip install pyyaml)", file=sys.stderr)
        return False
    text = open(path, encoding="utf-8").read()
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False
    old = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    new_fm = page_front_matter(m, slug)
    new_meta = yaml.safe_load(new_fm.split("---", 2)[1]) or {}
    merged = dict(old)
    merged.update({k: v for k, v in new_meta.items() if k in GENERATED_KEYS})
    for key in ("screenshots", "records"):
        merged[key] = old.get(key) or []
    dumped = yaml.safe_dump(merged, sort_keys=False, allow_unicode=True, default_flow_style=False)
    open(path, "w", encoding="utf-8", newline="\r\n").write("---\n" + dumped + "---" + body)
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--episodes", nargs="+", type=int, default=[106])
    ap.add_argument("--offline", action="store_true", help="use cached data instead of fetching")
    ap.add_argument("--cache", default=os.path.join(ROOT, "data", "maps.json"))
    ap.add_argument("--limit", type=int, default=0, help="only generate the first N maps")
    ap.add_argument("--refresh", action="store_true", help="update metadata of existing pages (needs PyYAML)")
    ap.add_argument("--delay", type=float, default=0.12)
    args = ap.parse_args()

    if args.offline:
        maps = json.load(open(args.cache, encoding="utf-8"))
        print(f"Loaded {len(maps)} maps from cache {args.cache}")
    else:
        maps, seen = [], set()
        for episode in args.episodes:
            page = http_get(FEEDBACK_URL.format(episode=episode))
            found = parse_feedback(page, episode)
            print(f"Episode {episode}: {len(found)} maps")
            for m in found:
                if m["uid"] not in seen:
                    seen.add(m["uid"])
                    maps.append(m)
        cached = {}
        if os.path.exists(args.cache):
            cached = {m["uid"]: m for m in json.load(open(args.cache, encoding="utf-8"))}
        for i, m in enumerate(maps):
            prev = cached.get(m["uid"], {})
            m["mx"] = prev.get("mx") or mx_info(m["uid"])
            if not prev.get("mx"):
                time.sleep(args.delay)
            if (i + 1) % 40 == 0:
                print(f"  MX enrichment {i + 1}/{len(maps)}", flush=True)
        os.makedirs(os.path.dirname(args.cache), exist_ok=True)
        json.dump(maps, open(args.cache, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"Cached source data -> {args.cache}")

    maps = sorted(maps, key=lambda m: (clean_name(m.get("name", "")).lower(), m["uid"]))
    gen_maps = maps[: args.limit] if args.limit else maps

    outdir = os.path.join(ROOT, "docs", "maps")
    os.makedirs(outdir, exist_ok=True)
    on_disk = {f[:-3] for f in os.listdir(outdir) if f.endswith(".md")}
    owned = {}
    for fname in on_disk:
        head = open(os.path.join(outdir, fname + ".md"), encoding="utf-8").read(2000)
        hit = re.search(r'^uid:\s*"([^"]+)"', head, re.M)
        if hit:
            owned[fname] = hit.group(1)
    used, created, updated, skipped = set(), 0, 0, 0
    for m in gen_maps:
        slug = m.get("slug") or slugify(clean_name(m.get("name") or m["uid"]), m["uid"])
        base, n = slug, 2
        while slug in used or (slug in on_disk and owned.get(slug) != m["uid"]):
            slug = f"{base}-{n}"
            n += 1
        used.add(slug)
        m["slug"] = slug
        path = os.path.join(outdir, slug + ".md")
        if os.path.exists(path):
            if args.refresh and refresh_existing(path, m, slug):
                updated += 1
            else:
                skipped += 1
            continue
        content = page_front_matter(m, slug) + PAGE_BODY
        with open(path, "w", encoding="utf-8", newline="\r\n") as fh:
            fh.write(content)
        created += 1

    print(f"Pages: created={created} refreshed={updated} left untouched={skipped} total={len(gen_maps)}")
    with_mx = sum(1 for m in gen_maps if m.get("mx"))
    print(f"MX metadata: {with_mx}/{len(gen_maps)} maps ({len(gen_maps) - with_mx} not indexed on ManiaExchange)")
    os.makedirs(os.path.dirname(args.cache), exist_ok=True)
    json.dump(maps, open(args.cache, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"Slug map saved -> {args.cache}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
