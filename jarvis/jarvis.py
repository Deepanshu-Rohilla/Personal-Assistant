import pyttsx3
import datetime
import os
import time
import playsound
from gtts import gTTS
import speech_recognition as sr
import pyaudio



#engine = pyttsx3.init('sapi5')
#voice = engine.getProperty('voices')
#print(voices)

def speak(text):
    tts = gTTS(text = text, lang = "en-in")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
def greetMe():

    # it will run in the starting
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good morning Deepanshu sir. How may I help you?")
    elif(hour>=12 and hour<18):
        speak("Good afternoon Deepanshu sir. How may I help you?")
    else:
        speak("Good evening Deepanshu sir. How may I help you?")
def takeCommand():
    #It takes microphone input from user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said: ", (query))
    except:
        print("Say that again please...")
        return "None"
    
    return query
if __name__ == "__main__":
    greetMe()
    takeCommand()
