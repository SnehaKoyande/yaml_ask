import re
from typing import Optional
from .chroma_indexer import collection

def extract_filename(question: str) -> Optional[str]:
    match = re.search(r'([^\s]+\.(tf|yaml|json))', question, re.IGNORECASE)
    if match:
        print(f'{match.group(1)=}')
    return match.group(1) if match else None

def search_config(question: str, top_k: int = 5):
    filename = extract_filename(question)

    filter_query = {"filename": filename} if filename else None

    results = collection.query(
        query_texts=[question],
        n_results=top_k,
        where=filter_query
    )

    return results["documents"][0]
