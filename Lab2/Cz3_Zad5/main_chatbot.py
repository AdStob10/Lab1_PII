from simple_chatbot import SimpleChatbot

if __name__ == "__main__":
    bot = SimpleChatbot(["Jak się nazywasz?", "Jaki jest twój ulubiony kolor?"])
    for question in bot:
        print(question)
        input()