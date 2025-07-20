from pydantic import BaseModel

class IndexRequest(BaseModel):
    config: dict
    filename: str

class QueryRequest(BaseModel):
    question: str

class AnalyzeRequest(BaseModel):
    config: dict
    filename: str

class ChatRequest(QueryRequest):
    mode: str = "chat" # Default mode is chat, can be set to "structured" for structured output