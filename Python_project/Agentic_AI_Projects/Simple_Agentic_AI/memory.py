conversation_history = []

def add_message(role, message):
    conversation_history.append({
        "role": role,
        "content": message
    })

def get_history():
    return conversation_history