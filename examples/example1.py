import logging
from deepsearcher.offline_loading import load_from_local_files
from deepsearcher.online_query import query
from deepsearcher.configuration import Configuration, init_config

httpx_logger = logging.getLogger("httpx")  # disable openai's logger output
httpx_logger.setLevel(logging.WARNING)


config = Configuration()  #Customize your config here
init_config(config = config)


import glob
all_md_files = glob.glob('/Users/zilliz/Downloads/milvus-docs-2.5.x/site/en/**/*.md', recursive=True)
load_from_local_files(paths_or_directory=all_md_files, collection_name="milvus_docs", collection_description="All Milvus Documents")

question = "Write a report comparing Milvus with other vector databases."
result = query(question)






