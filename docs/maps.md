---
layout: default
title: Maps
nav_order: 5
---

# Maps
{: .no_toc }

Per-map pages with a community screenshot gallery and a record history. Every map gets its own page; replays and clips can be linked or attached.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## How it works

- **One page per map** — screenshots, route notes, the record history, a timestamped **map history** (what happened on the map) and community **memories** all live on a dedicated map page under `docs/maps/`.
- **Anyone can contribute** — open a pre-filled issue (no Git knowledge needed) or edit the map page directly on GitHub and send a pull request.
- **Screenshots** are either uploaded to `assets/images/maps/` in a pull request, or linked from an external host (ManiaExchange, Imgur, Discord CDN).
- **Replays and clips: link or attach** — paste a ManiaExchange replay page or a YouTube/Twitch clip, or attach the `.replay.gbx` file to the issue. Files can also be committed under `assets/replays/` in a pull request.
- **Times need a date and a player name** so the history stays verifiable. A replay, a clip or an attached replay file is strongly recommended for record claims.

{: .note }
> This is a static site: there is no upload form or database. Contributions land through GitHub issues and pull requests, and a maintainer merges them into the map page.

---

## Map pages

{% assign map_pages = site.html_pages | where_exp: "p", "p.map == true" | sort: "title" %}
{% assign pursuit_maps = map_pages | where: "mode", "Pursuit" %}
{% assign goalhunt_maps = map_pages | where: "mode", "Goal Hunt" %}
{% assign hunters_maps = map_pages | where: "mode", "Hunters" %}
{% if map_pages.size > 0 %}
**{{ map_pages.size }} maps** — Pursuit {{ pursuit_maps.size }} · Goal Hunt {{ goalhunt_maps.size }} · Hunters {{ hunters_maps.size }} · unclassified {{ map_pages.size | minus: pursuit_maps.size | minus: goalhunt_maps.size | minus: hunters_maps.size }}

<style>
.map-tools { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin: 12px 0; }
.map-tools input[type="search"] { padding: 6px 10px; border-radius: 6px; border: 1px solid rgba(167,139,250,.35); background: rgba(255,255,255,.06); color: inherit; min-width: 220px; }
.map-filter { padding: 5px 12px; border-radius: 999px; border: 1px solid rgba(167,139,250,.35); background: transparent; color: inherit; cursor: pointer; font-size: .85rem; }
.map-filter.active { background: linear-gradient(135deg,#7c3aed,#4f46e5); border-color: transparent; color: #fff; }
.map-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 14px; margin-top: 14px; }
.map-card { display: flex; flex-direction: column; gap: 4px; padding: 8px; border-radius: 10px; border: 1px solid rgba(167,139,250,.18); background: rgba(16,18,40,.55); text-decoration: none !important; color: inherit; }
.map-card:hover { border-color: rgba(125,211,252,.6); box-shadow: 0 0 14px rgba(124,58,237,.25); }
.map-card img { width: 100%; aspect-ratio: 16/9; object-fit: cover; border-radius: 6px; background: rgba(255,255,255,.05); }
.map-card-title { font-weight: 600; font-size: .9rem; line-height: 1.25; }
.map-card-meta { font-size: .75rem; opacity: .75; }
.map-card-counts { font-size: .72rem; opacity: .6; }
.map-empty { display: none; margin-top: 12px; }
</style>

<div class="map-tools">
  <input type="search" id="map-search" placeholder="Filter by name or mapper…" aria-label="Filter maps">
  <button class="map-filter active" data-mode="all">All</button>
  <button class="map-filter" data-mode="Pursuit">Pursuit</button>
  <button class="map-filter" data-mode="Goal Hunt">Goal Hunt</button>
  <button class="map-filter" data-mode="Hunters">Hunters</button>
  <button class="map-filter" data-mode="unclassified">Unclassified</button>
  <select id="map-env" class="map-filter" aria-label="Filter by environment">
    <option value="all">All environments</option>
    <option>Canyon</option><option>Stadium</option><option>Valley</option><option>Lagoon</option><option value="unknown">Unknown</option>
  </select>
  <span id="map-count" class="map-card-meta"></span>
</div>

<div class="map-grid" id="map-grid">
{% for p in map_pages %}
  <a class="map-card" href="{{ p.url | relative_url }}" data-mode="{{ p.mode | default: 'unclassified' }}" data-env="{{ p.environment | default: 'unknown' }}" data-text="{{ p.map_name | default: p.title | escape | downcase }} {{ p.mapper | default: '' | escape | downcase }}">
    <img loading="lazy" src="{{ p.thumbnail }}" alt="{{ p.map_name | default: p.title | escape }} thumbnail">
    <span class="map-card-title">{{ p.map_name | default: p.title | escape }}</span>
    <span class="map-card-meta">{{ p.mode | default: "unclassified" }} · {{ p.environment | default: "unknown" }}</span>
    <span class="map-card-meta">{{ p.mapper | default: "unknown mapper" | escape }}</span>
    <span class="map-card-counts">{{ p.records.size | default: 0 }} records · {{ p.screenshots.size | default: 0 }} screenshots · {{ p.events.size | default: 0 }} events</span>
  </a>
{% endfor %}
</div>
<p class="map-empty" id="map-empty">No maps match this filter.</p>

<script>
(function () {
  var cards = Array.prototype.slice.call(document.querySelectorAll('#map-grid .map-card'));
  var mode = 'all', env = 'all', q = '';
  var count = document.getElementById('map-count');
  var empty = document.getElementById('map-empty');
  function apply() {
    var shown = 0;
    cards.forEach(function (c) {
      var ok = (mode === 'all' || c.dataset.mode === mode)
            && (env === 'all' || c.dataset.env === env)
            && (!q || c.dataset.text.indexOf(q) !== -1);
      c.style.display = ok ? '' : 'none';
      if (ok) shown++;
    });
    count.textContent = shown + ' / ' + cards.length + ' maps';
    empty.style.display = shown ? 'none' : 'block';
  }
  document.querySelectorAll('.map-filter[data-mode]').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.map-filter[data-mode]').forEach(function (x) { x.classList.remove('active'); });
      b.classList.add('active'); mode = b.dataset.mode; apply();
    });
  });
  document.getElementById('map-env').addEventListener('change', function (e) { env = e.target.value; apply(); });
  document.getElementById('map-search').addEventListener('input', function (e) { q = e.target.value.trim().toLowerCase(); apply(); });
  apply();
})();
</script>

