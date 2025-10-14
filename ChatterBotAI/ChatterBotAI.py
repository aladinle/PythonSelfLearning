import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Create OpenAI client using the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_ai():
    print("Chat with the AI (type 'quit' to exit)")
    conversation_history = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        # Append user's message
        conversation_history.append({"role": "user", "content": user_input})

        try:
            # Make API request with conversation history
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation_history
            )

            # Get assistant's reply
            ai_response = response.choices[0].message.content.strip()
            print(f"AI: {ai_response}")

            # Append assistant's reply
            conversation_history.append({"role": "assistant", "content": ai_response})

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_ai()