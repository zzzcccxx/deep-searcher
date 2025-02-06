from typing import List


def get_vector_db_search_prompt(
    question: str,
    collections: List[str],
    context: List[str] = None,
):
    """_summary_

    Args:
        question (str): the question to be asked
        collections (List[str]): all collections in the database, the str should be "collection name: collection description"
        context (List[str], optional): history chat. Defaults to None.

    Returns:
        _type_: _description_
    """
    return ""


def get_reflect_prompt(
   question: str, 
   mini_questions: List[str],
   mini_answers: List[str],
):
    return ""


def get_final_answer_prompt(
   question: str, 
   mini_questions: List[str],
   mini_answers: List[str], 
):
    return ""
