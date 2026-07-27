from datetime import datetime

LOG_FILE = "chat_logs.txt"

def save_log(question, answer):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write("=" * 50 + "\n")
        file.write(f"Time: {datetime.now()}\n")
        file.write(f"User: {question}\n")
        file.write(f"AI: {answer}\n\n")