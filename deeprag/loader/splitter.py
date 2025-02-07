## Sentence Window splitting strategy, ref:
#  https://github.com/milvus-io/bootcamp/blob/master/bootcamp/RAG/advanced_rag/sentence_window_with_langchain.ipynb

from langchain_core.documents import Document


class Chunk(Document):
    def __init__(self, text: str, metadata: dict = None, wider_text: str = None):
        super().__init__(text, metadata)
        self.wider_text = wider_text


from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter



def _write_wider_window(
    split_docs: List[Document], original_document: Document, offset: int = 200
) -> List[Chunk]:
    chunks = []
    original_text = original_document.page_content
    for doc in split_docs:
        doc_text = doc.page_content
        start_index = original_text.index(doc_text)
        end_index = start_index + len(doc_text) - 1
        wider_text = original_text[
            max(0, start_index - offset) : min(len(original_text), end_index + offset)
        ]
        chunk = Chunk(page_content=doc_text, metadata=doc.metadata, wider_text=wider_text)
        chunks.append(chunk)
    return chunks



def split_docs_to_chunks(documents: List[Document], chunk_size: int = 1500, chunk_overlap=100) -> List[Chunk]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return _write_wider_window(docs, documents[0], offset=300)
