from ollama import chat

bad = "Tell me about cats."
good = "List 3 cat breeds that are suitable for a penthouse. 2 lines about each."

responseB = chat(
    model= "llama3.2",
    messages=[
        {
            "role" : "user",
            "content" : bad
        }
    ]
)

responseG = chat(
    model= "llama3.2",
    messages=[
        {
            "role" : "user",
            "content" : good
        }
    ]
)

print(f"Bad Prompt Result: {responseB.message.content}")

print()

print(f"Good Prompt Result: {responseG.message.content}")