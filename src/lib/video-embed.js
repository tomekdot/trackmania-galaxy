// Turns a video URL into an inline embed descriptor: { kind: 'iframe' | 'video', src, label }.
// Anything unrecognized returns null and stays a plain clickable link.
// Rule for this wiki: videos are always LINKED, never uploaded (see docs/contributing).
const PARENT = 'tomekdot.github.io';

const VIDEO_FILE = /\.(mp4|webm|mov|m4v|ogv)(\?[^\s#]*)?(#[^\s]*)?$/i;

// Dropbox shared links serve the file only when `raw=1` is present.
function dropboxRaw(url) {
  const [base, query = ''] = url.split('?');
  const kept = query.split('&').filter((p) => p && !/^(dl|raw)=/i.test(p));
  kept.push('raw=1');
  return base + '?' + kept.join('&');
}

export function videoEmbed(rawUrl) {
  if (!rawUrl || typeof rawUrl !== 'string') return null;
  const u = rawUrl.trim();
  if (!/^https?:\/\//i.test(u)) return null;

  let m;

  // YouTube (watch, shorts, embed, live, youtu.be)
  m = u.match(/^https?:\/\/(?:www\.|m\.)?(?:youtube\.com\/(?:watch\?(?:[^#\s]*&)?v=|shorts\/|embed\/|live\/)|youtu\.be\/)([A-Za-z0-9_-]{6,})/i);
  if (m) return { kind: 'iframe', src: 'https://www.youtube-nocookie.com/embed/' + m[1], label: 'YouTube' };

  // Medal.tv clips. /embed/<id> is gone (404); /clip/<id> redirects to the
  // canonical /games/<game>/clip/<id> page, which allows being framed.
  m = u.match(/^https?:\/\/(?:www\.)?medal\.tv\/(?:[^\s]*\/)?(?:clips?|c)\/([A-Za-z0-9_-]+)/i);
  if (m) return { kind: 'iframe', src: 'https://medal.tv/clip/' + m[1], label: 'Medal.tv' };

  // Twitch clips and VODs (parent is required by Twitch)
  m = u.match(/^https?:\/\/clips\.twitch\.tv\/([A-Za-z0-9_-]+)/i);
  if (m) return { kind: 'iframe', src: 'https://clips.twitch.tv/embed?clip=' + m[1] + '&parent=' + PARENT, label: 'Twitch' };
  m = u.match(/^https?:\/\/(?:www\.)?twitch\.tv\/videos\/(\d+)/i);
  if (m) return { kind: 'iframe', src: 'https://player.twitch.tv/?video=' + m[1] + '&parent=' + PARENT, label: 'Twitch' };

  // Streamable — share (/<id>), embed (/e/<id>) and /o/<id> all map to /e/<id>.
  m = u.match(/^https?:\/\/(?:www\.)?streamable\.com\/(?:[eo]\/)?([A-Za-z0-9]{3,16})(?:[/?#]|$)/i);
  if (m) return { kind: 'iframe', src: 'https://streamable.com/e/' + m[1], label: 'Streamable' };

  // Google Drive — file page -> preview iframe
  m = u.match(/^https?:\/\/(?:drive|docs)\.google\.com\/file\/d\/([A-Za-z0-9_-]+)(?:\/|[?#]|$)/i)
    || u.match(/^https?:\/\/drive\.google\.com\/open\?id=([A-Za-z0-9_-]+)/i);
  if (m) return { kind: 'iframe', src: 'https://drive.google.com/file/d/' + m[1] + '/preview', label: 'Google Drive' };

  // MEGA — file page -> embed iframe (fragment holds the decryption key)
  m = u.match(/^https?:\/\/(?:www\.)?mega\.nz\/(?:file|embed)\/([A-Za-z0-9_-]+)(#[A-Za-z0-9_-]+)?/i);
  if (m) return { kind: 'iframe', src: 'https://mega.nz/embed/' + m[1] + (m[2] || ''), label: 'MEGA' };

  // Dropbox — shared file page -> direct video with raw=1
  m = u.match(/^https?:\/\/(?:www\.)?dropbox\.com\/s(?:cl\/fi)?\/[A-Za-z0-9]+\/[^\s?]*\.(?:mp4|webm|mov|m4v)(?:\?[^\s]*)?$/i);
  if (m) return { kind: 'video', src: dropboxRaw(u), label: 'Dropbox' };

  // Discord CDN / media attachments (including ephemeral ones) -> direct video
  m = u.match(/^https?:\/\/(?:cdn|media)\.discordapp\.(?:net|com)\/(?:ephemeral-)?attachments\/\d+\/\d+\/[^\s?]+\.(?:mp4|webm|mov|m4v)(?:\?[^\s]*)?$/i);
  if (m) return { kind: 'video', src: u, label: 'Discord' };

  // Any direct video file URL (includes raw links from other file hosts)
  if (VIDEO_FILE.test(u)) return { kind: 'video', src: u, label: 'Video' };

  return null;
}
