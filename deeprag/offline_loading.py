import os
from typing import List

from tqdm import tqdm

from deeprag.loader.splitter import split_docs_to_chunks
from deeprag.configuration import embedding_model, vector_db, file_loader


def load_from_local_files(paths_or_directory: str | List[str], collection_name: str = None, collection_description: str = None):
    vector_db.init_collection(dim=embedding_model.dimension, collection=collection_name, description=collection_description, force_new_collection=True)
    if isinstance(paths_or_directory, str):
        paths_or_directory = [paths_or_directory]
    all_docs = []
    for path in tqdm(paths_or_directory, desc="Loading files"):
        if os.path.isdir(path):
            docs = file_loader.load_directory(path)
        else:
            docs = file_loader.load_file(path)
        all_docs.extend(docs)
    # print("Splitting docs to chunks...")
    chunks = split_docs_to_chunks(all_docs)

    chunks = embedding_model.embed_chunks(chunks)
    vector_db.insert_data(collection=collection_name, chunks=chunks)


    

def load_from_website(urls: str | List[str], collection_name: str = None, collection_description: str = None):
    ... # TODO move to web_crawler package
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