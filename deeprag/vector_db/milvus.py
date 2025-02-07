import numpy as np
from typing import List
from .db import DB
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


class Milvus(DB):
    """Milvus class is a subclass of DB class."""

    client: MilvusClient = None

    def __init__(
        self,
        uri: str = "http://localhost:19530",
        token: str = "root:Milvus",
        db: str = "default",
    ):
        self.client = MilvusClient(uri=uri, token=token, db_name=db, timeout=30)

    def init_db(
        self,
        dim: int,
        collection: str = "deep_rag",
        force_new_collection: bool = False,
        text_max_length: int = 1024,
        reference_max_length: int = 256,
        metric_type: str = "L2",
        description: str = "",
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
            schema.add_field("embedding", DataType.FLOAT_VECTOR, dim=dim)
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

    def insert_data(self, collection: str, rows: List[MilvusData], *args, **kwargs):
        try:
            datas = [
                {
                    "embedding": row.embedding,
                    "text": row.text,
                    "reference": row.reference,
                    "metadata": row.metadata,
                }
                for row in rows
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
