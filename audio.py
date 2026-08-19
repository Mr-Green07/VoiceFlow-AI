import nltk
import pyttsx3
import ollama

# Create a speaker
# speaker = pyttsx3.init()

# Set the speaker's voice
# speaker.setProperty('voice', 'english')

# Say something
# for i in range(5):

#     speaker.say("Hello, world!", i)
#     print(i, "say() finished")

# Wait for the speaker to finish
# speaker.runAndWait()
print("runAndWait() finished")
# Install ollama
# (Download from https://ollama.com/download)

# Then in your Python code:
# import ollama

# Pull the model - this only needs to be done once
# In terminal: ollama pull llama3:8b

# Use the model
def get_response(prompt):
    response = ollama.generate(model='llama3.2:11b', prompt=prompt)
    return response['response']

# Example
print(get_response("Hello, how are you?"))

