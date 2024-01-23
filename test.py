from litellm import completion

response = completion(
    model="ollama/mistral", 
    messages=[{ "content": "respond in 20 words. who are you?","role": "user"}], 
    api_base="https://51af-34-148-67-249.ngrok-free.app"
)
print(response)
