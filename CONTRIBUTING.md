# Contributing to ManiaPlanet Wiki

Thank you for your interest in contributing to the ManiaPlanet Wiki! This project is community-driven and open-source.

## How to edit pages

1. Log in to your GitHub account.
2. Navigate to the page or article you want to edit.
3. Click the **pencil icon** or the **"Edit on GitHub"** button in the top right corner to open the GitHub web editor.
4. Make your changes in Markdown (`.md`) format.
5. At the bottom of the page, add a short commit message explaining your changes.
6. Click **"Propose changes"** to create a Pull Request. Once approved and merged, your changes will be live!

## How to add images and galleries

We encourage you to add images such as screenshots to enrich the documentation.

### Step 1: Upload the image to the repository
1. Go to the `assets/images/` folder on GitHub.
2. Click **"Add file"** -> **"Upload files"** in the top right corner.
3. Select your images (`.jpg`, `.png`, `.gif`) and commit the changes to create a Pull Request.

### Step 2: Add the image to an article
1. Open the `.md` file where you want the image to appear and click edit.
2. Use this Markdown syntax:
`![Image description](../assets/images/your_image_name.jpg)`

### Creating a Gallery
If you want to display multiple images side by side (e.g. for track screenshots), paste this HTML code directly into your Markdown file:

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
Every time you merge a Pull Request, GitHub Actions will automatically rebuild the pages behind the scenes. Updates usually appear online within 1-2 minutes.

Happy editing!
