# TrackMania² Galaxy

'''TrackMania² Galaxy''' is a free [[title pack]] for [[ManiaPlanet]] created by '''Dommy''' (domino54). It is a multi-environment title pack featuring multiple game modes, with the flagship mode being '''Pursuit''' (cops vs thieves). Originally released as '''TrackMania² Pursuit''' in 2014, the title was officially renamed to '''TrackMania² Galaxy''' in 2019 (Title Update 1.6).

The title pack is available for free — no Planets payment required.

{{Title pack infobox
| name = TrackMania² Galaxy
| image = 
| author = Dommy (domino54)
| initial_release = 2014 (as Pursuit), 2019 (as Galaxy)
| latest_release = 27 November 2024 (Galaxy Rebase)
| environments = [[Canyon]], [[Stadium]], [[Valley]], [[Lagoon]]
| game_modes = Pursuit (Survival, Goal Hunt, SWAP), Goal Hunt, Hunters
| type = Multi-environment title pack
}}

== Overview ==

TrackMania² Galaxy is an ever-expanding collection of various game modes introducing new gameplay mechanics and tactics to learn. Run for your freedom as a thief or execute the law as a cop in an intensive Pursuit match. Discover a new way of racing by hunting checkpoints in Goal Hunt. Hunt your opponents and avoid being hunted in Hunters.

The title pack was designed as a unified collection of game modes, inspired by Dommy's abandoned [[ShootMania Galaxy]] title. Galaxy is meant to be a shared ecosystem with a shared profile, stats, achievements, and unlockables across both TrackMania and ShootMania.

== Game Modes ==

=== Pursuit ===
{{Main|Pursuit (Galaxy)}}

The flagship mode. At the very beginning of a round everyone joins the '''Thieves''' team; after a few seconds the first '''officer''' is selected. An officer captures a thief by driving through them, and the captured player joins the police forces. The round ends when all thieves are caught or the time runs out.

* The color of your interface tells you which team you are on; nametag color distinguishes thieves from officers.
* As a thief you cannot respawn immediately — you must wait a short time and stand still before being moved back to the spawn point.
* Leaving the map area is impossible: driving outside the building zone or falling into the void respawns you and forces you onto the police team.
* Other players may be seen with a tiny delay, so a capture that looks successful may not have been registered by the server.

=== Goal Hunt ===

A points-based checkpoint hunting race where the player with the highest score wins the map.

* A random checkpoint ('''Target #1''') is selected for all players — everyone has the same Target #1.
* The first player to reach Target #1 scores '''3 points'''; a new target is then randomly selected.
* A new Target #1 may be selected automatically if nobody reaches it within '''45 seconds'''.
* If someone else captured Target #1, it becomes '''Target #2''' for you and scores fewer points. Up to '''2 previous targets''' can be captured before they vanish on the next target selection.
* Any respawn (manual, Zone elimination, vehicle change) takes '''1 point''' away from your score.

Goal Hunt is also a variation of Pursuit: when Goal Hunt maps are played in Pursuit, thieves hunt their individual checkpoints instead of scoring for surviving other captures (Goal Hunt Pursuit).

=== Hunters ===

A wild Pursuit spin-off where everyone chases everyone. Each player receives a target to catch for '''1 point''', while someone else hunts them without being revealed. A new target is assigned after the current one is dealt with. Players must wait '''5 seconds''' to respawn or change vehicle while being hunted. One map lasts '''5 minutes''', and the game ends when time reaches zero or someone reaches the point limit.

Pursuit maps can be played in Hunters. Hunters maps can be played in Pursuit, but they enable '''Pursuit SWAP''', where players switch roles every 30 seconds.

== Title Update History ==

=== Title Update 1.1 (14 January 2018) ===

