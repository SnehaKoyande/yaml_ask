from chromadb.utils import embedding_functions
import chromadb
import uuid

client = chromadb.Client()
embedder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection = client.get_or_create_collection(name="configs", embedding_function=embedder)

def build_index(flat_config: dict, filename: str):
    documents = [f"{k} = {v}" for k, v in flat_config.items()]
    ids = [str(uuid.uuid4()) for _ in documents]
    metadatas = [{"filename": filename} for _ in documents]

    collection.add(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )

    return {"status": f"Indexed {len(documents)} entries from {filename}"}
