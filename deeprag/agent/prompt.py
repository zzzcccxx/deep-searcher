from typing import List


def get_vector_db_search_prompt(
    question: str,
    collection_names: List[str],
    collection_descriptions: List[str],
    context: List[str] = None,
):
    sections = []
    # common prompt
    common_prompt = f"""You are an advanced AI problem analyst. Use your reasoning ability and historical conversation information, based on all the existing data sets, to get absolutely accurate answers to the following questions, and generate a suitable question for each data set according to the data set description that may be related to the question.

Question: {question}
"""
    sections.append(common_prompt)
    
    # data set prompt
    data_set = []
    for i, collection_name in enumerate(collection_names):
        data_set.append(f"{collection_name}: {collection_descriptions[i]}")
    data_set_prompt = f"""The following is all the data set information. The format of data set information is data set name: data set description.

Data Sets And Descriptions:
"""
    sections.append(data_set_prompt + "\n".join(data_set))
    
    # context prompt
    if context:
        context_prompt = f"""The following is a condensed version of the historical conversation. This information needs to be combined in this analysis to generate questions that are closer to the answer. You must not generate the same or similar questions for the same data set, nor can you regenerate questions for data sets that have been determined to be unrelated.

Historical Conversation:
"""
        sections.append(context_prompt + "\n".join(context))
    
    # response prompt
    response_prompt = f"""Based on the above, you can only select a few datasets from the following dataset list to generate appropriate related questions for the selected datasets in order to solve the above problems. The output format is json, where the key is the name of the dataset and the value is the corresponding generated question.

Data Sets:
"""
    sections.append(response_prompt + "\n".join(collection_names))
    
    footer = """Respond exclusively in valid JSON format matching exact JSON schema.

Critical Requirements:
- Include ONLY ONE action type
- Never add unsupported keys
- Exclude all non-JSON text, markdown, or explanations
- Maintain strict JSON syntax"""
    sections.append(footer)
    return "\n\n".join(sections)


def get_reflect_prompt(
   question: str,
   collections: List[str],
   mini_questions: List[str],
   mini_chuncks: List[str],
):
    sections = []
    common_prompt = f"""You are an AI expert in content judgment and analysis, and are good at judging whether there is a correlation between the question and the content. At present, we have the following information. The core needs to focus on solving the following main problem and analyzing whether other related problems and content are helpful to answer this question.

Main Question: {question}
"""
    sections.append(common_prompt)
    
    related_set = []
    for i, collection_name in enumerate(collections):
        related_set.append(f"""Question {i}: {mini_questions[i]}
Data Set Name: {collection_name}
Related Content: {mini_chuncks[i]}
""")
    related_prompt = f"""The following is a series of related questions and their corresponding content.

Related Questions And Content List:
"""
    sections.append(related_prompt + "\n".join(related_set))
    
    response_prompt = f"""Based on the above, please analyze whether the content of these related questions is related to the main question and whether it can help answer the main question.The output content is a json.
    
If the current related content is sufficient to accurately and completely answer the main question, an empty json is returned. Otherwise,

according to the related content, all related questions and content are first analyzed to see if they are related to the question. The judgment result is stored in the first-level key of the json. The key is **related_content**, and the value is a sub-json. The key of this sub-json is the related question content, and the value is YES or NO. If the question and content are helpful in answering the main question, it is YES, otherwise NO. 

After analyzing the association relationship, if the current relevant content of the question is not enough to answer the current question, please generate multiple related small questions. The result is stored in the first-level key of the json. The key is miss_questions, and the value is a string array.
"""
    sections.append(response_prompt)
    
    footer = """Respond exclusively in valid JSON format matching exact JSON schema.

Critical Requirements:
- Include ONLY ONE action type
- Never add unsupported keys
- Exclude all non-JSON text, markdown, or explanations
- Maintain strict JSON syntax"""
    sections.append(footer)
    
    return "\n\n".join(sections)


def get_final_answer_prompt(
   question: str, 
   collections: List[str],
   mini_questions: List[str],
   mini_chuncks: List[str],
):
    sections = []
    common_prompt = f"""You are a AI content analysis expert, good at summarizing content. After many attempts, we have obtained the answers to the following questions. Please summarize a simple and clear answer based on the following series of related questions and their corresponding contents.

Question: {question}
"""
    sections.append(common_prompt)
    
    data_set = []
    for i, collection_name in enumerate(collections):
        data_set.append(f"""Question {i}: {mini_questions[i]}
Data Set Name: {collection_name}
Origin Content: {mini_chuncks[i]}
""")
    data_set_prompt = f"""The following is a series of related questions and their corresponding content.

Related Questions And Answers List:
"""
    sections.append(data_set_prompt + "\n".join(data_set))
    
    response_prompt = f"""Based on the above, please provide a simple, clear and complete answer to the question. The answers can only be rewritten by sentences, and the answers need to explain which dataset sources and original content this part refers to. No additional expansion, extension or explanation can be made.
"""
    sections.append(response_prompt)
    
    return "\n\n".join(sections)
