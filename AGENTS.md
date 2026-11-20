# AGENTS.md — Trackmania Galaxy

This file is the shared source of truth for every agent working in this repo.
Read it before editing. Update it whenever a convention below changes — that is
how agents stay in sync across sessions. Do not delete this file.

## Project

Community wiki for the TrackMania² Galaxy title pack: 262 Pursuit & Goal Hunt
maps with thumbnails, ratings, search, filters, per-map galleries, records,
history and memories, plus documentation. Static site, no server, no database.

- Astro 7 + Starlight, GitHub Pages at tomekdot.github.io/trackmania-galaxy/
- Node.js 22+
- Push to `main` runs `.github/workflows/deploy.yml` (withastro/action) — no manual deploy.

## Commands

```
npm install
npm run dev       # http://localhost:4321/trackmania-galaxy/
npm run build     # static output in dist/
npm run preview
npm test          # checks videoEmbed() URL recognition
```

Run `npm test` and `npm run build` before committing; both must pass.

## Layout

- `src/pages/index.astro` — map gallery (filters, thumbnails)
- `src/pages/maps/[slug].astro` — per-map page; imports `videoEmbed` from the lib
- `src/components/Layout.astro` — SEO head, theme
- `src/data/maps.json` — data consumed by the gallery (source cache: `data/maps.json`)
- `src/content/docs/docs/*.md` — Starlight wiki pages
- `src/lib/video-embed.js` — video URL → inline embed logic
- `scripts/check-video-embed.mjs` — URL recognition checks (`npm test`)
- `.github/ISSUE_TEMPLATE/map-record.yml`, `map-history.yml` — community submission forms
- `src/styles/`, `public/`, `assets/`

## Video embeds — links only, never uploads

Videos are always LINKED. Do not upload video files to the repo. Replays may be
attached as `.replay.gbx`; screenshots go in the images folder or stay as URLs.

`videoEmbed()` in `src/lib/video-embed.js` returns `{ kind: 'iframe' | 'video', src, label }`
or `null` (then the URL stays a plain link). Recognized sources:

- YouTube (watch/shorts/embed/live/youtu.be), Medal.tv, Twitch clips/VODs, Streamable
- Discord: `cdn.discordapp.com`, `media.discordapp.net`, `ephemeral-attachments`
- File hosts: Google Drive, Dropbox (rewritten to `?raw=1`), MEGA
- Any direct `.mp4`/`.webm`/`.mov`/`.m4v`/`.ogv` URL

When adding a host: add a matcher to that module AND a case to
`scripts/check-video-embed.mjs`. Require `^https?://` — never emit `javascript:`.

## Git identity — never override

- Name: `tomekdot`
- Email: `73403480+tomekdot@users.noreply.github.com` (the id-noreply form)
- Config is global; do not set per-repo `user.name`/`user.email`.
- Workers and agents must never change this identity.

### Commit style

Lowercase Conventional Commits — `type: description` with a lowercase type
and a lowercase first word of the description, English, e.g.
`fix: repair Medal.tv clip detection`.
Types: `feat | fix | docs | style | refactor | perf | test | build | ci | chore | revert | demo`.
An optional scope is fine where useful, e.g. `feat(maps): generate map pages`.
A global `commit.template` (C:/Users/tomekdot/.gitmessage) holds the reminder.

### Verification

Every commit MUST be signed with the GitHub-registered key so it shows Verified:

- global `commit.gpgsign=true`, `gpg.format=ssh`
- signing key: C:/Users/tomekdot/.ssh/id_ed25519_goalmas_signing.pub
- key is registered on GitHub as a signing key ("goalmas-dev signing")
- verify locally with `git log -1 --format="%G? | %GS | %s"` — `%G?` must be `G`
- DO NOT set a repo-local `user.signingkey`: a Hermes scratch key was once set
  here and produced `%G? = U` with unverified commits. Use the global key.

History rewrites (`rebase`, `filter-branch`, `commit-tree`) silently DROP
signatures (`%G? = N`). A scripted rewrite that runs `git commit --amend` per
commit (with `commit.gpgsign=true`) re-signs them — verify with `%G?` afterwards.
Use `--allow-empty` when amending empty commits, or rebase silently drops them.
Never force-push a shared branch without explicit user consent.

After any root-to-tip rewrite, re-point the `jekyll-final` tag to the new hash of
the Jekyll-era tip; tags never move automatically and a stale tag breaks links.

### Branch hygiene

- One clean commit per PR. Iterate on a personal fork branch with
  `git commit --amend` + `git push --force`, not a stack of commits.
- If a maintainer leaves feedback the user chooses not to act on, leave the PR
  open and post a polite handoff comment — do not keep editing.
- Do NOT commit `memory/` or `.memory/` — they are tooling artifacts, not project files.
- Stage only the files you intentionally changed. Other agents may commit
  concurrently; check `git status` and `git log` before and after your work.

## Working with the user

- Chat in Polish, but never CJK characters in Polish output.
- Decode typo-heavy Polish intent instead of asking for clarification.
- Prefer direct action; ask only when the choice is destructive or genuinely ambiguous.
- No `**` bold around file paths — the desktop passes them through literally.
- Public bug reports: anonymize names/links unless told otherwise; English-only
  text in issues/PRs of public repos (Polish stays in the chat).
