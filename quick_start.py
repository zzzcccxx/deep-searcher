from deepsearcher.configuration import Configuration, init_config
from deepsearcher.online_query import query

config = Configuration()

# Customize your config here,
# more configuration see the Configuration Details section below.
config.set_provider_config("llm", "GLM", {"model": "glm-4-plus"})
config.set_provider_config("embedding", "GLMEmbedding", {"model": "embedding-3"})
init_config(config = config)

# Load your local data
from deepsearcher.offline_loading import load_from_local_files
load_from_local_files(paths_or_directory='/workspaces/deep-searcher/data/TZ-91005-9_U形衣通结构规范_A1版.pdf')

# (Optional) Load from web crawling (`FIRECRAWL_API_KEY` env variable required)
# from deepsearcher.offline_loading import load_from_website
# load_from_website(urls=website_url)

# Query
result = query("请问该产品的参数是多少？") # Your question here