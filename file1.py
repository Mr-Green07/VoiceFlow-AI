# palm api by google is discontinued so to use it you to use gemini api from vertex api



# import win32com.client
# import speech_recognition as sr
# import os
# import webbrowser
# # import openai
# import google.generativeai as palm

# # import subprocess, sys
# # import playsound
# import datetime
# from config import apikey
# palm.configure(api_key=apikey)
# import pprint
# for model in palm.list_models():
#     pprint.pprint(model) # 🦎🦦🦬🦄

# # chatStr = ""
# # def chat(query):
# #     global chatStr
# #     print(chatStr)
# #     openai.api_key = apikey
# #     chatStr += f"Yuvraj: {query}\n Jarvis: "
# #     response = openai.Completion.create(
# #         model="text-davinci-003",
# #         prompt= chatStr,
# #         temperature=0.7,
# #         max_tokens=256,
# #         top_p=1,
# #         frequency_penalty=0,
# #         presence_penalty=0
# #     )
# #     # todo: Wrap this inside of a  try catch block
# #     speaker.speak(response["choices"][0]["text"])
# #     chatStr += f"{response['choices'][0]['text']}\n"
# #     return response["choices"][0]["text"]

# # def ai(prompt):
# #     openai.api_key = apikey
# #     text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

# #     response = openai.Completion.create(
# #         model="text-davinci-003",
# #         prompt=prompt,
# #         temperature=0.7,
# #         max_tokens=256,
# #         top_p=1,
# #         frequency_penalty=0,
# #         presence_penalty=0
# #     )
    
# #     text += response["choices"][0]["text"]
# #     if not os.path.exists("Openai"):
# #         os.mkdir("Openai")

  
# #     with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
# #         f.write(text)


# def say(text):
#    os.system(f"say {text}")

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         speaker = win32com.client.Dispatch("SAPI.SpVoice") # create speaker object
#         r.pause_threshold =  1
#         audio = r.listen(source)

#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language="en-in")
#             print(f" User said: {query}")
#             return query
#         except Exception as e:
#             return "some error occured"

# speaker = win32com.client.Dispatch("SAPI.SpVoice")  # create speaker object
# # response = palm.generate_text(prompt="The opposite of hot is")
# # speaker.speak(response.result)
# # print(response.result) 
# response = palm.chat(messages=["Hello."])
# speaker.speak(response.last)
# print(response.last)
# response.reply("Can you tell me a joke?")

# if __name__ == '__main__':
#     print('hello')
#     speaker = win32com.client.Dispatch("SAPI.SpVoice") # create speaker object
#     speaker.speak("hello YUVRAJ , how are you ")
#     while True:
#         print("Listening....")
#         query = takecommand()
#         # sites = [ ["youtube", "https://www.youtube.com"], ["google", "https://www.google.com"], ["wikipedia", "www.wikipedia.com"]]
#         # for site in sites:
#         #     if f"Open {site[0]}".lower() in query.lower():
#         #         speaker.speak(f"opening {site[0]}")
#         #         webbrowser.open(site[1])
#         #     speaker.speak(query)
#         #     if "open google chrome".lower() in query.lower():
#         #         os.system(f"open C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
#         # if "play music" in query:
#         #      musicPath = "D:\GLOBAL\ audiorecognition\ audio1.mp3"
#         #      playsound.playsound(musicPath)
#         # todo: use try catch
#         # if "the time" in query:
#         #     time = datetime.datetime.now().strftime("%H:%M:%S")
#         #     speaker.speak(f"the time is {time}")   
#         #     hour = int(datetime.datetime.now().hour)
#         #     if hour>=0 and hour<12:
#         #         speaker.speak("good morning Sir")
#         #     elif hour>=12 and hour<18:
#         #         speaker.speak("good afternoon Sir")
#         #     else:
#         #         speaker.speak("good evening Sir")
#         # elif "Using artificial intelligence".lower() in query.lower():
            
#         #     response = palm.chat(messages=["Hello."])
#         #     print(response.last) #  'Hello! What can I help you with?'
#         #     response.reply("Can you tell me a joke?")


#         # if "Jarvis Quit".lower() in query.lower():
#         #     exit()

#         # elif "reset chat".lower() in query.lower():
#         #     chatStr = ""

#         # else:
#         #     print("Chatting...")
#         #     chat(query)
