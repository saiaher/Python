import os
from dotenv import load_dotenv
from groq import Groq

from database.chat_repository import save_message, get_messages
from database.session import get_session
from prompts import SYSTEM_PROMPT

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# One session for the current running conversation
SESSION_ID = get_session()


def ask_llm(question):

    try:
        # ---------------------------------
        # 1. Get previous conversation
        # ---------------------------------
        history = get_messages(SESSION_ID)

        # ---------------------------------
        # 2. Build conversation for LLM
        # ---------------------------------
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        # Add previous messages
        for role, content in history:
            messages.append({
                "role": role,
                "content": content
            })

        # Add current user question
        messages.append({
            "role": "user",
            "content": question
        })

        # ---------------------------------
        # 3. Send conversation to Groq
        # ---------------------------------
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7
        )

        # ---------------------------------
        # 4. Get AI response
        # ---------------------------------
        answer = response.choices[0].message.content

        # ---------------------------------
        # 5. Save user message
        # ---------------------------------
        save_message(
            SESSION_ID,
            "user",
            question
        )

        # ---------------------------------
        # 6. Save AI response
        # ---------------------------------
        save_message(
            SESSION_ID,
            "assistant",
            answer
        )

        return answer

    except Exception as e:
        return f"Error: {e}"