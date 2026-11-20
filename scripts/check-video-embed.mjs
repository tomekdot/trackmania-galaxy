// Verifies videoEmbed() against the URL shapes contributors actually paste.
// Run with: npm test
import assert from 'node:assert/strict';
import { videoEmbed } from '../src/lib/video-embed.js';

const cases = [
  // Discord CDN / media
  ['https://cdn.discordapp.com/attachments/123/456/run.mp4', { kind: 'video', label: 'Discord' }],
  ['https://media.discordapp.net/attachments/123/456/run.webm?width=1280', { kind: 'video', label: 'Discord' }],
  ['https://cdn.discordapp.com/ephemeral-attachments/123/456/clip.mov', { kind: 'video', label: 'Discord' }],
  // File hosts
  ['https://drive.google.com/file/d/1AbC_123xyz/view?usp=sharing', { kind: 'iframe', label: 'Google Drive' }],
  ['https://drive.google.com/open?id=1AbC_123xyz', { kind: 'iframe', label: 'Google Drive' }],
  ['https://www.dropbox.com/s/abc123def/run.mp4?dl=0', { kind: 'video', label: 'Dropbox' }],
  ['https://mega.nz/file/AbCdEfGh#IjKlMnOp', { kind: 'iframe', label: 'MEGA' }],
  ['https://streamable.com/e/abc123', { kind: 'iframe', label: 'Streamable' }],
  ['https://streamable.com/o/abc123', { kind: 'iframe', label: 'Streamable' }],
  // Existing hosts must keep working
  ['https://youtu.be/dQw4w9WgXcQ', { kind: 'iframe', label: 'YouTube' }],
  ['https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=3', { kind: 'iframe', label: 'YouTube' }],
  ['https://medal.tv/clips/12345', { kind: 'iframe', label: 'Medal.tv' }],
  ['https://www.medal.tv/games/trackmania/clips/abc123def', { kind: 'iframe', label: 'Medal.tv' }],
  ['https://clips.twitch.tv/AmazingClipName', { kind: 'iframe', label: 'Twitch' }],
  ['https://www.twitch.tv/videos/123456789', { kind: 'iframe', label: 'Twitch' }],
  ['https://example.com/some/direct-video.webm?token=1', { kind: 'video', label: 'Video' }],
  // Not a video -> let it stay a plain link
  ['https://github.com/tomekdot/trackmania-galaxy', null],
  ['javascript:alert(1)', null],
  ['', null],
];

for (const [url, expected] of cases) {
  const got = videoEmbed(url);
  if (expected === null) {
    assert.equal(got, null, `expected no embed for ${url}`);
  } else {
    assert.ok(got, `expected an embed for ${url}`);
    assert.equal(got.kind, expected.kind, `kind for ${url}`);
    assert.equal(got.label, expected.label, `label for ${url}`);
    assert.match(got.src, /^https:\/\//, `src for ${url}`);
  }
  console.log(`ok  ${url}  ->  ${got ? got.kind + ':' + got.label : 'plain link'}`);
}

const dropbox = videoEmbed('https://www.dropbox.com/s/abc123def/run.mp4?dl=0');
assert.match(dropbox.src, /raw=1/);
assert.doesNotMatch(dropbox.src, /dl=0/);
console.log(`ok  dropbox source rewritten to ${dropbox.src}`);

assert.equal(videoEmbed('https://medal.tv/clips/4954893').src, 'https://medal.tv/clip/4954893');
assert.equal(videoEmbed('https://streamable.com/o/abc123').src, 'https://streamable.com/e/abc123');
console.log('ok  Medal.tv normalised to the frameable /clip/<id> URL');
console.log('ok  Streamable /o/<id> normalised to /e/<id>');

console.log(`\n${cases.length + 3} checks passed.`);
