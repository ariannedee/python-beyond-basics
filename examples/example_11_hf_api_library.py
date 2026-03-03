"""
Hugging Face provides open-source AI models, with limited free usage (requires an account and API key).

https://huggingface.co/docs/inference-providers/guides/first-api-call
"""
from huggingface_hub import InferenceClient

with open("secrets/hf.txt") as file:
    api_key = file.read().strip()


def query_huggingface_ai(prompt, model="meta-llama/Llama-3.2-3B-Instruct"):
    client = InferenceClient(
        api_key=api_key,
    )

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    prompt = "Hello, world!"
    print(query_huggingface_ai(prompt))
