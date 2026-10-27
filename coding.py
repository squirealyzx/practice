def get_answer(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"

    elif "python" in message:
        return "Python is a programming language."

    elif "hackathon" in message:
        return "A hackathon is a competition where teams build projects."

    else:
        return "I don't know the answer yet!"