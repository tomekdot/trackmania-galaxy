---
title: "Contributing"
description: "How to contribute to the Trackmania Galaxy wiki — edits, screenshots, records and guides."
sidebar:
  order: 9
---

This wiki is maintained by the community. Everyone is welcome to contribute!

## How to Contribute

The Trackmania Galaxy Wiki is open source and hosted on GitHub. There are several ways you can help:

- **Fix typos or broken links** — small edits are welcome!
- **Add new screenshots** — enrich pages with visuals
- **Write new guides** — share your expertise on game modes, techniques, or map making
- **Update existing pages** — keep information current with the latest title updates
- **Translate content** — help make the wiki accessible to more players

### Editing Existing Pages

1. Navigate to the page on the wiki that you want to edit.
2. Open the [GitHub repository](https://github.com/tomekdot/trackmania-galaxy) in a new tab.
3. Browse to the corresponding file under `src/content/docs/docs/` (matching the page URL).
4. Click the pencil icon in GitHub to edit the file, make your changes, and add a clear commit message.
5. Submit a **Pull Request** with a clear description of your changes.

### Adding New Pages

1. Fork the [repository](https://github.com/tomekdot/trackmania-galaxy) on GitHub.
2. Create a new `.md` file in the `src/content/docs/docs/` folder.
3. Add the required **front matter** at the top of the file:

```yaml
---
title: Your Page Title
description: A short summary for search engines and link previews.
sidebar:
  order: 10
---
```

4. Write your content in Markdown. Starlight renders a table of contents automatically.
5. Submit a Pull Request.

### Map screenshots and records

Map data lives in `src/data/maps.json` and is data-driven: `screenshots` and `records` entries render automatically on each map's gallery page.

Two ways to contribute:

1. **Issue form (easiest)** — use the [Map screenshot or record](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-record.yml&labels=map-record) or [Map history or memory](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-history.yml&labels=map-history) template. A maintainer adds the entry to the map data.
2. **Pull request** — edit the map's entry in `src/data/maps.json`, add a `screenshots:` or `records:` item, and open a PR.

Rules:

- Replays can be **linked or attached** (ManiaExchange page, video clip, or the `.replay.gbx` file). Committed replay files go to `assets/replays/`; short video clips can go to `public/replays/` so they are published with the site.
- **Prefer links for videos.** Paste a URL and it plays inline on the map page. Supported inline sources: YouTube, Medal.tv, Twitch clips/VODs, Streamable, Discord CDN attachments (`cdn.discordapp.com`, `media.discordapp.net`), Google Drive, Dropbox, MEGA, and any direct `.mp4`/`.webm`/`.mov` URL. Anything else stays a plain clickable link.
- Medal.tv works with `medal.tv/clips/<id>` or `medal.tv/games/<game>/clips/<id>`; Streamable works with `streamable.com/<id>`, `/e/<id>` or `/o/<id>`. Both play inline — no upload to this repo is needed.
- A short clip may be committed to `public/replays/` and linked with its absolute site URL (e.g. `https://tomekdot.github.io/trackmania-galaxy/replays/clip.mp4`). Keep each file well under 100 MB and the whole published site under 1 GB; longer or numerous videos belong on a video host.
- Screenshots go to the images folder in a PR, or stay as external URLs.
- Records need a player name, a time in `m:ss.mmm` format and a date; a replay **or clip** link (or an attached replay file) makes them verifiable.

---

## Running Locally

To preview the wiki on your local machine:

### Prerequisites

- [Node.js](https://nodejs.org/) 22 or newer

### Steps

```bash
# Clone the repository
git clone https://github.com/tomekdot/trackmania-galaxy.git
cd trackmania-galaxy

# Install dependencies
npm install

# Start the local dev server
npm run dev

# Open in your browser
# http://localhost:4321/trackmania-galaxy/
```

To produce the production build (the same one GitHub Pages serves):

```bash
npm run build     # outputs to dist/
npm run preview   # serve the built site locally
```

---

## Style Guide

When writing wiki pages, please follow these guidelines:

- **Be concise** — Keep sentences short and focused.
- **Use headings** — Structure content with `##` and `###` headings.
- **Link related pages** — Cross-reference other relevant wiki pages with relative links.
- **Cite sources** — Link to official ManiaPlanet resources where applicable.
- **Use callouts** — Starlight asides: `:::note`, `:::tip`, `:::caution`, `:::danger` for important information.
- **Images** — Use `![Description](../../../assets/images/image.jpg)` for screenshots.
- **Be neutral** — Present facts objectively; avoid opinions or bias.
- **Respect others** — No offensive language, harassment, or personal attacks.

:::note
This wiki uses [Starlight](https://starlight.astro.build/) (Astro). Refer to its documentation for advanced formatting options like asides, cards, tabs and search configuration.
:::

---

## Code of Conduct

All contributors are expected to be respectful and constructive. Harmful, misleading, or disruptive contributions will be removed.

:::tip
Thank you for helping make the Trackmania Galaxy Wiki better for everyone!
:::
