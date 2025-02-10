import os
from typing import List

from langchain_core.documents import Document
from deepsearcher.loader.web_crawler.base import BaseCrawler


class JinaCrawler(BaseCrawler):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass
    def craw_url(self, url: str) -> List[Document]:
        pass



