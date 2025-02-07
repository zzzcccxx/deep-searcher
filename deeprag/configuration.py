from typing import Literal

FeatureType = Literal["llm", "file_loader", "web_crawler", "vector_db"]

class Configuration:
    def __init__(self):
        # Initialize default configurations
        self.settings = {
            "llm": {
                "provider": "DeepSeek",
                "config": {
                    "model": "deepseek-chat"
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

    def set_provider_config(self, feature: FeatureType, provider: str, provider_configs: dict):
        """
        Set the provider and its configurations for a given feature.

        :param feature: The feature to configure (e.g., 'llm', 'file_loader', 'web_crawler').
        :param provider: The provider name (e.g., 'openai', 'deepseek').
        :param provider_configs: A dictionary with configurations specific to the provider.
        """
        if feature not in self.settings:
            raise ValueError(f"Unsupported feature: {feature}")

        self.settings[feature]["provider"] = provider
        self.settings[feature]["config"] = provider_configs


    def get_provider_config(self, feature: FeatureType):
        """
        Get the current provider and configuration for a given feature.

        :param feature: The feature to retrieve (e.g., 'llm', 'file_loader', 'web_crawler').
        :return: A dictionary with provider and its configurations.
        """
        if feature not in self.settings:
            raise ValueError(f"Unsupported feature: {feature}")

        return self.settings[feature]
