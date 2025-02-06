from abc import ABC, abstractmethod

class DB(ABC):
    @abstractmethod
    def init_db(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def insert_data(self, data, *args, **kwargs):
        pass
    
    @abstractmethod
    def search_data(self, data, *args, **kwargs):
        pass

    @abstractmethod
    def clear_db(self, *args, **kwargs):
        pass