import random

import Keywords


def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit": # lower is used to convert the input to lowercase
            print("Chatbot: Goodbye!")
            break
        response = chatbot(user_input)
        print("Chatbot:", response)


def chatbot(user_input):
    for category, data in Keywords.keywords_responses.items():
        for keyword in data["keywords"]:
            if keyword in user_input.lower():
                return random.choice(data["responses"])
    return "I'm not sure how to respond to that."


if __name__ == "__main__":
    main()


