import openai


openai.api_key = "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"

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Chatbot: Hello! Ask me anything about finance. Type 'exit' to stop.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye! Have a great day! ")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
