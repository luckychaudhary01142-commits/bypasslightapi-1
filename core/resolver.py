from plugins import find_plugin
from core.browser import pool

async def resolve(url: str) -> dict:
    plugin = find_plugin(url)
    page, ctx = await pool.new_page()

    try:
        if plugin.name == "generic_redirect":
            final = await plugin.bypass(url)
        else:
            final = await plugin.bypass(url, page)
    finally:
        await ctx.close()

    return {"plugin": plugin.name, "final_url": final}
