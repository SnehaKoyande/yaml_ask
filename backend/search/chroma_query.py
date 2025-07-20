from search.chroma_indexer import collection

def search_config(query: str, top_k: int = 5):
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
    return results["documents"][0]
