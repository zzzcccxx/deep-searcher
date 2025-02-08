from deeprag.offline_loading import load_from_local_files, load_from_website
from deeprag.online_query import naive_rag_query, query
from deeprag.configuration import Configuration, init_config

config = Configuration()
init_config(config = config)


# import glob
# all_md_files = glob.glob('/Users/zilliz/Downloads/milvus-docs-2.5.x/site/en/**/*.md', recursive=True)
# load_from_local_files(all_md_files, collection_name="milvus_docs", collection_description="All Milvus Documents")

# load_from_local_files("./examples/data/Paul Graham's essay.txt", collection_name="personal_essay", collection_description="An essay by Paul Graham.")
# load_from_local_files("./examples/data/WhatisMilvus.pdf", collection_name="what_is_milvus", collection_description="An PDF document that introduce the Milvus features.")
# load_from_local_files("/Users/zilliz/zilliz/bootcamp/bootcamp/tutorials/integration/milvus_docs/en/embeddings", collection_name="milvus_embedding_docs", collection_description="Documentation of Milvus Embeddings")

# load_from_website(["https://milvus.io/docs/release_notes.md"], collection_name="milvus_docs")

# result = query("what is the new feature of Milvus 2.5.4?", max_iter=config.query_settings["max_iter"])
# question = "How to use OpenAI embedding in milvus model?"
question = "Write a report comparing Milvus with other vector databases."
result = query(question, max_iter=config.query_settings["max_iter"])
naive_rag_result = naive_rag_query(question, top_k=13)
print("==== NAIVE RAG RESULT ====")
print(naive_rag_result)






