---
layout: default
title: Companion Plugins
nav_order: 8
---

# Companion Plugins
{: .no_toc }

Community-developed plugins and utilities that enhance the Trackmania Galaxy experience.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Moon Calendar (Event Calendar)

The community-developed **Moon Calendar** (also known as the **Event Calendar** plugin) is a lightweight utility designed to help players coordinate and track active server schedules. It allows players to align their play sessions with dedicated server rotations (e.g. Goal Hunt days, Pursuit days, and other thematic community milestones).

### Key Features

- **Lunar Tracking:** Monitors upcoming moon phases displayed directly in your Openplanet overlay.
- **Dynamic Event Alerts:** Notifies players upon game startup about active thematic rotations (such as *Goat Hunt* days and surrounding event windows).
- **Auto-Refresh Engine:** Responsive, low-overhead data fetching that synchronizes calendar states smoothly.

---

### Release 1.1.0 — UI Polish & Enhanced Data Fetching (February 2026)

This release addresses previous packaging errors where specific asset directories were excluded from the `.op` build pipeline, causing initialization failures.

#### UI & UX Improvements

- **Consistency:** Standardized button sizes and unified navigation/day button heights for a cleaner, scaling interface.
- **Usability:** Enforced a minimum window width to prevent date controls from collapsing.
- **Layout:** Added a status footer to display connection and server sync states, plus enhanced notifications and alignment.

#### Data Fetching & Performance

- **Reliability:** Refactored the core connection handshake to increase stability under restricted environments (e.g., active VPN connections).
- **Automation:** Implemented auto-refresh tracking with a shortened debounce time of 2 seconds for increased UI snappiness.

#### Packaging & Tooling

- **Build Script:** Updated the companion build pipeline (`tools/build-op.ps1`) to automatically stage `.op` files in the plugin root and implement timestamped fallback folders if files are locked by a running instance of Trackmania.

---

### Installation & Configuration Guide

To ensure unofficial or development-stage plugins load successfully, **Developer Mode** must be active.

#### Step 1: Place the Plugin File

Move the downloaded `event-calendar-vX.Y.Z.op` file directly into your Openplanet plugins folder:

```
C:\Users\<YourUsername>\Openplanet4\Plugins\
```

#### Step 2: Enable Developer Mode

1. Launch the game and open the Openplanet overlay by pressing **F3**.
2. Navigate to **Signature Mode** and select **Developer**.
3. *Optional but recommended:* Go to **Settings** -> **Script Engine** -> check **Enable developer mode on startup** so you do not have to perform this step manually upon restarting.
4. Reload the scripts (**F3** -> **Reload scripts**) or restart your game client.

#### Step 3: Requirements

- **Openplanet Version:** Requires Openplanet **1.29.0** or **1.29.1** (or newer).
- The plugin will appear in your overlay menu as **Event Calendar** under the **Plugins** category.

---

## Related Links

- [Openplanet](https://openplanet.nl)
- [Openplanet Plugins Forum](https://forum.maniaplanet.com/viewforum.php?f=13)

---

{: .note }
> This page documents third-party community plugins. For plugin-specific support, please refer to the respective plugin authors or the Openplanet community forums.
