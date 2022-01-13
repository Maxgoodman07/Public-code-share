import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    audio_data = r.record(source, duration = 5)
    
    print("")
    print("Recognizing...")

    try:
        text = r.recognize_google(audio_data)
    
    except Exception:
        print("")
        print("Could not understand you, please try again!")

    print(text)