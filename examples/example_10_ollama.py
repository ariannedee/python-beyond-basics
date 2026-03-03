"""
Documentation: https://github.com/ollama/ollama-python
"""
import ollama

prompt = "Hello"

response: ollama.ChatResponse = ollama.chat(
    model="llama3", messages=[{"role": "user", "content": prompt}]
)

print(response["message"]["content"])  # Access via keys
print(response.message.content)        # Access via attributes
