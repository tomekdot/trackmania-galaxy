---
layout: default
title: Contributing
nav_order: 9
---

# Contributing to the Wiki
{: .no_toc }

This wiki is maintained by the community. Everyone is welcome to contribute!
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

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
3. In GitHub, browse to the corresponding file under the `docs/` directory (matching the page URL).
4. Click the pencil icon in GitHub to edit the file, make your changes, and add a clear commit message.
5. Submit a **Pull Request** with a clear description of your changes.

### Adding New Pages

1. Fork the [repository](https://github.com/tomekdot/trackmania-galaxy) on GitHub.
2. Create a new `.md` file in the `docs/` folder.
3. Add the required **front matter** at the top of the file:

```yaml
---
layout: default
title: Your Page Title
nav_order: 7
---
```

4. Write your content in Markdown.
5. Submit a Pull Request.

### Map screenshots and records

Map pages live in `docs/maps/` and are data-driven: screenshots and records are YAML entries in the page's front matter, and the gallery plus record table render automatically.

Two ways to contribute:

1. **Issue form (easiest)** — use the [Map screenshot or record](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-record.yml&labels=map-record) template. A maintainer adds the entry to the map page.
2. **Pull request** — edit the map page on GitHub (every page has an "Edit this page on GitHub" link), add a `screenshots:` or `records:` entry, and open a PR.

Rules:

- Replays can be **linked or attached** (ManiaExchange page, video clip, or the `.replay.gbx` file). Committed replay files go to `assets/replays/`; videos stay as links.
- Screenshots go to `assets/images/maps/` in a PR, or stay as external URLs.
- Records need a player name, a time in `m:ss.mmm` format and a date; a replay **or clip** link (or an attached replay file) makes them verifiable.
- New map pages start from [`docs/maps/TEMPLATE.md`](https://github.com/tomekdot/trackmania-galaxy/blob/main/docs/maps/TEMPLATE.md) and must keep `map: true` to be listed on the [Maps](maps) index.

---

## Running Locally

To preview the wiki on your local machine:

### Prerequisites

- [Ruby](https://www.ruby-lang.org/) 3.0+
- [Bundler](https://bundler.io/)

### Steps

```bash
# Clone the repository
git clone https://github.com/tomekdot/trackmania-galaxy.git
cd trackmania-galaxy.github.io

# Install dependencies
bundle install

# Start the local server
bundle exec jekyll serve

# Open in your browser
# http://localhost:4000
```

---

## Style Guide

When writing wiki pages, please follow these guidelines:

- **Be concise** — Keep sentences short and focused.
- **Use headings** — Structure content with `##` and `###` headings.
- **Add a TOC** — For longer pages, include a table of contents.
- **Link related pages** — Cross-reference other relevant wiki pages.
- **Cite sources** — Link to official ManiaPlanet resources where applicable.
- **Use callouts** — Use `{: .note }`, `{: .warning }`, etc. for important information.
- **Images** — Use `![Description](../assets/images/image.jpg)` for screenshots.
- **Be neutral** — Present facts objectively; avoid opinions or bias.
- **Respect others** — No offensive language, harassment, or personal attacks.

{: .note }
> This wiki uses the [Just the Docs](https://just-the-docs.com/) theme. Refer to their documentation for advanced formatting options like tables, callouts, and search configuration.

---

## Code of Conduct

All contributors are expected to be respectful and constructive. Harmful, misleading, or disruptive contributions will be removed.

{: .highlight }
> Thank you for helping make the Trackmania Galaxy Wiki better for everyone!