* '''Split Screen mode''' — Pursuit playable with up to '''4 gamepads''' (4 players on one computer), collisions on. Keyboard is not available as an input device and controllers are assigned randomly to players.
* '''Minimap from ShootMania Galaxy''' — rewritten to support TrackMania, showing opponents and teammates as cars with icons of their current vehicle. Configurable via Pause &gt; Pursuit Settings &gt; Minimap. Thieves are hidden from the minimap if names are set to be not visible through walls.
* '''Police skin for Canyon Car''' — applied on the next spawn after becoming a policeman; skins for other cars were planned to follow.
* '''Lagoon Car''' — locked to Lagoon maps after being overpowered elsewhere. A vehicle-selection mechanic was implemented to unlock it on any environment for '''30 minutes''' for '''15 Planets''', but the option was unavailable at the time and still to be discussed with players.
* '''Other cars on Stadium''' — Canyon Car, Valley Car and Lagoon Car unlockable in Stadium thanks to Openplanet, which was not a public tool yet.

=== Title Update 1.2 — "Enhanced Points System" (29 January 2018) ===

This update introduced a completely overhauled, dynamic scoring system designed to balance the matches between the Police and the Thieves.

* '''Capture Points Scaling''' — Early-game captures are worth 1 point; late-game captures scale up to 5 points per capture as fewer thieves remain.
* '''Survival Points''' — Every active thief receives 1 survival point whenever another thief is caught.
* '''Last Thief Bonus''' — Securing the final surviving thief awards up to 5 bonus points; each capture during a round grows the capture streak, adding 1 point per capture up to 5.
* '''Killstreaks and dominations''' from ShootMania Galaxy — a PENTAKILL note for ending 5 thieves at once, and domination when the same player captures you 2 times in a row (even across maps or days).
* '''Adjustable minimap zoom''' — Pause &gt; Pursuit Settings &gt; Minimap, with 6x6, 8x8 (default), 10x10 and 12x12 options. Zoom gives no advantage: opponents disappear at the same distance regardless of zoom.
* '''Vehicles shown in the ranking''' — the scores table displays each player's vehicle choice.

=== Title Update 1.3 — "Construction Update" (25 June 2018) ===

A set of new tools for mappers: gameplay tweaks, a vehicle toggle and two new OffZone types.

