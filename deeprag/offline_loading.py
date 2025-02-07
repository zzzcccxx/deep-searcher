import os
from typing import List

from deeprag.configuration import Configuration, ModuleFactory
from deeprag.loader.splitter import split_docs_to_chunks


def load_from_local_files(paths_or_directory: str | List[str], collection_name: str = None, collection_description: str = None, config: Configuration = None):
    module_factory = ModuleFactory(config)
    vector_db = module_factory.create_vector_db()
    vector_db.init_collection(collection=collection_name, description=collection_description, force_new_collection=True)
    loader = module_factory.create_file_loader()
    if isinstance(paths_or_directory, str):
        paths_or_directory = [paths_or_directory]
    all_docs = []
    for path in paths_or_directory:
        if os.path.isdir(path):
            docs = loader.load_directory(path)
        else:
            docs = loader.load_file(path)
        all_docs.extend(docs)
    chunks = split_docs_to_chunks(all_docs)
    vector_db.insert_data(collection=collection_name, chunks=chunks)


    

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