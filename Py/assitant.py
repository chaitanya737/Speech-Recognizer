from ast import expr_context, main
from datetime import datetime
from threading import main_thread
from tkinter.tix import MAIN
from unicodedata import name
import pyttsx3
import pyaudio
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')   #speach API
voices = engine.getProperty('voices');
engine.setProperty('voice' , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe() : 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18 : 
        speak("Good Afternoon")
    else:
        speak("Good Evening")        

    speak("I am Laura Sir. Please tell me how may i help you.")

def takeCommand():
    #Takes Input From user and Gives the String
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User Said {query}\n")    


    except Exception as e:
        print(e)
        print("Say that Again Please")
        return "None"
    return query    
if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open amazon' in query:
            webbrowser.open("www.amazon.com")        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open music' in query:
            webbrowser.open("music.amazon.in")

            