from typing import List
from openai._types import NOT_GIVEN
from deepsearcher.embedding.base import BaseEmbedding


OPENAI_MODEL_DIM_MAP = {
    "text-embedding-ada-002": 1536,
    "text-embedding-3-small": 1536,
    "text-embedding-3-large": 3072,
}


class OpenAIEmbedding(BaseEmbedding):
    """
    https://platform.openai.com/docs/guides/embeddings/use-cases
    """

    def __init__(self, model_name: str = "text-embedding-ada-002"):
        """

        Args:
            model_name (`str`):
                Can be one of the following:
                    'text-embedding-ada-002': No dimension needed, default is 1536,
                    'text-embedding-3-small': dimensions from 512 to 1536, default is 1536,
                    'text-embedding-3-large': dimensions from 1024 to 3072, default is 3072,
        """
        from openai import OpenAI

        self.client = OpenAI()
        self.model_name = model_name

    def embed_query(self, text:str, dimensions=NOT_GIVEN) -> List[float]:
        text = text.replace("\n", " ")
        return self.client.embeddings.create(input=[text], model=self.model_name, dimensions=dimensions).data[0].embedding
    @property
    def dimension(self) -> int:
        return OPENAI_MODEL_DIM_MAP[self.model_name]
