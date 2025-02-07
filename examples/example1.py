from deeprag.configuration import Configuration
from deeprag.offline_loading import load_from_local_files, load_from_website
from deeprag.online_query import query

config = Configuration()
# load_from_local_files("./examples/data/Paul Graham's essay.txt", collection_name="personal_essay")
load_from_local_files("./examples/data/WhatisMilvus.pdf", collection_name="what_is_milvus", collection_description="An PDF document that introduce the Milvus features.", config=config)

# load_from_website(["https://milvus.io/docs/release_notes.md"], collection_name="milvus_docs")

query("what is the new feature of Milvus 2.5.4?")
