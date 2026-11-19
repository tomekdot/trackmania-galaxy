---
layout: default
title: Gameplay Guides
nav_order: 3
---

# Gameplay Guides
{: .no_toc }

Master the mechanics of Trackmania Galaxy with these in-depth guides.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Basic Controls

Trackmania Galaxy uses a simple control scheme:

| Action | Default Key |
|--------|-------------|
| Accelerate | `Up Arrow` / `W` |
| Brake / Reverse | `Down Arrow` / `S` |
| Steer Left | `Left Arrow` / `A` |
| Steer Right | `Right Arrow` / `D` |
| Respawn | `Backspace` |
| Reset to Start | `Enter` |
| Open Openplanet Overlay | `F3` |

{: .note }
> Controls can be rebound in the ManiaPlanet settings. Many players use custom setups for competitive play.

---

## Game Modes

### Pursuit 🚔

The flagship mode — **cops vs thieves**.

- At the very beginning of a round everyone joins the **Thieves** team; after a few seconds the first **officer** is selected.
- An officer captures a thief by driving through them — the captured player joins the police forces.
- The round ends when all thieves are caught or the time runs out.
- Thieves earn survival points when other thieves are caught, plus bonuses for lasting until the end.

**Worth knowing while playing:**

- The color of your interface tells you which team you are on; nametag color distinguishes thieves from officers.
- As a thief you cannot respawn immediately — you have to wait a short time and stand still before being moved back to the spawn point.
- Leaving the map area is impossible: driving outside the building zone or falling into the void respawns you and forces you onto the police team.
- Not every capture registers instantly — other players may be seen with a tiny delay, so a capture that looks successful may not have been registered by the server.

See the full [TrackMania² Pursuit](pursuit) documentation for detailed mechanics, zones, and scoring.

### Goal Hunt 🎯

A points-based checkpoint hunting race — the player with the highest score wins the map.

- A random checkpoint (**Target #1**) is selected for all players; everyone has the same Target #1.
- The first player to reach Target #1 scores **3 points**, then a new target is randomly selected.
- A new Target #1 may be selected automatically if nobody reaches it within **45 seconds**.
- If someone else captured Target #1, it becomes **Target #2** for you and scores fewer points. You can capture up to **2 previous targets** before they vanish on the next target selection.
- Any respawn (manual, Zone elimination, vehicle change) takes **1 point** away from your score.

Goal Hunt is also a variation of Pursuit: when Goal Hunt maps are played in Pursuit, thieves hunt their individual checkpoints instead of getting points for surviving other captures (**Goal Hunt Pursuit**).

### Hunters 🏃

A wild Pursuit spin-off where everyone chases everyone.

- At the start you receive a target — a player you must catch to score **1 point**. Someone else is hunting you, and you do not know who.
- A new target is assigned once you deal with the current one (and players are available).
- You have to wait **5 seconds** to respawn or change your vehicle while someone is hunting you.
- One map lasts **5 minutes**; the game ends when time reaches zero or someone reaches the point limit.

Pursuit maps can be played in Hunters. Hunters maps can be played in Pursuit, but they enable **Pursuit SWAP**, where players switch roles every 30 seconds.

---

## Building Maps for Galaxy

### Pursuit maps (PursuitArena)

- Set the map type to **PursuitArena**, otherwise the server will not accept the map.
- Only two things are required: a **spawn block** and a **podium**. A multilap block with 1 checkpoint can replace the regular spawn. You cannot place a finish line.
- No validation is needed — once the required blocks are placed, the map is ready for the server.
- The map must be a **closed area** surrounded by a tall barrier (mountains, wall, glass), an island in a lake, or suspended in mid-air. If going outside is possible, the map is rejected.
- Building over water? Use the Pursuit Map Settings option that eliminates players in the water.
- Explore Pursuit Map Settings and the different Zones to add gameplay mechanics.

### Goal Hunt maps (GoalHuntArena)

- Set the map type to **GoalHuntArena**.
- A spawn block and a podium (or a multilap block with 1 checkpoint); no finish line.
- At least **5 supported checkpoints**. Only Nadeo blocks are supported, with some exceptions.
- The map type tells you how many checkpoints you placed and lists the names of unsupported ones.
- Build arenas rather than road systems — arenas are easier to drive on, and players should be able to get back on track easily after capturing a checkpoint.

### Hunters maps (HuntersArena)

- Follow the Pursuit map guidelines, but use **HuntersArena** so maps are easier to categorize online.
- Keep maps small for dynamic matches where everyone is in the same place.
- Avoid Zones and water — targets eliminated by a Zone instead of a capture take away the skill and tactical part of the mode.

---

## Advanced Techniques

### Steer Tapping

Steer tapping involves rapidly tapping the steering key to maintain control around tight corners without losing speed. This technique is particularly useful on slippery surfaces and sharp bends.

### Reactor Boosts

Reactor boosts are environmental speed boosts found on certain maps. Learning to enter and exit boost zones at the optimal angle is key to maximizing your speed.

### Bug Slides

Some surfaces in ManiaPlanet allow for physics-based slides. Mastering bug slides can shave significant time off your runs.

### Full Speed (FS) Driving

Full speed driving means completing a track without braking or releasing the accelerator. Many maps are designed to be completed full speed — study the optimal lines to pull this off.

---

## Map Types

Trackmania Galaxy features several surface types that require different techniques:

- **Road** — Standard surface with predictable grip
- **Dirt** — Lower grip, requires smooth inputs
- **Grass** — Varies by map; typically slower
- **Platform** — Elevated sections requiring precise jumps
- **Ice** — Very low grip, requires anticipation and smooth steering
- **Plastic** — Smooth surface with moderate grip
- **Wood** — Often used for ramps and technical sections

---

## Tips for Improving Your Times

1. **Study replays** — Watch top player replays to understand the optimal lines.
2. **Take notes** — Identify where you lose the most time.
3. **Practice segments** — Use checkpoint respawns to practice difficult sections.
4. **Consistency over speed** — A clean run beats a risky one.
5. **Learn the surfaces** — Each surface type demands a different approach.
6. **Watch the Pursuit meta** — Understand which vehicles excel on which maps.

{: .note }
> More technique guides are coming soon! Check back regularly or [contribute your own](contributing).
