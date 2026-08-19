import os
from typing import List, Dict

try:
    import ollama
except ImportError as e:
    raise SystemExit("Missing dependency: install the 'ollama' Python package and the Ollama app. See https://ollama.com.")

# Optional TTS if available
try:
    import pyttsx3  # type: ignore
    _tts_engine = pyttsx3.init()
except Exception:
    _tts_engine = None

MODEL = os.getenv("LLAMA_MODEL", "gemma3:4b")

SYSTEM_PROMPT = (
    "You are an expert AI Trainer and coach. You teach step-by-step, adapt to the learner's level, "
    "and check understanding with short quizzes. Keep answers concise and concrete."
)

Message = Dict[str, str]


def speak(text: str) -> None:
    if _tts_engine is None:
        return
    try:
        _tts_engine.say(text)
        _tts_engine.runAndWait()
    except Exception:
        pass


def chat(messages: List[Message]) -> str:
    """Single chat turn using Ollama with conversation history."""
    try:
        res = ollama.chat(model=MODEL, messages=messages)
        return res["message"]["content"]
    except Exception as e:
        raise RuntimeError(f"Chat failed: {e}")


def ensure_model(model: str) -> None:
    """Ensure the model exists locally; try to pull if missing, and check daemon availability."""
    try:
        # Fast path: check if model exists in local list
        models = ollama.list().get("models", [])
        if not any(m.get("model") == model for m in models):
            print(f"Model '{model}' not found locally. Attempting to pull (this may take a while)...")
            ollama.pull(model=model)
    except Exception as e:
        # Common cases: daemon not running / connection refused
        raise SystemExit(
            "Unable to connect to Ollama. Ensure the Ollama app/daemon is running.\n"
            "On Windows, start the Ollama app or run: 'ollama serve' in a terminal.\n"
            f"Details: {e}"
        )


def plan_curriculum(topic: str, level: str) -> str:
    messages: List[Message] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                f"Create a short learning plan for '{topic}' at {level} level. "
                "Include: goals, 4-6 step outline, and 3 practical exercises."
            ),
        },
    ]
    return chat(messages)


def quiz_question(topic: str) -> str:
    messages: List[Message] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                f"Ask one focused question to test understanding of: {topic}. "
                "Prefer real-world, concrete examples."
            ),
        },
    ]
    return chat(messages)


def evaluate_answer(question: str, answer: str) -> str:
    rubric = (
        "Evaluate the learner's answer on correctness, clarity, and depth. "
        "Return: Score (0-10) and 1-2 specific suggestions to improve."
    )
    messages: List[Message] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Question: {question}"},
        {"role": "user", "content": f"Learner answer: {answer}"},
        {"role": "user", "content": rubric},
    ]
    return chat(messages)


def interactive_session() -> None:
    print(f"Local Llama AI Trainer (Ollama) using model: {MODEL}\nType 'exit' to quit. Type 'quiz' to start a quick quiz.")
    # Verify daemon + model
    ensure_model(MODEL)
    topic = input("Topic you want to learn/train on: ").strip()
    if topic.lower() == "exit":
        return
    level = input("Your level (beginner/intermediate/advanced): ").strip() or "beginner"

    plan = plan_curriculum(topic, level)
    print("\nLearning plan:\n", plan, "\n")
    speak("Here is your learning plan.")

    # Chat mode with memory
    history: List[Message] = [
        {"role": "system", "content": SYSTEM_PROMPT + f" Topic: {topic}. Level: {level}."}
    ]

    while True:
        user_in = input("You: ").strip()
        if user_in.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if user_in.lower() == "quiz":
            q = quiz_question(topic)
            print("Trainer:", q)
            speak(q)
            ans = input("Your answer: ")
            fb = evaluate_answer(q, ans)
            print("Trainer:", fb)
            speak("Here is feedback on your answer.")
            continue

        history.append({"role": "user", "content": user_in})
        try:
            reply = chat(history)
        except RuntimeError as e:
            print(str(e))
            print("Tip: Verify the Ollama daemon is running and the model tag is correct.")
            continue
        print("Trainer:", reply)
        speak(reply)
        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    # Ensure the Ollama daemon is running and the model is available:
    #   ollama pull llama3.2:3b
    #   ollama run llama3.2:3b
    interactive_session()
