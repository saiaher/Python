import os

def read_file(filename):
    try:
        if not os.path.exists(filename):
            return f"Error: '{filename}' not found."

        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        return content

    except Exception as e:
        return f"Error reading file: {e}"