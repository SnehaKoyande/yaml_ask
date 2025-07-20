import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

client = chromadb.Client()
embedder = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection = client.get_or_create_collection("configs", embedding_function=embedder)

def build_index(flat_config: dict):
    # Clear previous entries (optional)
    # collection.delete()

    texts = [f"{k} = {v}" for k, v in flat_config.items()]
    ids = [f"item-{i}" for i in range(len(texts))]

    collection.add(
        documents=texts,
        ids=ids,
        metadatas=[{"key": k} for k in flat_config.keys()]
    )

    return {"message": "Index built", "chunks_indexed": len(texts)}
