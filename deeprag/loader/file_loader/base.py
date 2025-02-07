import os
from typing import List
from langchain_core.documents import Document


class BaseLoader:
    def __init__(self, **kwargs):
        pass

    def load_file(self, file_path: str) -> List[Document]:
        pass

    def load_directory(self, directory: str) -> List[Document]:
            documents = []
            for file in os.listdir(directory):
                for suffix in self.supported_file_types:
                    if file.endswith(suffix):
                        documents.extend(self.load(os.path.join(directory, file)))

    @property
    def supported_file_types(self) -> List[str]:
        pass