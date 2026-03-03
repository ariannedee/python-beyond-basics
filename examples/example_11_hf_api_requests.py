"""
Hugging Face provides open-source AI models, with limited free usage (requires an account and API key).

https://huggingface.co/docs/inference-providers/guides/first-api-call
"""
import requests

with open("secrets/hf.txt") as file:
    api_key = file.read().strip()


def query_huggingface_ai(message, model="meta-llama/Llama-3.2-3B-Instruct"):
    api_url = "https://router.huggingface.co/v1/chat/completions"

    headers = {"Authorization": f"Bearer {api_key}"}

    payload = {
        "messages": [
            {
                "role": "user",
                "content": message,
            }
        ],
        "model": model,
    }
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]


if __name__ == "__main__":
    prompt = "Hello, world!"
    print(query_huggingface_ai(prompt))
