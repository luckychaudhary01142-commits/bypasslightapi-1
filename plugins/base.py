from abc import ABC, abstractmethod
from playwright.async_api import Page

class BasePlugin(ABC):
    name: str = "base"
    domains: list[str] = []

    def matches(self, url: str) -> bool:
        u = url.lower()
        return any(d.lower() in u for d in self.domains)

    @abstractmethod
    async def bypass(self, url: str, page: Page) -> str | None:
        ...
