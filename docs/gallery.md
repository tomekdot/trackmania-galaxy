---
layout: default
title: Gallery
nav_order: 5
---

# Gallery

Showcase of Trackmania Galaxy screenshots and map previews. This page uses a tiny JavaScript helper to turn a list of image items into a gallery, similar to the open-source example you shared.

## Map Museum

Use this section as a small map museum for featured tracks, community screenshots, and discovered layouts.

<ul class="md-gallery">
	<li>![Map Museum - Track overview]({{ "/assets/images/logo16x9.jpg" | relative_url }})</li>
	<li>![Map Museum - Canyon section]({{ "/assets/images/logo16x9.jpg" | relative_url }})</li>
	<li>![Map Museum - Desert run]({{ "/assets/images/logo16x9.jpg" | relative_url }})</li>
</ul>

## Example gallery

If you want a second gallery for general screenshots, add another image list like this:

<ul class="md-gallery">
	<li>![Trackmania Galaxy logo]({{ "/assets/images/logo16x9.jpg" | relative_url }})</li>
	<li>![Trackmania Galaxy race shot]({{ "/assets/images/logo16x9.jpg" | relative_url }})</li>
	<li>![Trackmania Galaxy track preview]({{ "/assets/images/logo16x9.jpg" | relative_url }})</li>
</ul>

<script src="{{ '/assets/js/md-gallery.js' | relative_url }}"></script>

You can upload images to `assets/images/` and reference them here. If you want linked thumbnails, wrap the image in a link before the script runs.

## How it works

1. Write a list that contains only images.
2. Add the `md-gallery` class to the list container.
3. Load `assets/js/md-gallery.js` on the page.
4. The script replaces each list with a gallery of `figure` elements.

## Example output

The generated gallery uses semantic HTML, so you can style it with CSS later without changing the Markdown source.
