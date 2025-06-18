import requests
import json

# Function to call Ollama and stream the response
def ollama_chat(prompt, model="mistral"):
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={"model": model, "prompt": prompt},
        stream=True
    )
    reply = ""
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode('utf-8'))
            if "response" in data:
                reply += data["response"]
    return reply

# Feature Functions
def ask_question(question):
    return ollama_chat(f"Answer this academic question:\n\n{question}")

def paragraph_feedback(paragraph):
    prompt = f"Give constructive feedback for the following paragraph to help the student improve:\n\n{paragraph}"
    return ollama_chat(prompt)

def summarize_paragraph(paragraph):
    prompt = f"Summarize the following paragraph in simple terms:\n\n{paragraph}"
    return ollama_chat(prompt)

def explain_topic(topic):
    prompt = f"Explain the topic '{topic}' in a simple way for a student to understand."
    return ollama_chat(prompt)

def generate_quiz(content):
    prompt = f"Based on the following content, create 3 multiple-choice quiz questions with 4 options and mark the correct one:\n\n{content}"
    return ollama_chat(prompt)

# Main Chatbot Menu
def main():
    while True:
        print("\n🎓 Educational Chatbot (Powered by Ollama)")
        print("1. Ask a question")
        print("2. Submit a paragraph for feedback")
        print("3. Summarize a paragraph")
        print("4. Get a topic explained")
        print("5. Generate a quiz")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            q = input("Enter your question: ")
            print("\nAnswer:\n", ask_question(q))
        elif choice == "2":
            para = input("Paste your paragraph: ")
            print("\nFeedback:\n", paragraph_feedback(para))
        elif choice == "3":
            para = input("Paste your paragraph: ")
            print("\nSummary:\n", summarize_paragraph(para))
        elif choice == "4":
            topic = input("Enter a topic: ")
            print("\nExplanation:\n", explain_topic(topic))
        elif choice == "5":
            content = input("Enter topic/content: ")
            print("\nQuiz:\n", generate_quiz(content))
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
