import pyttsx3
import datetime
import os
import time
import playsound
from gtts import gTTS
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import sys
import subprocess
import smtplib
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
        print(query)
    except:
        print("Say that again please...")
        return "None"
    return query    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your-password")
    # youremail@gmail.com => plug in your emailid here
    #your-password => plug in your password here
    server.sendmail("youremail@gmail.com", to, content)
    server.close()



if __name__ == "__main__":
    greetMe()

    #logic here
    if(1):
        query = takeCommand().lower()
        if('wikipedia' in query):
            speak("Searching wikipedia...")
            query=query.replace("wikipedia", "")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif ("youtube" in query):
            print("here")
            webbrowser.open("http://www.youtube.com")
        elif ("open" in query and "google" in query):
            webbrowser.open("http://www.google.com")
        elif ("stackoverflow" in query):
            webbrowser.open("http://www.stackoverflow.com")
        elif("p***" in query): #if someone asks it to open porn ( speech recognition convets porn to p*** in string query)
            speak("abey saale tharki")
        elif (("time" in query) and ("what" in query)):
            t = datetime.datetime.now().strftime("%H:%M")
            speak("Sir, the time is " + t )
        elif("spotify" in query):
           # os.system(Applications/Spotify)
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "/Applications/Spotify" ])
        elif("email to deepanshu"):
            try:
                speak("What should I say")
                content = takeCommand()
                to = reciever@gmail.com 
                # replace reciever@gmail.com with the sender's email
                sendEmail(to, content)
                speak("Your email has been sent")
            except:
                speak("Sorry yaar. Nahi ho paaya. Pata nahi kya ho gaya")
    

            