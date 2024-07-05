from sentence_transformers import SentenceTransformer
from langchain_community.embeddings.huggingface import HuggingFaceInstructEmbeddings

# Minimal example
def test_embeddings():
    try:
        embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
        print("Initialization successful")
    except TypeError as e:
        print(f"TypeError: {e}")

test_embeddings()