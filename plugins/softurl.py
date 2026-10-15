import asyncio
from plugins.base import BasePlugin

class SoftUrl(BasePlugin):
    name = "softurl"
    domains = ["softurl.in", "softurl"]

    async def bypass(self, url, page):
        await page.goto(url, wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(3)

        selectors = [
            "#btn-main", "#btn6", "button:has-text('Continue')",
            "button:has-text('Get Link')", "a:has-text('Continue')",
            "input[type=submit]", ".btn-primary", ".btn-success",
        ]
        for sel in selectors:
            try:
                btn = await page.query_selector(sel)
                if btn:
                    await btn.click()
                    await page.wait_for_load_state("networkidle", timeout=20000)
                    await asyncio.sleep(2)
                    break
            except Exception:
                continue

        for _ in range(15):
            await asyncio.sleep(1)
            if any(d in page.url for d in [
                "drive.google", "mega.nz", "mediafire",
                "youtube", "blogspot",
            ]):
                break

        return page.url
