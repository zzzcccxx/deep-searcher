import ast

from deeprag.agent.prompt import get_vector_db_search_prompt
from deeprag.configuration import llm, embedding_model, vector_db



RERANK_PROMPT = """Based on the query question and the retrieved chunk, to determine whether the chunk is helpful in answering the question, you can only return "YES" or "NO", without any other information
Query: {query}
Retrieved Chunk: {retrieved_chunk}

Is the chunk helpful in answering the question?
"""
def search_chunks_from_vectordb(query: str):
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
    # except:
        # print(f"Failed to parse response: {response_content}\nReturning empty list.")
    all_retrieved_results = []
    for collection, query in collection_2_query.items():
        retrieved_results = vector_db.search_data(collection=collection, vector=embedding_model.embed_query(query))

        for retrieved_result in retrieved_results:
            chat_response = llm.chat(messages=[{"role": "user", "content": RERANK_PROMPT.format(query=query, retrieved_chunk=retrieved_result.text)}])
            if chat_response.content.startswith("YES"):
                all_retrieved_results.append(retrieved_result)
    return all_retrieved_results
    
    # vector_db.search_data(collection="deep_rag", vector=query_embedding)


    