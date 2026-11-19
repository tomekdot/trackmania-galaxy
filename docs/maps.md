---
layout: default
title: Maps
nav_order: 5
---

# Maps
{: .no_toc }

Per-map pages with a community screenshot gallery and a record history. Every map gets its own page; replays are shared as links only.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## How it works

- **One page per map** — screenshots, route notes and the record history live together on a dedicated map page under `docs/maps/`.
- **Anyone can contribute** — open a pre-filled issue (no Git knowledge needed) or edit the map page directly on GitHub and send a pull request.
- **Screenshots** are either uploaded to `assets/images/maps/` in a pull request, or linked from an external host (ManiaExchange, Imgur, Discord CDN).
- **Replays are links only** — paste a ManiaExchange replay page or a file-host link. Replay files are never committed to this repository.
- **Times need a date and a player name** so the history stays verifiable. A replay or video link is strongly recommended for record claims.

{: .note }
> This is a static site: there is no upload form or database. Contributions land through GitHub issues and pull requests, and a maintainer merges them into the map page.

---

## Map pages

{% assign map_pages = site.html_pages | where_exp: "p", "p.map == true" | sort: "title" %}
{% if map_pages.size > 0 %}
| Map | Mode | Environment | Records | Screenshots |
|-----|------|-------------|---------|-------------|
{% for p in map_pages %}| [{{ p.map_name | default: p.title }}]({{ p.url | relative_url }}) | {{ p.mode | default: "—" }} | {{ p.environment | default: "—" }} | {{ p.records.size | default: 0 }} | {{ p.screenshots.size | default: 0 }} |
{% endfor %}
{% else %}
{: .highlight }
> No map pages yet. Create the first one with the button below — the template takes about two minutes to fill in.
{% endif %}

---

## Add a screenshot or a record

[Submit a screenshot or record](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-record.yml&labels=map-record&title=%5BMap%5D%20%3Cmap%20name%3E){: .btn .btn-primary }
[Open the map feedback form](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-feedback.yml&labels=map-feedback&title=%5BMap%5D%20%3Cmap%20name%3E){: .btn }

The form asks for:

1. **Map name** (required) — the exact in-game name.
2. **What you are adding** — screenshot, record, or both.
3. **Player name and time** — for records, in `m:ss.mmm` format (for example `0:42.123`).
4. **Date** — when the run or screenshot happened (`YYYY-MM-DD`).
5. **Links** — screenshot URL and replay URL. Links only, no file uploads.

A maintainer then adds the entry to the map page and it goes live with the next deploy.

---

## Create a new map page

1. Copy [`docs/maps/TEMPLATE.md`](https://github.com/tomekdot/trackmania-galaxy/blob/main/docs/maps/TEMPLATE.md) into a new file `docs/maps/<map-name>.md` (lowercase, hyphens instead of spaces).
2. Fill in the front matter: `map_name`, `mode`, `environment`, `mapper`, `mx_url`.
3. Add screenshots and records as YAML entries — the page renders the gallery and the record table automatically.
4. Keep `map: true` so the page is listed above, and `parent: Maps` for the breadcrumb.
5. Open a pull request. The map appears in the table as soon as it is merged.

[Create a map page on GitHub](https://github.com/tomekdot/trackmania-galaxy/new/main/docs/maps?filename=docs/maps/new-map.md&value=Copy%20the%20contents%20of%20docs/maps/TEMPLATE.md%20here){: .btn }

{: .warning }
> Do not commit replay files (`.replay.gbx`) or other binaries. Link to ManiaExchange or a file host instead. Keep screenshots reasonably sized (under ~1 MB each) and prefer WebP/JPG for photos.

---

## Related pages

- [Gallery](gallery) — title pack screenshots and UI examples.
- [Gameplay Guides](gameplay) — mode rules and map-building guidelines.
- [Contributing](contributing) — general wiki contribution guide.
