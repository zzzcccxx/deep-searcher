import unittest
import pprint
import numpy as np
from deepsearcher.vector_db import Milvus, RetrievalResult
from deepsearcher.tools import log


class TestMilvus(unittest.TestCase):
    def test_milvus(self):
        d = 8
        collection = "hellp_deepsearcher"
        milvus = Milvus()
        milvus.init_db(
            dim=d,
            collection=collection,
        )
        rng = np.random.default_rng(seed=19530)
        milvus.insert_data(
            collection=collection,
            rows=[
                RetrievalResult(
                    embedding=rng.random((1, d))[0],
                    text="hello world",
                    reference="local file: hi.txt",
                ),
                RetrievalResult(
                    embedding=rng.random((1, d))[0],
                    text="hello milvus",
                    reference="local file: hi.txt",
                ),
                RetrievalResult(
                    embedding=rng.random((1, d))[0],
                    text="hello deep learning",
                    reference="local file: hi.txt",
                ),
                RetrievalResult(
                    embedding=rng.random((1, d))[0],
                    text="hello llm",
                    reference="local file: hi.txt",
                ),
            ],
        )
        top_2 = milvus.search_data(
            collection=collection, vector=rng.random((1, d))[0], top_k=2
        )
        log.info(pprint.pformat(top_2))

    def test_clear_collection(self):
        d = 8
        collection = "deepsearcher"
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
