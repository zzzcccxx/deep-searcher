import os
from typing import Dict, List
from deepsearcher.llm.base import BaseLLM, ChatResponse


class SiliconFlow(BaseLLM):
    """
    https://docs.siliconflow.cn/quickstart
    """
    def __init__(self, model: str = "deepseek-ai/DeepSeek-V3"):
        from openai import OpenAI as OpenAI_
        self.model = model
        self.client = OpenAI_(api_key=os.getenv("SILICONFLOW_API_KEY"), base_url="https://api.siliconflow.cn/v1")


    def chat(self, messages: List[Dict]) -> ChatResponse:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return ChatResponse(content=completion.choices[0].message.content, total_tokens=completion.usage.total_tokens)

