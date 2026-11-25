print("PocketPal chatbot — type 'bye' to exit")

while True:
    message = input("You: ").strip().lower()

    if message in ("bye", "exit", "quit"):
        print("Bot: Goodbye!")
        break
    elif "hello" in message or "hi" in message:
        print("Bot: Hi! How can I help?")
    elif "how are you" in message:
        print("Bot: I'm doing fine, thanks!")
    elif "name" in message:
        print("Bot: I'm PocketPal.")
    else:
        print("Bot: I don't know that one yet. Try saying hello!")