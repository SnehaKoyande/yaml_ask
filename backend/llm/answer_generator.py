import requests
from llm.memory import get_memory_text, add_to_memory
from typing import Union
import json

def generate_agent_answer(context: str, question: str, mode: str = "chat") -> Union[dict, str]:
    conversation = get_memory_text()
    if mode == "structured":
        prompt = f"""
You are a config assistant for DevOps engineers.

Using the context below, answer the user's question with structured output in JSON format.

Previous conversation:
{conversation}

Context:
{context}

User:
{question}

Respond in this format:
{{
  "summary": "...",
  "risk": "...",
  "fix": "...",
  "references": "..."  // optional
}}
"""

    else:
        prompt = f"""
You are a helpful DevOps AI assistant. Use the provided config context to answer the user's question.
Be concise, specific, and helpful.

Previous conversation:
{conversation}

Config context:
{context}

User: {question}
AI:"""

    print('**** generate_agent_answer ****')
    print(f'{prompt=}')
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        raise Exception(f"Ollama error: {response.text}")

    answer = response.json()["response"].strip()
    add_to_memory("user", question)
    add_to_memory("assistant", answer)

    if mode == "structured":
        try:
            return json.loads(answer)
        except Exception:
            return {
                "summary": "Could not parse structured response.",
                "raw": answer
            }

    return answer
