import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
#import datetime
#import wikipedia #pip install wikipedia
#import webbrowser
#import os
#import smtplib

engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
volume = engine.getProperty('volume') 

engine.setProperty('rate',120) #120 words per minute




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    #It takes microphone input from the user and returns string output

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