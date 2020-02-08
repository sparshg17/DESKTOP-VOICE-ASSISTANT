import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os

import webbrowser
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour <18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir!")
    speak("Please tell me how may I help you")

def takeCommand():            #for taking microphone input from user and it will return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=3, phrase_time_limit=3)

    try:
        print("Recognizing...")
        Query = r.recognize_google(audio,language="en-in")
        print("User Said:",Query)

    except Exception as e:
      #  print(e)
        print ("Say that again Please...")
        return "None"
    return Query

if __name__ == "__main__":
    wishme()
    takeCommand()
    while True:
        Query = takeCommand().lower() #logic for executing tasks based on query

        if "wikipedia" in Query:
            speak("Searching Wikipedia...")
            Query = Query.replace("Wikipedia","")
            results = wikipedia.summary(Query,sentences=2) #returns 2 sentences from wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in Query:
            webbrowser.open("youtube.com")
        
        elif "open google" in Query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in Query:
            webbrowser.open("stackoverflow.com")
        elif "the time" in Query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir! The time is {strtime}")
        elif "open gmail" in Query:
           webbrowser.open("gmail.com")




