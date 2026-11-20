---
title: "Maps & Records"
description: "How per-map pages, community screenshots and record histories work in Trackmania Galaxy."
sidebar:
  order: 5
---

Per-map pages with a community screenshot gallery and a record history. Every map gets its own page; replays and clips can be linked or attached.

:::tip[Open the map gallery]
Browse all **262 maps** with thumbnails, ratings, search and environment filters in the **[Map Gallery](../../)** — click any map for its dedicated page.
:::

## How it works

- **One page per map** — screenshots, route notes, the record history, a timestamped **map history** (what happened on the map) and community **memories** all live on a dedicated map page.
- **Anyone can contribute** — open a pre-filled issue (no Git knowledge needed) or edit the map data directly on GitHub and send a pull request.
- **Screenshots** are either uploaded in a pull request, or linked from an external host (ManiaExchange, Imgur, Discord CDN).
- **Replays and clips: link or attach** — paste a ManiaExchange replay page or a YouTube/Twitch clip, or attach the `.replay.gbx` file to the issue.
- **Times need a date and a player name** so the history stays verifiable. A replay, a clip or an attached replay file is strongly recommended for record claims.

:::note
This is a static site: there is no upload form or database. Contributions land through GitHub issues and pull requests, and a maintainer merges them into the map data.
:::

---

## How the map list is generated

Map pages are generated from two public sources, then enriched by the community:

1. **ManiaPlanet Feedback** — the official episode page for the Pursuit Multienvironment playlist (`votes/display/106`) provides the map names, UIDs, thumbnails and community ratings.
2. **ManiaExchange API** — adds mapper, environment, map type, upload date and the MX map link. Maps that are not indexed on MX keep their name, thumbnail and ratings, with the remaining fields marked unknown.

- Source data and the UID → page slug mapping are cached in `src/data/maps.json`.
- A re-run **never overwrites community content**: screenshots, records and descriptions stay intact. New maps from the playlist get new pages.

:::caution
Coverage: the pages currently mirror the official feedback episode (262 maps). If the server playlist contains maps that are missing here, report them with the issue form — a maintainer adds them to the cache and regenerates.
:::

---

## Add a screenshot or a record

- [Submit a screenshot or record](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-record.yml&labels=map-record&title=%5BMap%5D%20%3Cmap%20name%3E)
- [Submit map history or a memory](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-history.yml&labels=map-history&title=%5BMap%20history%5D%20%3Cmap%20name%3E)
- [Open the map feedback form](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-feedback.yml&labels=map-feedback&title=%5BMap%5D%20%3Cmap%20name%3E)

The form asks for:

1. **Map name** (required) — the exact in-game name.
2. **What you are adding** — screenshot, record, or both.
3. **Player name and time** — for records, in `m:ss.mmm` format (for example `0:42.123`).
4. **Date** — when the run or screenshot happened (`YYYY-MM-DD`).
5. **Links or files** — screenshot URL, replay URL and/or a video clip URL. You can also drag a `.replay.gbx` replay or a screenshot straight into the issue; GitHub hosts the attachment.

A maintainer then adds the entry to the map data and it goes live with the next deploy.

:::caution
Keep uploads small: replay files (`.replay.gbx`, usually tens of kB) belong in `assets/replays/`, screenshots (under ~1 MB, prefer WebP/JPG) in the images folder. Keep long videos as links (YouTube/Twitch/Streamable); a short clip (well under 100 MB) can be committed to `public/replays/` and linked with an absolute site URL.
:::

---

## Related pages

- [Gallery](../gallery/) — title pack screenshots and UI examples.
- [Gameplay Guides](../gameplay/) — mode rules and map-building guidelines.
- [Contributing](../contributing/) — general wiki contribution guide.
