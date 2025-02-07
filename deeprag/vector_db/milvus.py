import numpy as np
from typing import List

from deeprag.loader.splitter import Chunk
from deeprag.vector_db.base import BaseVectorDB
from deeprag.tools import log
from pymilvus import MilvusClient, DataType


class MilvusData:
    def __init__(
        self, embedding: np.array, text: str, reference: str, metadata: dict, score: float = 0.0
    ):
        self.embedding = embedding
        self.text = text
        self.reference = reference
        self.metadata = metadata
        self.score: float = score

    def __repr__(self):
        return f"MilvusData(score={self.score}, embedding={self.embedding}, text={self.text}, reference={self.reference}), metadata={self.metadata}"


class Milvus(BaseVectorDB):
    """Milvus class is a subclass of DB class."""

    client: MilvusClient = None

    def __init__(
        self,
        uri: str = "http://localhost:19530",
        token: str = "root:Milvus",
        db: str = "default",
    ):
        self.client = MilvusClient(uri=uri, token=token, db_name=db, timeout=30)
        from pymilvus import model
        # This will download "all-MiniLM-L6-v2", a light weight model.
        self.embedding_model = model.DefaultEmbeddingFunction()
        self.dim = self.embedding_model.dim

    def init_collection(
        self,
        collection: str = "deep_rag",
        description: str = "",
        force_new_collection: bool = False,
        text_max_length: int = 65_535,
        reference_max_length: int = 2048,
        metric_type: str = "L2",
        *args,
        **kwargs,
    ):
        try:
            has_collection = self.client.has_collection(collection, timeout=5)
            if force_new_collection and has_collection:
                self.client.drop_collection(collection)
            if has_collection:
                return
            schema = self.client.create_schema(
                enable_dynamic_field=False, auto_id=True, description=description
            )
            schema.add_field("id", DataType.INT64, is_primary=True)
            schema.add_field("embedding", DataType.FLOAT_VECTOR, dim=self.dim)
            schema.add_field("text", DataType.VARCHAR, max_length=text_max_length)
            schema.add_field(
                "reference", DataType.VARCHAR, max_length=reference_max_length
            )
            schema.add_field("metadata", DataType.JSON)
            index_params = self.client.prepare_index_params()
            index_params.add_index(field_name="embedding", metric_type=metric_type)
            self.client.create_collection(
                collection,
                schema=schema,
                index_params=index_params,
                consistency_level="Strong",
            )
        except Exception as e:
            log.critical(f"fail to init db for milvus, error info: {e}")

    def insert_data(self, collection: str, chunks: List[Chunk], *args, **kwargs):
        texts = [chunk.text for chunk in chunks]
        references = [chunk.reference for chunk in chunks]
        metadatas = [chunk.metadata for chunk in chunks]
        embeddings = self.embedding_model.encode_documents(texts)

        try:
            datas = [
                {
                    "embedding": embedding,
                    "text": text,
                    "reference": reference,
                    "metadata": metadata,
                }
                for embedding, text, reference, metadata in zip(embeddings, texts, references, metadatas)
            ]
            self.client.insert(collection_name=collection, data=datas)
        except Exception as e:
            log.critical(f"fail to insert data, error info: {e}")

    def search_data(
        self, collection: str, vector: np.array, top_k: int = 5, *args, **kwargs
    ) -> List[MilvusData]:
        try:
            search_results = self.client.search(
                collection_name=collection,
                data=[vector],
                limit=top_k,
                output_fields=["*"],
                timeout=10,
            )

            return [
                MilvusData(
                    embedding=b["entity"]["embedding"],
                    text=b["entity"]["text"],
                    reference=b["entity"]["reference"],
                    score=b["distance"],
                    metadata=b["entity"]["metadata"],
                )
                for a in search_results
                for b in a
            ]
        except Exception as e:
            log.critical(f"fail to search data, error info: {e}")

    def clear_db(self, collection: str = "deep_rag", *args, **kwargs):
        try:
            self.client.drop_collection(collection)
        except Exception as e:
            log.warning(f"fail to clear db, error info: {e}")
