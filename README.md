# DeepSearcher

DeepSearcher combines powerful LLMs (DeepSeek, OpenAI, etc.) and Vector Databases (Milvus, etc.) to perform search, evaluation, and reasoning based on private data, providing highly accurate answer and comprehensive report. This project is suitable for enterprise knowledge management, intelligent Q&A systems, and information retrieval scenarios.

![Architecture](./assets/pic/deep-searcher-arch.png)

## 🚀 Features

- **Private Data Search**: Maximizes the utilization of enterprise internal data while ensuring data security. When necessary, it can integrate online content for more accurate answers.
- **Vector Database Management**: Supports Milvus and other vector databases, allowing data partitioning for efficient retrieval.
- **Flexible Embedding Options**: Compatible with multiple embedding models for optimal selection.
- **Multiple LLM Support**: Supports DeepSeek, OpenAI, and other large models for intelligent Q&A and content generation.
- **Document Loader**: Supports local file loading, with web crawling capabilities under development.

---

## 🎉 Demo
![demo](./assets/pic/demo.gif)


## 📖 Quick Start

### Installation
Install DeepSearcher using pip:
```bash
# Clone the repository
git clone https://github.com/zilliztech/deep-searcher.git

# Recommended: Create a Python virtual environment

# Install dependencies
cd deep-searcher 
pip install -e .
```
### Quick start demo
```python
from deepsearcher.configuration import Configuration, init_config
from deepsearcher.online_query import query

config = Configuration()

# Customize your config here,
# more configuration see the Configuration Details section below.
config.set_provider_config("llm", "OpenAI", {"model": "gpt-4o-mini"})
init_config(config = config)

# Load your local data
from deepsearcher.offline_loading import load_from_local_files
load_from_local_files(paths_or_directory=your_local_path)

# Query
result = query("Write a report about xxx.") # Your question here
```
### Configuration Details:
#### LLM Configuration

  <pre><code>
config.set_provider_config("llm", "(LLMName)", "(Arguments dict)")
</code></pre>
<p>The "LLMName" can be one of the following: ["DeepSeek", "OpenAI", "SiliconFlow", "TogetherAI"]</p>
<p> The "Arguments dict" is a dictionary that contains the necessary arguments for the LLM class.</p>

<details>
  <summary>Example (OpenAI)</summary>
    <pre><code>
config.set_provider_config("llm", "OpenAI", {"model": "gpt-4o"})
    </code></pre>
    <p> More details about OpenAI models: https://platform.openai.com/docs/models </p>
</details>

<details>
  <summary>Example (DeepSeek from official)</summary>
    <pre><code>
config.set_provider_config("llm", "DeepSeek", {"model": "deepseek-chat"})
    </code></pre>
    <p> More details about DeepSeek: https://api-docs.deepseek.com/ </p>
</details>

<details>
  <summary>Example (DeepSeek from SiliconFlow)</summary>
    <pre><code>
config.set_provider_config("llm", "SiliconFlow", {"model": "deepseek-ai/DeepSeek-V3"})
    </code></pre>
    <p> More details about SiliconFlow: https://docs.siliconflow.cn/quickstart </p>
</details>

<details>
  <summary>Example (DeepSeek from TogetherAI)</summary>
    <pre><code>
config.set_provider_config("llm", "TogetherAI", {"model": "deepseek-ai/DeepSeek-V3"})
    </code></pre>
    <p> More details about TogetherAI: https://www.together.ai/ </p>
</details>





### Python CLI Mode (Coming Soon)

---

## 🔧 Module Support

### 🔹 Embedding Models
- Pymilvus built-in embedding model
- OpenAI
- VoyageAI

### 🔹 LLM Support
- DeepSeek
- OpenAI

### 🔹 Document Loader
- Local File
- Web Crawler (Under Development)

### 🔹 Vector Database Support
- Milvus

---

## 📌 Future Plans
- Enhance web crawling functionality
- Support more vector databases (e.g., FAISS...)
- Add support for additional large models
- Provide RESTful API interface

We welcome contributions! Star & Fork the project and help us build a more powerful DeepSearcher! 🎯