from deeprag.offline_loading import load_from_local_files, load_from_website
from deeprag.online_query import naive_rag_query, query
from deeprag.configuration import config

# load_from_local_files("./examples/data/Paul Graham's essay.txt", collection_name="personal_essay")
load_from_local_files("./examples/data/WhatisMilvus.pdf", collection_name="what_is_milvus", collection_description="An PDF document that introduce the Milvus features.")

# load_from_website(["https://milvus.io/docs/release_notes.md"], collection_name="milvus_docs")

# result = query("what is the new feature of Milvus 2.5.4?", max_iter=config.query_settings["max_iter"])
question = "How to use OpenAI embedding in milvus model?"
result = query(question, max_iter=config.query_settings["max_iter"])
naive_rag_result = naive_rag_query(question)
print("==== NAIVE RAG RESULT ====")
print(naive_rag_result)