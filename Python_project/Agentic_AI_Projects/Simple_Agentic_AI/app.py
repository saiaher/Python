from planner import create_plan
from llm import ask_llm
from logger import save_log
from tools import read_file
from memory import add_message

print("===================================")
print("      Simple AI Research Agent")
print("===================================")

while True:

    # User Input
    question = input("\nEnter your question (type 'exit' to quit): ").strip()

    # Exit
    if question.lower() == "exit":
        print("\nThank you for using Simple AI Research Agent!")
        break

    # Empty Input
    if question == "":
        print("Please enter a valid question.")
        continue

    print("\nYou asked:")
    print(question)

    # Create Plan
    plan = create_plan(question)

    print("\nPlan:")
    for step in plan:
        print("-", step)

    # ---------------- TOOL INTEGRATION ----------------
    if question.lower().startswith("read "):

        filename = question[5:].strip()

        file_content = read_file(filename)

        # If file not found
        if file_content.startswith("Error"):
            answer = file_content

        else:
            # Store file content in memory
            add_message(
                "system",
                f"""
The user has uploaded/read a file named '{filename}'.

Remember the following information and use it to answer future questions.

File Content:
{file_content}
"""
            )

            answer = f"✅ File '{filename}' loaded successfully.\nI will remember its contents for future questions."

    # ---------------- LLM ----------------
    else:
        answer = ask_llm(question)

    # Show Answer
    print("\nAnswer:")
    print(answer)

    # Save Logs
    save_log(question, answer)