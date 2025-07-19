from fastapi import FastAPI, UploadFile, File, HTTPException
import json
import hcl2
from io import StringIO
import os
import yaml

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
