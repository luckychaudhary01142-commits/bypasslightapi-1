import asyncio
from plugins.base import BasePlugin

SELECTORS = [
    "#btn-main", "#skip_button", "#btn6", "#invisibleCaptchaShortlink",
    "#submit-button", "#continue", "#get-link", "#go-link",
    "button:has-text('Continue')", "button:has-text('Skip')",
    "button:has-text('Get Link')", "button:has-text('Go to Link')",
    "button:has-text('Click Here')", "button:has-text('Proceed')",
    "a:has-text('Continue')", "a:has-text('Skip Ad')",
    "input[type=submit]", ".btn-primary", ".btn-success",
    ".btn-main", ".get-link", "a[href^='http']",
]

TARGET_HINTS = [
    "drive.google", "mega.nz", "mediafire", "pixeldrain",
    "gofile", "youtube", "blogspot", "archive.org",
]

class SmartFallback(BasePlugin):
    name = "smart_fallback"
    domains = []

    async def bypass(self, url, page):
        await page.goto(url, wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(4)

        for sel in SELECTORS:
            try:
                btn = await page.query_selector(sel)
                if btn:
                    await btn.click()
                    await page.wait_for_load_state("networkidle", timeout=15000)
                    await asyncio.sleep(2)
                    break
            except Exception:
                continue

        for _ in range(12):
            await asyncio.sleep(1)
            if any(h in page.url for h in TARGET_HINTS):
                break

        return page.url
