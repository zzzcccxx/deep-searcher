from typing import List
from langchain_core.documents import Document
from deeprag.loader.file_loader.base import BaseLoader



class PDFLoader(BaseLoader):
    def __init__(self):
        pass

    def load_file(self, file_path: str) -> List[Document]:
        import pdfplumber
        with pdfplumber.open(file_path) as file:
            page_content = "\n\n".join([page.extract_text() for page in file.pages])
            return [Document(page_content=page_content, metadata={"source": file_path})]

    @property
    def supported_file_types(self) -> List[str]:
        return ["pdf"]