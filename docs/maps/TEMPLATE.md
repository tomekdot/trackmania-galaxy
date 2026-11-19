---
layout: default
title: "Map page template"
parent: Maps
nav_exclude: true
search_exclude: true
map: false

# --- Fill these in, then rename the file to docs/maps/<map-name>.md ---
map_name: "Map name"
mode: "Pursuit"            # Pursuit | Goal Hunt | Hunters | Pursuit SWAP | Goal Hunt Pursuit
environment: "Stadium"     # Canyon | Stadium | Valley | Lagoon
mapper: "Mapper name"
mx_url: ""                 # https://tm.mania.exchange/maps/...

# Screenshots: repo path (../assets/images/maps/...) or an external https URL.
screenshots: []
#  - url: "assets/images/maps/example.jpg"   # repo path (site-root relative) or an external https URL
#    caption: "Start area seen from the thief spawn"
#    author: "Nickname"
#    date: 2026-11-19

# Record history: newest entries first. Replay/clip = link OR a file committed under assets/replays/.
records: []
#  - player: "Nickname"
#    time: "0:42.123"
#    date: 2026-11-19
#    mode: "Pursuit"
#    replay: "https://tm.mania.exchange/replays/..."   # or "assets/replays/<file>.replay.gbx"
#    clip: "https://youtu.be/..."
#    note: "Lagoon Car, no shortcuts"
---

# {{ page.map_name | escape }}
{: .no_toc }

| | |
|---|---|
| **Mode** | {{ page.mode }} |
| **Environment** | {{ page.environment }} |
| **Mapper** | {{ page.mapper }} |
{% if page.mx_url != "" %}| **ManiaExchange** | [Map page]({{ page.mx_url }}) |
{% endif %}

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## About the map

Short description: layout, size, notable routes, zones used, and what makes the map interesting. Replace this paragraph.

---

## Screenshots

{% if page.screenshots and page.screenshots.size > 0 %}
<div style="display: flex; flex-wrap: wrap; gap: 12px;">
{% for s in page.screenshots %}
  <figure style="width: 48%; margin: 0;">
    <img src="{% if s.url contains 'http' %}{{ s.url }}{% else %}{{ s.url | relative_url }}{% endif %}" alt="{{ s.caption | default: page.map_name }}" style="width: 100%; border-radius: 8px;">
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
| Player | Time | Date | Mode | Replay | Clip | Note |
|--------|------|------|------|--------|------|------|
{% for r in page.records %}| {{ r.player }} | `{{ r.time }}` | {{ r.date }} | {{ r.mode | default: page.mode }} | {% if r.replay %}{% if r.replay contains 'http' %}[link]({{ r.replay }}){% else %}[file]({{ r.replay | relative_url }}){% endif %}{% else %}—{% endif %} | {% if r.clip %}{% if r.clip contains 'http' %}[clip]({{ r.clip }}){% else %}[file]({{ r.clip | relative_url }}){% endif %}{% else %}—{% endif %} | {{ r.note | default: "" }} |
{% endfor %}

{: .note }
> Entries are added by maintainers from community submissions. A replay or clip link makes a record verifiable; unlinked times may be marked as unverified.
{% else %}
{: .highlight }
> No records yet. Be the first to submit a time.
{% endif %}

---

## Add your screenshot or record

[Submit a screenshot or record](https://github.com/tomekdot/trackmania-galaxy/issues/new?template=map-record.yml&labels=map-record&title=%5BMap%5D%20{{ page.map_name | url_encode }}){: .btn .btn-primary }
[Edit this page on GitHub](https://github.com/tomekdot/trackmania-galaxy/edit/main/{{ page.path }}){: .btn }

Replays and clips can be **linked or attached** — a ManiaExchange replay page, a YouTube/Twitch clip, or the `.replay.gbx` file itself (attach it to the issue, or add it under `assets/replays/` in a pull request).
