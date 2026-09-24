from ollama import chat

system_msg = "You are a friendly tutor. Answer in warm tones. Answer in one sentence."
history = [{"role" : "system","content" : system_msg}]
question_counter = 0

while True:
    question = input("You:")
    if question == "":
        print("Anushka 🤖: Please type something.")
        continue

    if question.lower().strip() == "/history":
        print("----- Your Conversation so far ------")
        if len(history) < 2:
            print("Nothing here so far!")
        for msg in history[1:]:
            if msg["role"] == "user":
                speaker = "You"
            else:
                speaker = "Anushka 🤖"
            print(f"{speaker}: {msg['content']}")
        print("-----------------------------------")
        print()
        continue

    if question.lower().strip() == "/clear":
        history = [{"role" : "system","content" : system_msg}]
        print("Your history is cleared. Start a fresh conversation.")
        print()
        continue

    if question.lower().strip() == "/help":
        print("----- Available commands -----")
        print("/history - displays conversation history")
        print("/clear - clears chat history")
        print("/help - displays this list")
        print("exit - quits the chatbot")
        print("------------------------------")
        print()
        continue

    if question.lower().strip() == "exit":
        print("Anushka 🤖: Goodbye user. Please come back soon! 🤧🤧")
        print(f"You asked {question_counter} questions today. Good job!")
        break

    history.append({"role" : "user", "content": question})
    question_counter += 1
    try:
        response = chat(
                model="llama3.2",
                messages = history 
            )
        reply = response.message.content
        history.append({"role" : "assistant", "content" : reply})
        print(f"Anushka 🤖: {reply}")
        print()
    except Exception as e:
        print("Unknown issue. Is Ollama running?")




# /personality
# you type the personality
# reset the system msg, print confirmation
# and continue the loop


# print()

# history[0]["content"] = new_personality