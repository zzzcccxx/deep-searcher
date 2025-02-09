from abc import ABC
from typing import Dict, List

class ChatResponse(ABC):
    def __init__(self, content: str, total_tokens: int) -> None:
        self.content = content
        self.total_tokens = total_tokens
    
    def __repr__(self) -> str:
        return f"ChatResponse(content={self.content}, total_tokens={self.total_tokens})"

class BaseLLM(ABC):
    def __init__(self):
        pass

    def chat(self, messages: List[Dict]) -> ChatResponse:
        pass
    