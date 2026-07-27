import os
from dotenv import load_dotenv
from groq import Groq

from memory import add_message, get_history
from prompts import SYSTEM_PROMPT

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(question):
    try:
        # Save user question in memory
        add_message("user", question)

        # Create messages list
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        # Add conversation history
        messages.extend(get_history())

        # Send request to Groq
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7
        )

        # Get AI answer
        answer = response.choices[0].message.content

        # Save AI answer in memory
        add_message("assistant", answer)

        return answer

    except Exception as e:
        return f"Error: {e}"