from gtts import gTTS
from playsound import playsound as p
import os
import speech_recognition as sr

sound = {1 : "salam.mp3", 2 : "namasaya.mp3", 3: "error.mp3", 4: "unregister.mp3"}
path = "/home/rusdy/cpython/tts/"

def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("ready")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("you said "+ command + "\n")

    except sr.UnknownValueError:
        p(path+sound[3])
        command = myCommand()

    return command

def asisstant(command):
    if 'who your parents' in command:
        p(path+sound[1])
    elif 'what is your name'in command:
        p(path+sound[2])
    else:
        p(path+sound[4])

while True:
    asisstant(myCommand())
