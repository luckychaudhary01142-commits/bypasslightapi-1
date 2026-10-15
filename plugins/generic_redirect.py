import httpx
from plugins.base import BasePlugin

class GenericRedirect(BasePlugin):
    name = "generic_redirect"
    domains = [
        "bit.ly", "tinyurl.com", "t.co", "cutt.ly", "shorturl.at",
        "youtu.be", "youtube.com", "m.youtube.com", "youtube-nocookie.com",
        "drive.google.com", "drive.usercontent.google.com",
        "pixeldrain.com", "pixeldrain.dev", "gofile.io",
        "mediafire.com", "mega.nz", "transfer.it",
    ]

    async def bypass(self, url, page=None):
        async with httpx.AsyncClient(follow_redirects=True, timeout=25) as c:
            r = await c.get(url, headers={"User-Agent": "Mozilla/5.0"})
            return str(r.url)
