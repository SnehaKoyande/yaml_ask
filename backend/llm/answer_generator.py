import requests
from llm.memory import get_memory_text, add_to_memory

def generate_agent_answer(context: str, question: str) -> str:
    conversation = get_memory_text()

    prompt = f"""
You are a helpful DevOps AI assistant. Use the provided config context to answer the user's question.
Be concise, specific, and helpful.

Previous conversation:
{conversation}

Config context:
{context}

User: {question}
AI:"""
    
    print(f'Prompt for LLM: {prompt}')

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

    return answer
