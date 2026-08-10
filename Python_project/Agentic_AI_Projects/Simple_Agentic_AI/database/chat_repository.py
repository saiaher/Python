from database.connection import get_connection


# CREATE
# Save a new message
def save_message(session_id, role, content):

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO messages (session_id, role, content)
            VALUES (?, ?, ?)
        """, (session_id, role, content))

        conn.commit()

    except Exception as e:
        print(f"Database error while saving message: {e}")

    finally:
        if conn:
            conn.close()


# READ
# Get all messages from a session
def get_messages(session_id):

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT role, content
            FROM messages
            WHERE session_id = ?
            ORDER BY id ASC
        """, (session_id,))

        messages = cursor.fetchall()

        return messages

    except Exception as e:
        print(f"Database error while retrieving messages: {e}")
        return []

    finally:
        if conn:
            conn.close()


# UPDATE
# Update an existing message
def update_message(message_id, new_content):

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE messages
            SET content = ?
            WHERE id = ?
        """, (new_content, message_id))

        conn.commit()

    except Exception as e:
        print(f"Database error while updating message: {e}")

    finally:
        if conn:
            conn.close()


# DELETE
# Delete an existing message
def delete_message(message_id):

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM messages
            WHERE id = ?
        """, (message_id,))

        conn.commit()

    except Exception as e:
        print(f"Database error while deleting message: {e}")

    finally:
        if conn:
            conn.close()