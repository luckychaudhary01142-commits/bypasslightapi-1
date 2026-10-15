from playwright.async_api import async_playwright

ADBLOCK_KILLER = """
Object.defineProperty(window, 'canRunAds', { get: () => true });
Object.defineProperty(window, 'adsbygoogle', { value: { loaded: true } });
Object.defineProperty(window, 'adblock', { get: () => false });
window.showAds = () => true;
"""

class BrowserPool:
    def __init__(self):
        self._pw = None
        self._browser = None

    async def start(self):
        self._pw = await async_playwright().start()
        self._browser = await self._pw.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-blink-features=AutomationControlled",
                "--disable-dev-shm-usage",
            ],
        )

    async def stop(self):
        if self._browser:
            await self._browser.close()
        if self._pw:
            await self._pw.stop()

    async def new_page(self):
        ctx = await self._browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1366, "height": 768},
            locale="en-US",
        )
        await ctx.add_init_script(ADBLOCK_KILLER)
        page = await ctx.new_page()
        return page, ctx

pool = BrowserPool()
