import ast
from typing import List

from deeprag.agent.prompt import get_vector_db_search_prompt
# from deeprag.configuration import llm, embedding_model, vector_db
from deeprag import configuration
from deeprag.tools import log


RERANK_PROMPT = """Based on the query questions and the retrieved chunk, to determine whether the chunk is helpful in answering any of the query question, you can only return "YES" or "NO", without any other information.
Query Questions: {query}
Retrieved Chunk: {retrieved_chunk}

Is the chunk helpful in answering the any of the questions?
"""
def search_chunks_from_vectordb(query: str, sub_queries: List[str]):
    vector_db = configuration.vector_db
    llm = configuration.llm
    embedding_model = configuration.embedding_model
    # query_embedding = embedding_model.embed_query(query)
    collection_infos = vector_db.list_collections()
    vector_db_search_prompt = get_vector_db_search_prompt(
        question=query,
        collection_names=[collection_info.collection_name for collection_info in collection_infos],
        collection_descriptions=[collection_info.description for collection_info in collection_infos],
    )
    chat_response = llm.chat(messages=[{"role": "user", "content": vector_db_search_prompt}])
    response_content = chat_response.content.strip()
    if response_content.startswith("```json") and response_content.endswith("```"):
        response_content = response_content[7:-3]
    # try:
    collection_2_query = ast.literal_eval(response_content)
    log.color_print(f"\ncollection_2_query: {collection_2_query}\n")
    # except:
        # log.color_print(f"Failed to parse response: {response_content}\nReturning empty list.")
    
    # If a collection description is not provided, use the query as the search query
    for collection_info in collection_infos:
        if not collection_info.description:
            collection_2_query[collection_info.collection_name] = query
    
    all_retrieved_results = []
    for collection, col_query in collection_2_query.items():
        col_query = query #TODO col_query seems too verbose, use original query instead, need more tests and prompt refinement
        log.color_print(f"\n  Search query in [{collection}]: {col_query}")
        retrieved_results = vector_db.search_data(collection=collection, vector=embedding_model.embed_query(col_query))

        for retrieved_result in retrieved_results:
            chat_response = llm.chat(messages=[{"role": "user", "content": RERANK_PROMPT.format(query=[col_query] + sub_queries, retrieved_chunk=retrieved_result.text)}])
            if chat_response.content.startswith("YES"):
                all_retrieved_results.append(retrieved_result)
                log.color_print("    Chunk Accepted")
            else:
                log.color_print("    Chunk Rejected")
    return all_retrieved_results
    
    # vector_db.search_data(collection="deep_rag", vector=query_embedding)


    