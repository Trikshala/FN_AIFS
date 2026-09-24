from ollama import chat

response = chat(
    model= "llama3.2",
    messages=[
        {
            "role" : "user",
            "content" : "Write me a whatsapp message to my friend geetha asking her to meet me at the bus stop. Keep the answer under 2 lines."
        }
    ]
)

print(response.message.content)