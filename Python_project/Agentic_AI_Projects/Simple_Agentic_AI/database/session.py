import uuid


SESSION_FILE = "current_session.txt"


def create_session():
    session_id = str(uuid.uuid4())

    with open(SESSION_FILE, "w") as file:
        file.write(session_id)

    return session_id


def get_session():
    try:
        with open(SESSION_FILE, "r") as file:
            session_id = file.read().strip()

            if session_id:
                return session_id

    except FileNotFoundError:
        pass

    return create_session()