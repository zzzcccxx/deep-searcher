from abc import ABC, abstractmethod
from typing import List

import numpy as np

from deeprag.loader.splitter import Chunk

class RetrievalResult:
    def __init__(
        self,
        embedding: np.array,
        text: str,
        reference: str,
        metadata: dict,
        score: float = 0.0,
    ):
        self.embedding = embedding
        self.text = text
        self.reference = reference
        self.metadata = metadata
        self.score: float = score

    def __repr__(self):
        return f"RetrievalResult(score={self.score}, embedding={self.embedding}, text={self.text}, reference={self.reference}), metadata={self.metadata}"




class BaseVectorDB(ABC):
    @abstractmethod
    def init_collection(self, dim: int, collection: str, description: str, force_new_collection=False, *args, **kwargs):
        pass
    
    @abstractmethod
    def insert_data(self, collection: str, chunks: List[Chunk], *args, **kwargs):
        pass
    
    @abstractmethod
    def search_data(self, collection: str, data, *args, **kwargs):
        pass

    @abstractmethod
    def clear_db(self, *args, **kwargs):
        pass
