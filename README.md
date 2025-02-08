# Deep RAG Agent

Deep RAG Agent combines Large Language Models (LLMs) and Vector Databases to perform search, evaluation, and reasoning based on private data, providing highly accurate answers. This project is suitable for enterprise knowledge management, intelligent Q&A systems, and information retrieval scenarios.

![Architecture](./assets/pic/deep-rag-agent-arch.png)

## 🚀 Features

- **Private Data Search**: Maximizes the utilization of enterprise internal data while ensuring data security. When necessary, it can integrate online content for more accurate answers.
- **Vector Database Management**: Supports Milvus and other vector databases, allowing data partitioning for efficient retrieval.
- **Flexible Embedding Options**: Compatible with multiple embedding models for optimal selection.
- **Multiple LLM Support**: Supports DeepSeek, OpenAI, and other large models for intelligent Q&A and content generation.
- **Document Loader**: Supports local file loading, with web crawling capabilities under development.

---

## 🎉 Demo
![demo](./demo.gif)


## 📖 Quick Start

### Local Mode

```bash
# Clone the repository
git clone https://github.com/zilliztech/deep-rag-agent.git

# Recommended: Create a Python virtual environment

# Install dependencies
cd deep-rag-agent 
pip install -e .

# Configure LLM or Milvus
code examples/example1.py

# Prepare data and run an example
python examples/example1.py
```

💡 **Hint**: Refer to the `examples` directory to import your private data and build your customized Deep RAG Agent.

### Python Package Mode (Coming Soon)

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

We welcome contributions! Star & Fork the project and help us build a more powerful Deep RAG Agent! 🎯