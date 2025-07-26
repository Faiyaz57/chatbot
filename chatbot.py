print(" Chatbot: Hi! I am your simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()   

    if user_input in ["hi", "hello", "hey"]:
        print(" Chatbot: Hello! How can I help you today?")
    
    elif user_input in ["how are you", "how are you?"]:
        print(" Chatbot: I'm just a bot, but I'm doing great! Thanks for asking.")
    
    elif user_input in ["what is your name", "your name"]:
        print(" Chatbot: I'm a simple chatbot created with Python!")
    
    elif user_input in ["bye", "exit", "quit"]:
        print(" Chatbot: Goodbye! Have a nice day.")
        break
    
    else:
        print(" Chatbot: Sorry, I didn’t understand that.")
