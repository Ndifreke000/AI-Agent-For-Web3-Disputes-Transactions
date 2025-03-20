from deeppavlov import build_model, configs

def chatbot():
    # Build and download the FAQ model using DeepPavlov's built-in configuration
    faq_model = build_model(configs.faq.fasttext_logreg, download=True)  # Updated to use the available configuration

    print("AI Dispute Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        # Get the model's response (model returns a list)
        response = faq_model([user_input])[0]
        
        # Fallback if no response is found
        if not response:
            response = "I'm not sure about that. Could you rephrase?"
        
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()
