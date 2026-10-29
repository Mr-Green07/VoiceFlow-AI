import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import os
import subprocess
import os
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

print(f"There are {len(voices)} voices available.")

# Display details for each voice
for i, voice in enumerate(voices):
    print(f"Voice {i}:")
    print(f"  ID: {voice.id}")
    print(f"  Name: {voice.name}")
    print(f"  Languages: {voice.languages}")
    print(f"  Gender: {voice.gender}")
    print(f"  Age: {voice.age}")
    print("-" * 20)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
 
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...")   
        return "None" 
    return query

def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak(" please tell me how may is assist you")

def toggle_wifi(turn_on=True):
    """
    Toggle WiFi on or off using netsh command
    Args:
        turn_on (bool): True to turn on WiFi, False to turn off
    """
    interfaces_output = subprocess.check_output("netsh interface show interface", shell=True).decode('utf-8')
    
    # Look for wireless interfaces
    lines = interfaces_output.split('\n')
    for line in lines:
        if "Wireless" in line:
            # Extract interface name (usually "Wi-Fi" or "Wireless Network Connection")
            parts = line.split()
            if len(parts) >= 4:
                interface_name = ' '.join(parts[3:])
                
                if turn_on:
                    speak(f"Turning on {interface_name}")
                    os.system(f'netsh interface set interface "{interface_name}" enabled')
                    time.sleep(1)
                    speak("WiFi has been turned on.")
                else:
                    speak(f"Turning off {interface_name}")
                    os.system(f'netsh interface set interface "{interface_name}" disabled')
                    time.sleep(1)
                    speak("WiFi has been turned off.")
                return True
    
    speak("No wireless interface found")
    return False

def check_wifi_status():
    """Check if WiFi is enabled"""
    output = subprocess.check_output("netsh interface show interface", shell=True).decode('utf-8')
    lines = output.split('\n')
    for line in lines:
        if "Wireless" in line:
            if "Connected" in line or "Enabled" in line:
                return True
    return False
            
if __name__=="__main__":
    wishme()
    while True:
        query = takecommand().lower()
        
        if "wish me" in query:
            wishme()
            
        elif "turn on wifi" in query or "enable wifi" in query or "connect wifi" in query:
            toggle_wifi(turn_on=True)
            
        elif "turn off wifi" in query or "disable wifi" in query or "disconnect wifi" in query:
            toggle_wifi(turn_on=False)
            
        elif "check wifi" in query or "wifi status" in query:
            status = check_wifi_status()
            if status:
                speak("WiFi is currently enabled")
            else:
                speak("WiFi is currently disabled")
                
        elif "exit" in query or "quit" in query or "goodbye" in query:
            speak("Goodbye, sir")
            break