* '''Vehicle Selection Screen''' — shows a picture of each car, a brief summary of its pros and cons, and properly measured stats. Stats are shown as a percentage score compared to the best car in every category.
* '''Map-Specific Gameplay Options''':
** Choose available vehicles — only the marked ones are selectable in the vehicle selection screen.
** Force different cars for Police and Thieves (for example CanyonCar cops vs StadiumCar robbers).
** Gameplay settings — Pursuit or Hide & Seek, nametag behavior, anti-camping mode toggle, disable free camera. Servers can force their own settings over map-specified ones.
** Lock minimap rotation to North — useful for a top-down camera that does not rotate (keep the camera's North over the top edge of the screen).
* '''Danger Zone''' — a less lethal OffZone: players inside have '''8 seconds''' to leave it before it treats them like a normal OffZone.
* '''Police Zone''' — marks routes available only for the Police team; any thief who enters is moved to the Police team instantly.
* None of the OffZone types are automatically marked with items — mappers must place visual indicators manually.

=== Title Update 1.3.1 (2 July 2018) ===

* '''Zone Items by florenzius''' — designed by Dommy and crafted by florenzius, these ornaments indicate the locations of all three zone types: OffZone, Danger Zone and Police Zone (yellow Danger Zone, red OffZone, blue Police Zone).
* The items are '''only decorations''' — they do not act as zones. Mappers must place the zone manually using the Pursuit OffZone plugin, then use the decorations for visual feedback.
* Minor changes: custom chat shows the message time and multiline issues are fixed; alternative gameplay Stadium vehicles have skins applied, with Police CanyonCar showing properly; decoration size is selectable in the Stadium pack.

=== Title Update 1.4 — "4 Years of Pursuing" (19 February 2019) ===

Released on the 4th anniversary of the mode's first release, together with florenzius.

* '''Capture Assists''' — the game detects who contributed to catching a thief besides the capturer: chasing a thief long enough, provoking a thief to start moving, or making a thief drop off ledges and cliffs or drive downhill (the nearest policeman within a fixed distance is marked as assistant). Assisting gives '''1 point'''; if the thief dies through any other means while you are marked as assistant, it counts as '''your''' catch. Assistance status is kept for '''15 seconds'''.
* '''TrackMania Forever Vehicles''' — all 6 "new" TMF vehicles available without Planet paywalls, including upgraded Island Car, Desert Car and Snow Car models made with Purification and the TM ONE crew. TrackMania 2 cars were unavailable for the first week.
* '''Goal Hunt Pursuit''' — thieves get no survival points when someone else is captured; instead each thief has an individual goal worth '''2 points''', with the next goal picked randomly once it is reached. After being caught, the only way to score is catching thieves as a policeman. Available on the same server as standard Survival Pursuit — just add Goal Hunt maps.
* '''Speedbomb''' — maps can equip cars with a bomb ignited by driving at slow speed; '''5 seconds''' of turtling triggers an explosion that costs the player their thief or policeman status.
* '''3 New Zones''':
** '''Thief Zone''' — thieves only; police are respawned immediately on entry. Thieves can stay inside for '''2 seconds''' only, and the remaining time does not reset when leaving — it regenerates very slowly, preventing camping.
** '''Speedbomb Zone''' — enables the speedbomb for any player inside, with minimum speed requirements twice as high as map-wide Speedbomb ('''200 km/h'''); limits are customizable in map properties.
** '''Police Danger Zone''' — a combo zone that does not physically exist in the editor: placing Danger Zone and Police Zone in the same area combines both effects.
* '''Fuel & Charging Stations''' — placing stations enables the fuel mechanic: a full tank lasts '''3 minutes of driving''' or '''12 minutes of standing still''' before car controls are cut off. Refilling happens almost immediately upon entering a station. With fuel enabled, policemen must wait '''15 seconds''' to respawn, like thieves.
* '''Race Objectives''' — each objective on a map is loaded with up to '''10 points''' (depending on player count). The first player to reach it gets the most points, each next player one point less, until the objective awards nothing. Points are awarded regardless of team.
* '''UI Optimization''' — an ongoing client-side UI rewrite separates client UI updates from server updates, so UI bugs and translations can be fixed without a server update.
* '''Quality of Life''' — thieves buffed to up to '''4 survival points''' (doubled once half the thieves are gone, 3 when a quarter remains, 4 for the last 1/8); +1 point for capturing a Lagoon Car thief with any other car (also for assists); the Lagoon Car purchase now gives '''2 hours''' instead of 30 minutes, with the timer ticking only while spawned with the car and only if the map does not force Lagoon Car for everyone; AFK players on the spawn turn into policemen when the round starts; the first spawn of a round has a '''1.5-second''' delay.
* '''Mapper notice''' — Charging Stations and Race Objectives are recognized as checkpoints, so their anchor tags must be set to <code>GasStation</code> and <code>RaceObjective</code>. Neither item can be rotated on any axis: they must be placed level horizontally and aligned to cardinal directions, though they may be placed off-grid at arbitrary X/Y/Z coordinates.

=== Title Update 1.4.1 (25 February 2019) ===

A small week-one patch for both the Multienvironment and Stadium titles:

* TrackMania 2 cars were unlocked again.
* Added a setting to override the list of cars forced by the map.
* Added a setting to enable '''vehicle rotation''' — randomly selected cars become the only ones available, in the number specified by the setting.
* Made "chase" assist detection less strict, allowing assists to happen more often.
* Fixed Danger Zone and Thief Zone icons remaining on screen after unspawning.
* Danger Zone and Thief Zone timers now start only after the player has started.
* Speedbomb is no longer active in the "Waiting for players" sequence if the previous map enabled it globally.
* The map type now saves <code>-0:00.001</code> as the author time instead of <code>0:00.001</code>.
* Capture combo points are now present in Goal Hunt Pursuit to balance the teams.
* Removed last-thief and surviving-to-the-end point awards in Goal Hunt Pursuit. The only way to earn points as a thief in this mode is through capturing checkpoints.

Mapper notice: customized Gas Stations and Race Objectives made by mashing the items with blocks via Mesh Modeller are '''not allowed or unsupported'''. Their trigger shapes are hardcoded in the game mode, so modified variants are very likely to break player detection. Support is not planned, both because of the trigger-shape complications and to keep easily recognizable landmarks consistent across maps.

=== Several Small Updates (12 July 2019) ===

Over the weeks following 1.4.1, several changes were deployed gradually to both Pursuit packs.

==== Improved next map selection screen ====

* Replaying the just finished map is no longer available (at least for now).
* Vote counts for each map are shown only after voting is complete, so players are not influenced by others' choices.
* The game remembers which maps you recently played and shares this with the server, which shows the '''6 maps played least often''' by currently connected players.
* In case of a tie, the '''first map to receive a vote wins'''. If a player changes their mind and their first pick ties with anything else, the initial pick still wins.
* Voting algorithm: playing at least one full round on a map adds it to the beginning of your recently played list (or moves it back to the start if already there). When voting begins, the server collects a list of 15 maps from all players. Based on a map's position in each list, it gets between 1 and 15 points — more recently played maps get more points. Maps are then ordered by points ascending, and the first 6 appear as voting options.

==== Redesigned vehicle selection menu ====

* All 10 car buttons fit on the whole screen, spaced out more evenly.
* Skins are featured in the buttons as well.
* UI elements behind the menu are hidden to prevent blending.
* The new menu supports an experimental live car preview at the start of a map.

==== Other changes ====

* New elimination icons replace the "drowning car" symbol shown on environmental captures, reducing text bloat on screen.
* Enviromixing soundtrack: a full mix of all 27 tracks heard in Canyon, Stadium, Valley and Lagoon, available in the Multienvironment pack only. Shuffle is on by default and repeat one was added.
* Progressive respawn time: retrying takes '''5 seconds''' at the start of a round and gradually extends up to '''15 seconds''' for the last thief remaining. Everyone is informed if a captured player was about to respawn. Respawn always takes 5 seconds in Goal Hunt Pursuit.
* Balanced cop points: captures now award up to '''8 points in total''' — 1–3 base points (up to 5 for the last thief), 0–4 capture streak points (if not the last thief), and +1 for catching a Lagoon Car with any other car.

=== Title Update 1.5 — "Pursuit SWAP" (22 July 2019) ===

* '''Pursuit SWAP''' — a mutation of regular Survival Pursuit: half the players start as cops and half as thieves. Catch thieves to score 5 points or survive to gain 1 point. '''All players swap roles every 30 seconds''' (10 swaps during the match) and the player with the highest score wins. It is played on HuntersArena maps, within the same game mode script as other Pursuit variants. SWAP was played on channels for one week, after which its maps were merged into the regular Pursuit playlist.
* '''Overtime''' — when the timer hits the limit but a thief is still being chased, the game continues until they lose their tail or get captured. Overtime applies only to Survival and Goal Hunt variants.
* '''Other changes''' — Stadium red turbos can now be used to construct more extreme maps; the exploit allowing thieves to switch to spectator mode without consequences was fixed, and any policeman who could have got an assist on such a thief now receives points for capturing them.

=== Title Update 1.6 — "Galaxy" (17 October 2019) ===

The title pack was officially renamed from TrackMania² Pursuit to TrackMania² Galaxy. The Pursuit mode name remains unchanged.

> "It doesn't mean the Pursuit mode changes its name, it's just a rename of the title pack. The reason behind this change is my will to continue the legacy of my abandoned ShootMania Galaxy title."
> — Dommy (domino54)

Both the multi-environment and Stadium variants were renamed. The title is now free of Planets payment. The update also brought a new ranking page, exclusive player badges, interface tweaks and a large set of technical changes.

==== Additions ====

* New, redesigned ranking screen with detailed player info, gamepad navigation, match info in the header, per-player stats in the footer, and separate round/match points.
* Exclusive badges next to player names for important contributors (models, translations, long-time mappers, competition winners); most Nadeo members have one.
* Points are split into round points and match points — green PTS are added to the Total at the end of the round, like in ShootMania or Rounds/Cup modes.
* '''Proximity assists''' — least-priority assists for cops within 8 metres of a thief (a quarter of a Stadium block).
* Gamepad support for the vehicle selection and map selection screens.
* Scoreboard now counts assists scored by each player.
* '''Active and Passive thieves system''' — thieves actively driving gain more survival points, while campers' points are capped.
* Test mode in the map editor (avoid for now — impossible to return to the editor).
* Speedometer now fakes the first 1k RPM to reflect idle engine sounds of TMU vehicles, plus other cosmetic speedometer changes.
* Platform soundtrack, an easter egg related to drifting, and an easter egg played when capturing or being captured by a specific player.
* '''TrackMania² Galaxy Canary''' — development branch of the Stadium title for testing.
* Discord advertisement under the scoreboard.

==== New ranking page in detail ====

The ranking page was fully rewritten by Dommy and no longer relies on the outdated ManiaPlanet 3 scripts, so it no longer randomly crashes upon joining.

* '''Gamepad navigation''' — D-Pad or Right Stick up/down moves a page up or down; D-Pad left/right switches between tabs.
* '''Header''' — information about the ongoing match plus the logo of the played game mode.
* '''Footer''' — your stats (or the spectated player's): survival score, captures, assists, total points and current placement.
* '''Vehicle icons''' replace 1-letter abbreviations — hover for the full car name, click to switch to it if you can respawn.
* The '''best players page''' was remade: previously only under Left Alt, now available under Tab and through the gamepad.
* More room for player names, with badges shown next to nicknames.

==== Badges, design tweaks and Canary ====

* Badges '''cannot be bought''' — they are earned by contributing models or translations, being a long-time mapper, or winning official competitions. They appear in the scoreboard and nametags, with more locations planned.
* Minor design tweaks refreshed some interface elements and added animations for a more polished feel.
* '''Canary''' is the pack where all pre-release tests happen; it is only for players interested in testing new features, with information posted on the official Discord.

==== Changes ====

* Hunters mode updated and playable again.
* Most files reorganized and converted to WebP, JSON and OGG.
* Tweaked UI placement/effects internals, resulting in fewer frame drops.
* Assists optimized — checked twice a second instead of every frame (100 frames → 2 frames).
* Capture detection optimized with smarter distance calculation.
* Speedometer RPM gauge slightly interpolated to reduce jitter in TMU cars.
* More split-screen compatibility.
* Fixed: Thief Zone timer appearing for cops; on-screen messages with links staying after the message disappears; faulty detection of random chase assists; incorrect visibility of player names during the preparation phase.

==== Deletions ====

* Removed discontinued server manager ("Players list"), obsolete code and obsolete buttons from the pause menu.

=== Galaxy Rebase — TMAll Update (27 November 2024) ===

TrackMania² Galaxy was '''rebased on the latest version of TMAll''', bringing all the newest TMAll features directly into Galaxy and unifying the codebase. Announced by Dommy on the Galaxy Discord on '''27 November 2024''' ("The most unexpected news of the year, for Galaxy"), covering both the Multienvironment and Stadium titles.

* '''MP Store integration''' — access the ManiaPlanet Store directly from Galaxy.
* Trailer skins for TM2 cars in Stadium; custom skins for thieves in Stadium.
* Persistent Storage Crash Fix — the notorious "29.9 bug" is resolved.
* All Goal Hunt maps (including new ones) are now properly detected and automatically switch the mode to Goal Hunt Pursuit.
* TrafficCar playable in Pursuit if the currently played map explicitly enables it; LagoonCar fully accessible in the map editor.
* Map Voting Screen now correctly suggests the 6 least-played maps of the currently playing players instead of being effectively random.
* Galaxy Stadium fresh look, and car model fixes (Bay Car, Coast Car and Rally Car no longer turn white on dirt surfaces).

Known limitations: TMU car models remain unchanged for now, and Galaxy Stadium currently does not allow creating maps with different vehicles.

== Building maps ==

=== Pursuit maps ===

* The map type must be set to '''PursuitArena''', otherwise the server will not accept it.
* Only a '''spawn block''' and a '''podium''' are required; a multilap block with 1 checkpoint can replace the regular spawn. A finish line cannot be placed.
* No validation is needed — once the required blocks are placed, the map is ready for the server.
* The map must be a closed area surrounded by a tall barrier (mountains, wall, glass), an island in a lake, or suspended in mid-air. If going outside is possible, the map is rejected.
* Maps built over water can use the Pursuit Map Settings option that eliminates players in the water.

=== Goal Hunt maps ===

* The map type must be set to '''GoalHuntArena'''.
* A spawn block and a podium (or a multilap block with 1 checkpoint); no finish line.
* At least '''5 supported checkpoints'''; only Nadeo blocks are supported, with some exceptions. The map type reports the checkpoint count and lists unsupported checkpoint names.
* Arenas are preferred over road systems, and maps should be easy to navigate after capturing a checkpoint.

=== Hunters maps ===

* Follow the Pursuit guidelines but use '''HuntersArena''' for easier online categorization.
* Maps should usually be small, allowing dynamic matches where everyone is in the same place.
* Avoid Zones and water — targets eliminated by a Zone rather than a capture remove the skill and tactical part of the mode.

== Environments ==

{| class="wikitable"
|-
! Environment !! Game
|-
| [[Canyon]] || [[TrackMania² Canyon]]
|-
| [[Stadium]] || [[TrackMania² Stadium]]
|-
| [[Valley]] || [[TrackMania² Valley]]
|-
| [[Lagoon]] || [[TrackMania² Lagoon]]
|}

== Vehicles ==

{| class="wikitable"
|-
! Vehicle !! Game
|-
| CanyonCar || [[TrackMania² Canyon]]
|-
| StadiumCar || [[TrackMania² Stadium]]
|-
| ValleyCar || [[TrackMania² Valley]]
|-
| LagoonCar || [[TrackMania² Lagoon]]
|-
| IslandCar (redesigned by Purification) || [[TrackMania² Island]]
|-
| BayCar || [[TrackMania United Forever]]
|-
| CoastCar || [[TrackMania United Forever]]
|-
| SpeedCar (DesertCar) || [[TrackMania² Speed]]
|-
| AlpineCar (SnowCar) || [[TrackMania² Alpine]]
|-
| RallyCar || [[TrackMania United Forever]]
|-
| TrafficCar || [[TrackMania² All]]
|}

== Gallery ==

<gallery>
<!-- Add screenshots here: File:Galaxy_screenshot.jpg|Caption -->
</gallery>

== See Also ==

* [[Pursuit (Galaxy)]]
* [[Openplanet]]
* [[Title pack]]

== External Links ==

* [https://maniaplanet.com/titles/Pursuit@domino54 Official ManiaPlanet page]
* [https://discord.me/pursuit Official Discord server]
* [https://tm.mania.exchange ManiaExchange — community maps]
* [https://forum.maniaplanet.com/viewtopic.php?t=42646 Official forum thread]

== References ==

<references />

[[Category:Title packs]]
[[Category:ManiaPlanet]]
[[Category:TrackMania² Galaxy]]
[[Category:Community projects]]
