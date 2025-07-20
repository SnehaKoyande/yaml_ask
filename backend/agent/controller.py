import requests
from agent.tools import tool_search, tool_analyze, tool_validate

TOOLS = {
    "search": tool_search,
    "analyze": tool_analyze,
    "validate": tool_validate
}

def decide_tools(question: str, context: str = "") -> list[str]:
    prompt = f"""
Given this user question:

"{question}"

Choose tools to answer it. Available tools:
- search
- analyze
- validate

Return a Python list of tool names like ["search", "analyze"].
Respond only with a valid list.
"""
    
    print('**** decide_tools ****')
    print(f'{prompt=}')

    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    })
    try:
        print('response from decide_tools:')
        print(f'{res.json()["response"]=}')
        return eval(res.json()["response"])
    except:
        return ["search"]

def agent_pipeline(question: str, filename: str, config: dict):
    tool_plan = decide_tools(question)
    memory = []

    for tool in tool_plan:
        if tool == "search":
            memory.append(tool_search(question))
        elif tool == "analyze":
            memory.append(tool_analyze(filename, config))
        elif tool == "validate":
            memory.append(tool_validate(config))

    final_prompt = f"""
You are a configuration assistant.

Question: {question}

Use this gathered context to answer:
{chr(10).join(memory)}

Return a structured response:
{{
  "summary": "...",
  "risk": "...",
  "fix": "...",
  "references": "..."
}}
"""
    print('**** generate_agent_answer ****')
    print(f'{final_prompt=}')

    final = requests.post("http://localhost:11434/api/generate", json={
        "model": "mistral",
        "prompt": final_prompt,
        "stream": False
    })

    return final.json()["response"]
