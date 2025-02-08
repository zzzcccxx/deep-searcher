from typing import List

# from deeprag.configuration import llm
from deeprag.agent.prompt import get_final_answer_prompt
from deeprag.vector_db.base import RetrievalResult
from deeprag import configuration

def generate_final_answer(original_query: str, all_sub_queries: List[str], all_chunks: List[RetrievalResult]) -> str:
    llm = configuration.llm
    chunk_texts = []
    for chunk in all_chunks:
        if "wider_text" in chunk.metadata:
            chunk_texts.append(chunk.metadata["wider_text"])
        else:
            chunk_texts.append(chunk.text)
    print(f"Summarize answer from all {len(all_chunks)} retrieved chunks...")
    summary_prompt = get_final_answer_prompt(question=original_query, mini_questions=all_sub_queries, mini_chuncks=chunk_texts)
    chat_responese = llm.chat([{"role": "user", "content": summary_prompt}])
    return chat_responese.content