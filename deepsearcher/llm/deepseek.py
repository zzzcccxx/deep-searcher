import os
from typing import Dict, List
from deepsearcher.llm.base import BaseLLM, ChatResponse


class DeepSeek(BaseLLM):
    """
    https://api-docs.deepseek.com/
    """
    def __init__(self, model: str = "deepseek-chat"):
        from openai import OpenAI as OpenAI_
        self.model = model
        self.client = OpenAI_(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")


    def chat(self, messages: List[Dict]) -> ChatResponse:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return ChatResponse(content=completion.choices[0].message.content, total_tokens=completion.usage.total_tokens)

