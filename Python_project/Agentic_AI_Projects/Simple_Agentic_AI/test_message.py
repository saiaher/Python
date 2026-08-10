from database.chat_repository import save_message, get_messages

session_id = "session_001"

# Save user message
save_message(
    session_id,
    "user",
    "What is Python?"
)

# Save AI response
save_message(
    session_id,
    "assistant",
    "Python is a programming language."
)

# Get conversation
messages = get_messages(session_id)

print("\nConversation History:")

for role, content in messages:
    print(role, ":", content)