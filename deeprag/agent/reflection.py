import ast
from typing import List

from deeprag.configuration import llm
from deeprag.agent.prompt import get_reflect_prompt
from deeprag.vector_db.base import RetrievalResult


def generate_gap_queries(original_query: str, all_sub_queries: List[str], all_chunks: List[RetrievalResult]) -> List:
    reflect_prompt = get_reflect_prompt(question=original_query, mini_questions=all_sub_queries, mini_chuncks=[chunk.text for chunk in all_chunks])
    chat_response = llm.chat([{"role": "user", "content": reflect_prompt}])
    return ast.literal_eval(chat_response.content)