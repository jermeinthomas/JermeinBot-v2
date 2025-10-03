# =====================================================
# JermeinBot v2 - Junior Developer + Tier 1 IT Support
# Author: Jermein Thomas
# Description:
#   Chatbot that answers questions about programming (Dev)
#   and Tier 1 IT support (TI).
# =====================================================

def ask(question, answer):
    print(f"Q: {question}")
    print(f"A: {answer}\n")

# Dictionary of responses
responses = {
    # --- Dev / Programming ---
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

    # --- TI / Tier 1 Support ---
    "ti": "IT is an area where you can solve many problems and help users.",
    "internet": (
        "Stay calm first, I'm going to assist you with the issue. "
        "Please disconnect the laptop from electricity if it's charging. "
        "Provide your real password and network name so we can reset it. "
        "Then give me the new password you want to use, and try again."
    ),
    "tier 1": (
        "Tier 1 is the first line of defense in an IT company. "
        "They answer phones, chats, or meet users first. "
        "If the issue is difficult, they pass it to Tier 2 or Tier 3. "
        "Basically, Tier 1 is the friendly IT person who fixes easy stuff and "
        "knows when to escalate tricky problems."
    ),

    # --- General responses ---
    "thanks": "It was a pleasure helping you!",
    "bye": "Thanks so much! See you later!"
}

def start_bot():
    print("JermeinBot ready! (type 'exit' to quit)\n")

    while True:
        question = input("You: ").strip().lower()
        
        if question == "exit":
            print("Thanks so much! Case finished.")
            break
        
        found = False
        for key in responses:
            if key in question:  # search for keyword in input
                ask(question, responses[key])
                found = True
                break
        
        if not found:
            ask(question, "Hmm, I'm still learning. Could you repeat that please?")

# Run the bot
start_bot()
# Ask questions
# Asnwer questions
