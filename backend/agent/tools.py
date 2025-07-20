from search.chroma_query import search_config
from llm.analyzer import analyze_config
from validation.rules import run_validations

def tool_search(question: str):
    chunks = search_config(question)
    return "\n".join(chunks)

def tool_analyze(filename: str, config: dict):
    result = analyze_config(filename, config)
    return result["analysis"]

def tool_validate(config: dict):
    return run_validations(config)
