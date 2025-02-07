from abc import ABC, abstractmethod
from typing import List

from deeprag.loader.splitter import Chunk

class BaseVectorDB(ABC):
    @abstractmethod
    def init_collection(self, collection: str, description: str, force_new_collection=False, *args, **kwargs):
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