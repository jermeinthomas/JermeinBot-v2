def ask(question, answer):
    print(f"Q: {question}")
    print(f"A: {answer}\n")


responses = {
    "python": "Python is a programming language that helps you build apps, websites, AI, etc.",
    "variable": "You can create a variable like this: my_variable = 5",
    "chatgpt": "ChatGPT is an AI that helps you with many things like creating images, solving tasks, and answering questions.",
    "javascript": "JavaScript is a programming language used to make websites, apps, and games interactive.",
    "if statement": "An if statement lets you make decisions in code. Example: if x > 5: do something.",
    "software architecture": (
        "It's the plan that connects everything in an app. "
        "Example: In a hotel chatbot: the bot chats, AI understands, "
        "and backend checks bookings - everything works together."
    ),

    "ti": "IT is an area where you can solve many problems and help users.",
    "internet": (
        "Stay calm first, I'm going to assist you with the issue. "
        "Please disconnect the laptop from electricity if it's charging. "
        "Please verify your network settings and restart the router if necessary. "
        "If the issue continues, contact your IT support team."
    ),
    "tier 1": (
        "Tier 1 is the first line of defense in an IT company. "
        "They answer phones, chats, or meet users first. "
        "If the issue is difficult, they pass it to Tier 2 or Tier 3. "
        "Basically, Tier 1 is the friendly IT person who fixes easy stuff and "
        "knows when to escalate tricky problems."
    ),

    "thanks": "It was a pleasure helping you!",
    "bye": "Thanks so much! See you later!"
}


def find_answer(question):
    for key in responses:
        if key in question:
            return responses[key]

    return None


def start_bot():
    print("JermeinBot ready! (type 'exit' to quit)\n")

    while True:
        question = input("You: ").strip().lower()

        if question == "exit":
            print("Thanks so much! Case finished.")
            break

        answer = find_answer(question)

        if answer:
            ask(question, answer)
        else:
            ask(question, "Hmm, I'm still learning. Could you repeat that please?")


start_bot()
