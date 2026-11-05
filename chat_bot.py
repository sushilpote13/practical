import re

def chatbot(user_input):

    user_input = user_input.lower()

    if re.search("hello|hi|hey", user_input):
        return "Hello! How can I help you?"

    elif re.search("your name", user_input):
        return "I am a simple Python chatbot."

    elif re.search("how are you", user_input):
        return "I am fine. Thank you!"

    elif re.search("bye|exit", user_input):
        return "Goodbye!"

    elif re.search("thank", user_input):
        return "You are welcome!"

    else:
        return "Sorry, I don't understand."


print("Chatbot Started!")
print("Type 'bye' to exit.")

while True:

    user = input("You: ")
    response = chatbot(user)

    print("Bot:", response)

    if re.search("bye|exit", user.lower()):
        break