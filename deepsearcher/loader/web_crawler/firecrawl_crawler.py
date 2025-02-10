import os
from typing import List

from firecrawl import FirecrawlApp
from langchain_core.documents import Document

from deepsearcher.loader.web_crawler.base import BaseCrawler


class FireCrawlCrawler(BaseCrawler):
    def __init__(self, **kwargs):
        self.app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    def craw_url(self, url: str) -> List[Document]:
        scrape_status = self.app.scrape_url(
            url,
            params={"formats": ["markdown"]},
        )
        markdown_content = scrape_status["markdown"]
        # print(markdown_content)
        ...# TODO: convent markdown to Document object