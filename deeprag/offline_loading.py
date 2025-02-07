import os
from typing import List

from deeprag.configuration import Configuration
from deeprag.loader.file_loader import PDFLoader
from deeprag.loader.splitter import split_docs_to_chunks


def load_from_local_files(filepath_or_directorys: str | List[str], collection_name: str = None, collection_description: str = None, config: Configuration = None):
    pdf_loader = PDFLoader()#TODO init from file_loader config
    if isinstance(filepath_or_directorys, str):
        filepath_or_directorys = [filepath_or_directorys]
    all_docs = []
    for filepath_or_directory in filepath_or_directorys:
        if os.path.isdir(filepath_or_directory):
            docs = pdf_loader.load_directory(filepath_or_directory)
        else:
            docs = pdf_loader.load_file(filepath_or_directory)
        all_docs.extend(docs)
    chunks = split_docs_to_chunks(all_docs)
    

def load_from_website(urls: str | List[str], collection_name: str = None, collection_description: str = None):
    ... # move to web_crawler package
    # import os
    # from firecrawl import FirecrawlApp
    # if isinstance(urls, str):
    #     urls = [urls]
    # for url in urls:
    #     app = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))
    #     scrape_status = app.scrape_url(
    #         url,
    #         params={"formats": ["markdown"]},
    #     )
    #     markdown_content = scrape_status["markdown"]
    #     print(markdown_content)