<details markdown="1">
<summary>Table view (sortable columns, copy-friendly)</summary>

| Map | Mode | Environment | Mapper | Records | Screenshots |
|-----|------|-------------|--------|---------|-------------|
{% for p in map_pages %}| [{{ p.map_name | default: p.title | escape }}]({{ p.url | relative_url }}) | {{ p.mode | default: "—" }} | {{ p.environment | default: "—" }} | {{ p.mapper | default: "—" | escape }} | {{ p.records.size | default: 0 }} | {{ p.screenshots.size | default: 0 }} |
{% endfor %}

</details>

{: .note }
> Each card opens a dedicated map page with its description, screenshots, record history, timestamped map history and memories. The site search (shortcut `k`) also covers every map page.
{% else %}
{: .highlight }
> No map pages yet. Create the first one with the button below — the template takes about two minutes to fill in.
{% endif %}

---

## How the map list is generated

Map pages are generated from two public sources, then enriched by the community:

1. **ManiaPlanet Feedback** — the official episode page for the Pursuit Multienvironment playlist (`votes/display/106`) provides the map names, UIDs, thumbnails and community ratings.
2. **ManiaExchange API** — adds mapper, environment, map type, upload date and the MX map link. Maps that are not indexed on MX keep their name, thumbnail and ratings, with the remaining fields marked unknown.

```bash
python3 scripts/generate_map_pages.py            # fetch sources, create missing pages
python3 scripts/generate_map_pages.py --offline  # regenerate from data/maps.json
```

- Source data and the UID → page slug mapping are cached in `data/maps.json`.
- A re-run **never overwrites existing pages**: community screenshots, records and descriptions stay intact. New maps from the playlist get new pages.
- `--refresh` updates only the generated metadata of existing pages (requires PyYAML) and still preserves community content.

{: .warning }
> Coverage: the pages currently mirror the official feedback episode (262 maps). If the server playlist contains maps that are missing here, report them with the issue form — a maintainer adds them to the cache and regenerates.

---

## Add a screenshot or a record

[Submit a screenshot or record](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-record.yml&labels=map-record&title=%5BMap%5D%20%3Cmap%20name%3E){: .btn .btn-primary }
[Submit map history or a memory](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-history.yml&labels=map-history&title=%5BMap%20history%5D%20%3Cmap%20name%3E){: .btn }
[Open the map feedback form](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-feedback.yml&labels=map-feedback&title=%5BMap%5D%20%3Cmap%20name%3E){: .btn }

The form asks for:

1. **Map name** (required) — the exact in-game name.
2. **What you are adding** — screenshot, record, or both.
3. **Player name and time** — for records, in `m:ss.mmm` format (for example `0:42.123`).
4. **Date** — when the run or screenshot happened (`YYYY-MM-DD`).
5. **Links or files** — screenshot URL, replay URL and/or a video clip URL. You can also drag a `.replay.gbx` replay or a screenshot straight into the issue; GitHub hosts the attachment.

A maintainer then adds the entry to the map page and it goes live with the next deploy.

---

## Create a new map page

1. Copy [`docs/maps/TEMPLATE.md`](https://github.com/tomekdot/trackmania-galaxy/blob/main/docs/maps/TEMPLATE.md) into a new file `docs/maps/<map-name>.md` (lowercase, hyphens instead of spaces).
2. Fill in the front matter: `map_name`, `mode`, `environment`, `mapper`, `mx_url`.
3. Add `screenshots:`, `records:`, `events:` (timestamped map history) and `memories:` entries as YAML — the page renders the gallery, record table, timeline and memories automatically.
4. Keep `map: true` so the page is listed above, and `parent: Maps` for the breadcrumb.
5. Open a pull request. The map appears in the table as soon as it is merged.

[Create a map page on GitHub](https://github.com/tomekdot/trackmania-galaxy/new/main/docs/maps?filename=docs/maps/new-map.md&value=Copy%20the%20contents%20of%20docs/maps/TEMPLATE.md%20here){: .btn }

{: .warning }
> Keep uploads small: replay files (`.replay.gbx`, usually tens of kB) belong in `assets/replays/`, screenshots (under ~1 MB, prefer WebP/JPG) in `assets/images/maps/`. Long videos stay as links (YouTube/Twitch) — never commit video files.

---

## Related pages

- [Gallery](gallery) — title pack screenshots and UI examples.
- [Gameplay Guides](gameplay) — mode rules and map-building guidelines.
- [Contributing](contributing) — general wiki contribution guide.
