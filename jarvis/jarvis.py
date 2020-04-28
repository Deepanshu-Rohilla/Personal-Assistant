import pyttsx3
import datetime
import os
import time
import playsound
from gtts import gTTS


#engine = pyttsx3.init('sapi5')
#voice = engine.getProperty('voices')
#print(voices)

def speak(text):
    tts = gTTS(text = text, lang = "en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good morning Deepanshu sir. How may I help you?")
    elif(hour>=12 and hour<18):
        speak("Good afternoon Deepanshu sir. How may I help you?")
    else:
        speak("Good evening Deepanshu sir. How may I help you?")

if __name__ == "__main__":
    greetMe()