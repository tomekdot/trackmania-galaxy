---
layout: default
title: Gallery
nav_order: 5
---

# Gallery

Showcase of Trackmania Galaxy screenshots and map previews. This page uses a tiny JavaScript helper to turn a Markdown list of images into a gallery.

## Map Museum

Use this section for map folders, historical screenshots, and track archives.

### Canyon maps

* ![Canyon map - overview]({{ "/assets/images/maps/canyon/overview.svg" | relative_url }})
* ![Canyon map - start zone]({{ "/assets/images/maps/canyon/start-zone.svg" | relative_url }})
* ![Canyon map - finish line]({{ "/assets/images/maps/canyon/finish-line.svg" | relative_url }})

{: .md-gallery }

### Desert maps

* ![Desert map - overview]({{ "/assets/images/maps/desert/overview.svg" | relative_url }})
* ![Desert map - wall ride]({{ "/assets/images/maps/desert/wall-ride.svg" | relative_url }})
* ![Desert map - checkpoint]({{ "/assets/images/maps/desert/checkpoint.svg" | relative_url }})

{: .md-gallery }

## Example gallery

If you want a second gallery for general screenshots, add another list like this:

* ![Trackmania Galaxy logo]({{ "/assets/images/logo16x9.jpg" | relative_url }})
* ![Trackmania Galaxy race shot]({{ "/assets/images/logo16x9.jpg" | relative_url }})
* ![Trackmania Galaxy track preview]({{ "/assets/images/logo16x9.jpg" | relative_url }})

{: .md-gallery }

<script src="{{ '/assets/js/md-gallery.js' | relative_url }}"></script>

You can upload images to `assets/images/` and reference them here. If you want linked thumbnails, wrap the image in a link before the script runs.

## How it works

1. Write a list that contains only images.
2. Add the `md-gallery` class to the list container.
3. Load `assets/js/md-gallery.js` on the page.
4. The script replaces each list with a gallery of `figure` elements.

## Example output

The generated gallery uses semantic HTML, so you can style it with CSS later without changing the Markdown source.
