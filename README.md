# yaml_ask
A fullstack AI-powered app that lets users upload YAML/Terraform config files and ask questions or get debugging help using LLMs + vector search.

## Run command for frontend:
npm run dev

## Run command for backend:
(first adtivate the virtual environemt using the Activate script)
uvicorn main:app --reload --port 8000

## Sample curl req for backend
 curl.exe -X POST -F "file=@sample_yaml.yml" http://localhost:8000/parse/
