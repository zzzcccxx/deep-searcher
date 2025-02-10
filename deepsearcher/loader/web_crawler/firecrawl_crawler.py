import os
from typing import List

from firecrawl import FirecrawlApp
from langchain_core.documents import Document

from deepsearcher.loader.web_crawler.base import BaseCrawler


class FireCrawlCrawler(BaseCrawler):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    def crawl_url(self, url: str) -> List[Document]:
        scrape_result = self.app.scrape_url(
            url,
            params={"formats": ["markdown"]},
        )

        markdown_content = scrape_result.get('markdown', '')
        source_url = scrape_result.get('metadata', {}).get('sourceURL', url)
        metadata = scrape_result.get('metadata', {})
        metadata['reference'] = source_url

        return [Document(page_content=markdown_content, metadata=metadata)]