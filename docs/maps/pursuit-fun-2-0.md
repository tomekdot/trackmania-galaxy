---
layout: default
title: "Pursuit Fun 2,0"
parent: Maps
nav_exclude: true
map: true
uid: "Ndb1KtLeK6CaIHEJaU4GRV_fwIk"
map_name: "Pursuit Fun 2,0"
mode: "Pursuit"
map_type: "PursuitArena"
environment: "Stadium"
mapper: "rosschiko"
mx_url: "https://tm.mania.exchange/maps/242164"
mx_id: 242164
thumbnail: "https://files-v4.live.maniaplanet.com/maps/556c900e3f/Ndb1KtLeK6CaIHEJaU4GRV_fwIk.jpg"
uploaded: "2024-02-14"
titlepack: "TMStadium"
feedback:
  yn_rating: null
  yn_votes: null
  stars_avg: 3.9
  stars_total: 83

# Community content below — a generator re-run never overwrites these.
screenshots: []
records: []
---
# {{ page.map_name | escape }}
{: .no_toc }

{% if page.thumbnail != "" %}
<img src="{{ page.thumbnail }}" alt="{{ page.map_name | escape }} thumbnail" style="max-width: 420px; width: 100%; border-radius: 8px;">
{% endif %}

| | |
|---|---|
| **Mode** | {{ page.mode | default: "unclassified" }}{% if page.map_type != "" %} (`{{ page.map_type }}`){% endif %} |
| **Environment** | {{ page.environment | default: "unknown" }} |
| **Mapper** | {{ page.mapper | default: "unknown" }} |
{% if page.uploaded != "" %}| **Uploaded** | {{ page.uploaded }} |
{% endif %}{% if page.mx_url != "" %}| **ManiaExchange** | [Map page]({{ page.mx_url }}) |
{% endif %}{% if page.feedback.stars_avg %}| **Community rating** | {{ page.feedback.stars_avg }}/5 ({{ page.feedback.stars_total }} votes){% if page.feedback.yn_rating %} · YES/NO {{ page.feedback.yn_rating }}/5 ({{ page.feedback.yn_votes }}){% endif %} |
{% endif %}

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## About the map

_No description yet — add layout notes, routes, zones and tactics here._

---

## Screenshots

{% if page.screenshots and page.screenshots.size > 0 %}
<div style="display: flex; flex-wrap: wrap; gap: 12px;">
{% for s in page.screenshots %}
  <figure style="width: 48%; margin: 0;">
    <img src="{{ s.url }}" alt="{{ s.caption | default: page.map_name }}" style="width: 100%; border-radius: 8px;">
    <figcaption style="font-size: 0.85rem; opacity: 0.8;">{{ s.caption }}{% if s.author %} — {{ s.author }}{% endif %}{% if s.date %} ({{ s.date }}){% endif %}</figcaption>
  </figure>
{% endfor %}
</div>
{% else %}
{: .highlight }
> No screenshots yet. Add yours with the button below — a link to an image is enough.
{% endif %}

---

## Record history

{% if page.records and page.records.size > 0 %}
| Player | Time | Date | Mode | Replay | Note |
|--------|------|------|------|--------|------|
{% for r in page.records %}| {{ r.player }} | `{{ r.time }}` | {{ r.date }} | {{ r.mode | default: page.mode }} | {% if r.replay %}[link]({{ r.replay }}){% else %}—{% endif %} | {{ r.note | default: "" }} |
{% endfor %}

{: .note }
> A replay or video link makes a record verifiable; unlinked times may be marked as unverified.
{% else %}
{: .highlight }
> No records yet. Be the first to submit a time.
{% endif %}

---

## Add your screenshot or record

[Submit a screenshot or record](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-record.yml&labels=map-record&title=%5BMap%5D%20{{ page.map_name | url_encode }}){: .btn .btn-primary }
[Edit this page on GitHub](https://github.com/tomekdot/trackmania-galaxy/edit/main/{{ page.path }}){: .btn }

Replays are shared as **links only** — ManiaExchange replay pages or file hosts. Never upload `.replay.gbx` files to this repository.
