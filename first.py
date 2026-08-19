import os

import google.generativeai as genai

# To install the library, run: pip install google-generativeai

try:
    # --- Configuration ---
    # Get your API key from Google AI Studio: https://aistudio.google.com/app/apikey
    # It's recommended to set it as an environment variable for security.
    # Example for Windows command prompt: set GOOGLE_API_KEY="YOUR_API_KEY"
    # Example for Linux/macOS terminal: export GOOGLE_API_KEY="YOUR_API_KEY"
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        # If the environment variable is not set, prompt the user.
        api_key = input("Please enter your Google API Key: ")
    
    genai.configure(api_key=api_key)

    # --- Model Initialization ---
    # Choose a model that supports chat, like 'gemini-pro'
    model = genai.GenerativeModel('gemini-pro')

    # --- Start Chat Session ---
    # The history allows the model to remember the conversation context.
    chat = model.start_chat(history=[])

    print("AI Chatbot is ready. Type 'exit' or 'quit' to end the session.")
    print("-" * 30)

    # --- Main Chat Loop ---
    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit']:
            print("AI: Goodbye!")
            break

        if not user_input.strip():
            print("AI: Please say something.")
            continue

        # Send the user's message to the model
        response = chat.send_message(user_input)

        # Print the model's response
        print(f"AI: {response.text}")

except ImportError:
    print("The 'google-generativeai' library is not installed.")
    print("Please install it by running: pip install google-generativeai")
except Exception as e:
    print(f"An error occurred: {e}")
    print("Please ensure your API key is correct and has the necessary permissions.")
