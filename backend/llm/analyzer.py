import requests

def analyze_config(filename: str, config: dict) -> dict:
    flat = flatten_config_for_prompt(config)
    prompt = f"""
You are a DevOps assistant that audits infrastructure as code.

The following configuration is from file `{filename}`.
Please do the following:
1. Summarize what the config is doing
2. Identify any misconfigurations or bad practices
3. Suggest improvements or best practices
4. Propose a corrected version (if applicable)

Config content:
{flat}
"""

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

    return {
        "analysis": response.json()["response"].strip()
    }

def flatten_config_for_prompt(config: dict, prefix="") -> str:
    """Flattens nested dict to string for prompting"""
    lines = []
    for k, v in config.items():
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            lines.append(flatten_config_for_prompt(v, path))
        else:
            lines.append(f"{path} = {v}")
    return "\n".join(lines)
