# Simple in-memory storage for now
memory = []

def add_to_memory(role: str, content: str):
    memory.append({"role": role, "content": content})

def get_memory_text():
    chat = ""
    for turn in memory:
        chat += f"{turn['role'].capitalize()}: {turn['content']}\n"
    return chat

def clear_memory():
    memory.clear()
