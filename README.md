# MultiPdf-Chat-Bot

## Project Overview

This project is a web application that leverages natural language processing (NLP) and similarity search capabilities using Sentence Transformers and Faiss. The app is built with Streamlit and includes features such as PDF processing, text embeddings, and similarity searches. It supports the use of OpenAI and HuggingFace models for embedding generation.

## Features

- **PDF Processing**: Extract text from PDF documents.
- **Text Embeddings**: Generate text embeddings using Sentence Transformers.
- **Similarity Search**: Perform similarity searches using Faiss.
- **Support for Multiple Embedding Models**: Use both OpenAI and HuggingFace models for embedding generation.

## Requirements

The app requires the following Python packages, which can be installed using the provided `requirements.txt` file.

```plaintext
langchain
PyPDF2
python-dotenv
streamlit
openai
faiss-cpu
altair
tiktoken
# uncomment to use huggingface llms
huggingface-hub

# uncomment to use instructor embeddings
InstructorEmbedding
sentence-transformers
langchain-community
