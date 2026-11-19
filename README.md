# Trackmania Galaxy

[![Deploy to GitHub Pages](https://github.com/tomekdot/trackmania-galaxy/actions/workflows/deploy.yml/badge.svg)](https://github.com/tomekdot/trackmania-galaxy/actions/workflows/deploy.yml)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

**Live site:** https://tomekdot.github.io/trackmania-galaxy/

Community wiki for the **TrackMania² Galaxy** title pack — a galaxy-styled map gallery (262 Pursuit & Goal Hunt maps with thumbnails, ratings, search and filters) plus documentation (guides, title-update history, contributing).

Built with **Astro 7 + Starlight**, hosted free on GitHub Pages. This repository was migrated from the previous Jekyll / Just the Docs site; the full Jekyll version is preserved in git history (tag `jekyll-final`).

## Stack

- **Astro 7** (static output) + **Starlight** for the docs section (`/docs/`)
- Custom galaxy pages: map gallery (`/`) and per-map pages (`/maps/<slug>/`), styled after the in-game TM² Galaxy menu and map-voting screen
- **Pagefind** full-text search (built automatically), sitemap, Open Graph / Twitter cards and JSON-LD structured data
- Map data: `src/data/maps.json` — derived from ManiaPlanet Feedback + ManiaExchange; community screenshots/records merged on top
- Docs content: `src/content/docs/docs/*.md`; images in `src/assets/images/`

## Project structure

```
src/
  pages/            custom galaxy pages (index.astro, maps/[slug].astro)
  components/       Layout.astro (SEO head, theme)
  content/docs/     Starlight wiki pages (Markdown)
  data/maps.json    map data consumed by the gallery
  assets/images/    screenshots & logo (optimized by Astro)
  styles/           galaxy.css, starlight.css
public/             robots.txt, favicon.svg, og-default.jpg
data/maps.json      original source cache (ManiaExchange + Feedback)
scripts/            legacy map-page generator (Jekyll era, kept for provenance)
.github/
  workflows/deploy.yml   Astro build → GitHub Pages
  ISSUE_TEMPLATE/        map-record / map-history / map-feedback forms
```

## Develop

Requires **Node.js 22+**.

```bash
npm install
npm run dev       # http://localhost:4321/trackmania-galaxy/
npm run build     # static site into dist/
npm run preview   # serve the production build
```

## Deploy

Every push to `main` triggers `.github/workflows/deploy.yml`, which builds with [`withastro/action`](https://github.com/withastro/action) and publishes to GitHub Pages (Pages source: **GitHub Actions**). No server, no database, nothing to pay for.

## Contributing

Anyone can add a map screenshot or record — open a pre-filled [issue](https://github.com/tomekdot/trackmania-galaxy/issues/new/choose) (no Git knowledge needed) or edit the map data and send a pull request. See the [Contributing guide](https://tomekdot.github.io/trackmania-galaxy/docs/contributing/) on the live site.

## License

Content: **CC BY-SA 4.0** (community wiki). Not affiliated with Ubisoft or Nadeo.
