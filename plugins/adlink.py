import asyncio
from plugins.base import BasePlugin

class Adlink(BasePlugin):
    name = "adlink"
    domains = [
        "adrinolinks", "arolinks", "adlink", "adf.ly", "atglinks",
        "clk.sh", "fc.lc", "fc-lc.xyz", "exe.io", "exeygo.com",
        "fajlix.cc", "shortxlinks", "shrinkme", "shrinkearn",
        "clk.ink", "fclc", "fc-lc", "short2url", "earnlinks",
        "clk.ink", "clickscoin", "linkshortify", "lksfy",
    ]

    async def bypass(self, url, page):
        await page.goto(url, wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(3)

        selectors = [
            "#skip_button", "#btn-main", "button:has-text('Skip')",
            "button:has-text('Skip Ad')", "a:has-text('Skip')",
            "button:has-text('Continue')", "button:has-text('Get Link')",
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

        return page.url
