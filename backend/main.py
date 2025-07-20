from fastapi import FastAPI, UploadFile, File, HTTPException
import json
import hcl2
from io import StringIO
import os
import yaml
from utils.flatten import flatten_dict
from search.chroma_indexer import build_index
from search.chroma_query import search_config
from llm.answer_generator import generate_agent_answer
from llm.memory import clear_memory
from llm.analyzer import analyze_config
from models.request_models import AnalyzeRequest, IndexRequest, QueryRequest, ChatRequest
from agent.controller import agent_pipeline

def parse_json(content):
    return json.loads(content)

def parse_tf(content):
    return hcl2.load(StringIO(content.decode()))

def parse_yaml(content):
    return yaml.safe_load(content)

app = FastAPI()

@app.post("/parse/")
async def parse_file(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename)[1]

    content = await file.read()
    try:
        if ext in ['.yaml', '.yml']:
            result = parse_yaml(content)
        elif ext == '.tf':
            result = parse_tf(content)
        elif ext == '.json':
            result = parse_json(content)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"parsed": result}

@app.post("/index/")
async def index_config(payload: IndexRequest):
    try:
        flat = flatten_dict(payload.config)
        response = build_index(flat, payload.filename)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query/")
async def ask_question(payload: QueryRequest):
    try:
        results = search_config(payload.question)
        context = "\n".join(results)
        answer = generate_agent_answer(context, payload.question)
        return {"matches": results, "answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/chat/")
async def chat(payload: ChatRequest):
    try:
        context = "\n".join(search_config(payload.question))
        answer = generate_agent_answer(context, payload.question, mode=payload.mode)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/reset/")
async def reset():
    clear_memory()
    return {"message": "Memory cleared."}

@app.post("/analyze/")
async def analyze(payload: AnalyzeRequest):
    try:
        result = analyze_config(payload.filename, payload.config)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/agent/")
async def agent_copilot(req: AnalyzeRequest):
    try:
        response = agent_pipeline(
            question="What can be improved in this config?",
            filename=req.filename,
            config=req.config
        )
        return {"copilot": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

