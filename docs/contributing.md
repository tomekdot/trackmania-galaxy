---
layout: default
title: Contributing
nav_order: 6
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

### Editing Existing Pages

1. Navigate to the page on the wiki that you want to edit.
2. Open the [GitHub repository](https://github.com/tomekdot/trackmania-galaxy.github.io) in a new tab.
3. In GitHub, browse to the corresponding file under the `docs/` directory (matching the page URL).
4. Click the pencil icon in GitHub to edit the file, make your changes, and add a clear commit message.
5. Submit a **Pull Request** with a clear description of your changes.

### Adding New Pages

1. Fork the [repository](https://github.com/tomekdot/trackmania-galaxy.github.io) on GitHub.
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

## Running Locally

To preview the wiki on your local machine:

### Prerequisites

- [Ruby](https://www.ruby-lang.org/) 3.0+
- [Bundler](https://bundler.io/)

### Steps

```bash
# Clone the repository
git clone https://github.com/tomekdot/trackmania-galaxy.github.io.git
cd trackmania-galaxy.github.io

# Install dependencies
bundle install

# Start the local server
bundle exec jekyll serve

# Open in your browser
# http://localhost:4000
```

## Style Guide

When writing wiki pages, please follow these guidelines:

- **Be concise** — Keep sentences short and focused.
- **Use headings** — Structure content with `##` and `###` headings.
- **Add a TOC** — For longer pages, include a table of contents.
- **Link related pages** — Cross-reference other relevant wiki pages.
- **Cite sources** — Link to official Trackmania resources where applicable.
- **Use callouts** — Use `{: .note }`, `{: .warning }`, etc. for important information.

## Code of Conduct

All contributors are expected to be respectful and constructive. Harmful, misleading, or disruptive contributions will be removed.

{: .highlight }
> Thank you for helping make the Trackmania Galaxy Wiki better for everyone!
