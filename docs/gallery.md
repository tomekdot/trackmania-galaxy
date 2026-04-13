---
layout: default
title: Gallery
nav_order: 5
---

# Gallery

Showcase of Trackmania Galaxy screenshots and map previews. This page uses a tiny JavaScript helper to turn a Markdown image list into a gallery, similar to the open-source example you shared.

## Example gallery

Create a simple Markdown list like this:

* ![Trackmania Galaxy logo]({{ "/assets/images/logo16x9.jpg" | relative_url }})
* ![Trackmania Galaxy track preview]({{ "/assets/images/logo16x9.jpg" | relative_url }})
* ![Trackmania Galaxy race shot]({{ "/assets/images/logo16x9.jpg" | relative_url }})

{: .md-gallery }

<script src="{{ '/assets/js/md-gallery.js' | relative_url }}"></script>

You can upload images to `assets/images/` and reference them here. If you want linked thumbnails, wrap the image in a link before the script runs.

## How it works

1. Write a Markdown list with only images.
2. Add the `.md-gallery` class to that list.
3. Load `assets/js/md-gallery.js` on the page.
4. The script replaces the list with a gallery of `figure` elements.

## Example output

The generated gallery uses semantic HTML, so you can style it with CSS later without changing the Markdown source.
