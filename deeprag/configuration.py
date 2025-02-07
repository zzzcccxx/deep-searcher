from typing import Literal

from deeprag.llm.base import BaseLLM
from deeprag.loader.file_loader.base import BaseLoader
from deeprag.loader.web_crawler.base import BaseCrawler
from deeprag.vector_db.base import BaseVectorDB

FeatureType = Literal["llm", "file_loader", "web_crawler", "vector_db"]

class Configuration:
    def __init__(self):
        # Initialize default configurations
        self.provide_settings = {
            "llm": {
                "provider": "TogetherAI",
                "config": {
                    "model": "deepseek-ai/DeepSeek-V3"
                }
            },
            "file_loader": {
                "provider": "PDFLoader",
                "config": {}
            },
            "web_crawler": {
                "provider": "Firecrawl",
                "config": {}
            },
            "vector_db": {
                "provider": "Milvus",
                "config": {
                    "uri": "./milvus.db"
                }
            }
        }
        self.query_settings = {
            "max_iter": 8
        }

    def set_provider_config(self, feature: FeatureType, provider: str, provider_configs: dict):
        """
        Set the provider and its configurations for a given feature.

        :param feature: The feature to configure (e.g., 'llm', 'file_loader', 'web_crawler').
        :param provider: The provider name (e.g., 'openai', 'deepseek').
        :param provider_configs: A dictionary with configurations specific to the provider.
        """
        if feature not in self.provide_settings:
            raise ValueError(f"Unsupported feature: {feature}")

        self.provide_settings[feature]["provider"] = provider
        self.provide_settings[feature]["config"] = provider_configs


    def get_provider_config(self, feature: FeatureType):
        """
        Get the current provider and configuration for a given feature.

        :param feature: The feature to retrieve (e.g., 'llm', 'file_loader', 'web_crawler').
        :return: A dictionary with provider and its configurations.
        """
        if feature not in self.provide_settings:
            raise ValueError(f"Unsupported feature: {feature}")

        return self.provide_settings[feature]

class ModuleFactory:
    def __init__(self, config: Configuration):
        self.config = config
    
    def _create_module_instance(self, feature: FeatureType, module_name: str):
        # e.g.
        # feature = "file_loader"
        # module_name = "deeprag.loader.file_loader"
        class_name = self.config.provide_settings[feature]["provider"]
        module = __import__(module_name, fromlist=[class_name])
        class_ = getattr(module, class_name)
        return class_(**self.config.provide_settings[feature]["config"])
    
    def create_llm(self) -> BaseLLM:
        return self._create_module_instance("llm", "deeprag.llm")
    
    def create_file_loader(self) -> BaseLoader:
        return self._create_module_instance("file_loader", "deeprag.loader.file_loader")
    
    def create_web_crawler(self) -> BaseCrawler:
        return self._create_module_instance("web_crawler", "deeprag.loader.web_crawler")
    
    def create_vector_db(self) -> BaseVectorDB:
        return self._create_module_instance("vector_db", "deeprag.vector_db")