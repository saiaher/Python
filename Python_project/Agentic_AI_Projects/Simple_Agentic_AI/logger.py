from datetime import datetime

LOG_FILE = "chat_logs.txt"


def save_log(question, answer):

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:

            file.write("=" * 60 + "\n")
            file.write(f"Time: {datetime.now()}\n")
            file.write("Activity: AI conversation\n")
            file.write(f"User: {question}\n")
            file.write(f"AI: {answer}\n")
            file.write("=" * 60 + "\n\n")

    except Exception as e:
        print(f"Logging error: {e}")