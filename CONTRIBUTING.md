# Contributing to Trackmania Galaxy Wiki

Thank you for your interest in contributing to the Trackmania Galaxy Wiki! This project is community-driven, open-source, and built to be edited directly from GitHub.

## How to edit pages

1. Log in to your GitHub account.
2. Navigate to the page or article you want to edit.
3. Click the **pencil icon** or the **"Edit on GitHub"** button in the top right corner to open the GitHub web editor.
4. Make your changes in Markdown (`.md`) format.
5. At the bottom of the page, add a short commit message explaining your changes.
6. Click **"Propose changes"** to create a Pull Request. Once approved and merged, your changes will be live!

## How to add images and galleries

We encourage you to add images such as screenshots to enrich the documentation and make pages more useful for the community.

### Step 1: Upload the image to the repository
1. Go to the `assets/images/` folder on GitHub.
2. Click **"Add file"** -> **"Upload files"** in the top right corner.
3. Select your images (`.jpg`, `.png`, `.gif`) and commit the changes to create a Pull Request.
4. Use short, descriptive file names like `track-preview.jpg` or `logo-banner.png`.

### Step 2: Add the image to an article
1. Open the `.md` file where you want the image to appear and click edit.
2. Use this Markdown syntax:
`![Image description](../assets/images/your_image_name.jpg)`

### Step 3: Create a gallery
If you want a gallery on the wiki, open [docs/gallery.md](docs/gallery.md) and use a Markdown list with images like this:

```md
* ![Track preview]({{ "/assets/images/track-preview.jpg" | relative_url }})
* ![Track detail]({{ "/assets/images/track-detail.jpg" | relative_url }})
* ![Race shot]({{ "/assets/images/race-shot.jpg" | relative_url }})
```

Then add the `.md-gallery` class and load the helper script:

```html
{: .md-gallery }
<script src="{{ '/assets/js/md-gallery.js' | relative_url }}"></script>
```

### Alternative gallery layout
If you prefer a simple static gallery instead of the helper script, you can still paste raw HTML into a Markdown file:

```html
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
  <img src="../assets/images/image1.jpg" alt="Description" style="width: 30%; border-radius: 5px;">
  <img src="../assets/images/image2.jpg" alt="Description" style="width: 30%; border-radius: 5px;">
  <img src="../assets/images/image3.jpg" alt="Description" style="width: 30%; border-radius: 5px;">
</div>
```

## Formatting Guidelines
- Our site is built using Markdown (`.md`) and the Just The Docs theme.
- When creating a completely new page, remember to include the "Front Matter" at the very top of the file:

```yml
---
layout: default
title: Your Page Title
nav_order: 10
---
```

## Automated Builds
Every time you push to `main` or merge a Pull Request, GitHub Actions will automatically rebuild the pages behind the scenes. Updates usually appear online within 1-2 minutes.

## Where to ask for help

If you are not sure how a page should be structured, open an Issue or start a Discussion on GitHub before editing.

Happy editing!
