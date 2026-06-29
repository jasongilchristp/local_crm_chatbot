import json
from collections.abc import Generator

import requests

from config.constants import OLLAMA_BASE_URL, OLLAMA_CHAT_URL


def is_ollama_running() -> bool:
    try:
        response = requests.get(OLLAMA_BASE_URL, timeout=3)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def build_payload(
    model: str,
    system_prompt: str,
    temperature: float,
    messages: list[dict],
) -> dict:
    return {
        "model": model,
        "messages": [{"role": "system", "content": system_prompt}, *messages],
        "stream": True,
        "options": {
            "temperature": temperature,
        },
    }


def stream_chat(payload: dict) -> Generator[str, None, None]:
    with requests.post(OLLAMA_CHAT_URL, json=payload, stream=True, timeout=120) as response:
        response.raise_for_status()

        for line in response.iter_lines():
            if not line:
                continue

            chunk = json.loads(line.decode("utf-8"))
            content = chunk.get("message", {}).get("content", "")

            if content:
                yield content

            if chunk.get("done", False):
                break
