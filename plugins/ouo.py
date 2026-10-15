import asyncio
from plugins.base import BasePlugin

class Ouo(BasePlugin):
    name = "ouo"
    domains = ["ouo.io", "ouo.press", "ouo.pw"]

    async def bypass(self, url, page):
        await page.goto(url, wait_until="domcontentloaded", timeout=45000)
        await asyncio.sleep(5)

        try:
            btn = await page.query_selector(
                "button.btn-main, #btn-main, input[type=submit], "
                "button:has-text('Continue')"
            )
            if btn:
                await btn.click()
                await page.wait_for_load_state("networkidle", timeout=20000)
                await asyncio.sleep(2)
        except Exception:
            pass

        return page.url
