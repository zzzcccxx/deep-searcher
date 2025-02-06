import unittest
import pprint
import numpy as np
from deeprag.vector_db import Milvus, MilvusData
from deeprag.tools import log


class TestMilvus(unittest.TestCase):
    def test_milvus(self):
        d = 8
        milvus = Milvus()
        milvus.init_db(
            dim=d,
            uri="https://in01-e7a0f666553484e.aws-us-west-2.vectordb-uat3.zillizcloud.com:19536",
            token="4b3adfb14ce0800147d6f31b64d247a9bdf70589b2b2f3d50fc34e9c582d4578a4bb58838774f52ecf5923bdd2d96ce6a8638719",
        )
        rng = np.random.default_rng(seed=19530)
        milvus.insert_data(
            rows=[
                MilvusData(
                    embedding=rng.random((1, d))[0],
                    text="hello world",
                    reference="local file: hi.txt",
                ),
                MilvusData(
                    embedding=rng.random((1, d))[0],
                    text="hello milvus",
                    reference="local file: hi.txt",
                ),
                MilvusData(
                    embedding=rng.random((1, d))[0],
                    text="hello deep learning",
                    reference="local file: hi.txt",
                ),
                MilvusData(
                    embedding=rng.random((1, d))[0],
                    text="hello llm",
                    reference="local file: hi.txt",
                ),
            ]
        )
        top_2 = milvus.search_data(vector=rng.random((1, d))[0], top_k=2)
        log.info(pprint.pformat(top_2))

    def test_clear_collection(self):
        d = 8
        collection = "deep_rag"
        milvus = Milvus()
        milvus.init_db(
            dim=d,
            only_init_client=True,
            collection=collection,
        )
        milvus.clear_db(collection=collection)
        self.assertFalse(milvus.client.has_collection(collection, timeout=5))


if __name__ == "__main__":
    unittest.main()
