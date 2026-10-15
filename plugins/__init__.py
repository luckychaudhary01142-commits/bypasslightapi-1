from plugins.base import BasePlugin
from plugins.adlink import Adlink
from plugins.gplinks import GPLinks
from plugins.ouo import Ouo
from plugins.softurl import SoftUrl
from plugins.generic_redirect import GenericRedirect
from plugins.smart_fallback import SmartFallback

PLUGINS = [
    Adlink(),
    GPLinks(),
    Ouo(),
    SoftUrl(),
    GenericRedirect(),
]

FALLBACK = SmartFallback()

def find_plugin(url: str):
    for p in PLUGINS:
        if p.matches(url):
            return p
    return FALLBACK
