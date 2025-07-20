from pydantic import BaseModel

class IndexRequest(BaseModel):
    config: dict
    filename: str

class QueryRequest(BaseModel):
    question: str

class AnalyzeRequest(BaseModel):
    config: dict
    filename: str
