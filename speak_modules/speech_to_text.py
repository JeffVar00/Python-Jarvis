import speech_recognition as sr
import pyttsx3

# jarvis library for speech recognition, needed for the speech recognition personalization, fakeU library
# speech to text functionality from https://www.youtube.com/watch?v=LEDpgye3bf4&t=0s&ab_channel=CSCoach

class SpeechToText():

    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

    def record_audio(self):
        # loop through the audio input until the user stops talking
        while(1):
            try:
                with self.m as source:
                    self.r.adjust_for_ambient_noise(source)
                    print("Say something!")
                    audio = self.r.listen(source)
                return self.r.recognize_google(audio)
            except sr.RequestError as e:
                print("API was unreachable or unresponsive, {0}".format(e))
            except sr.UnknownValueError:
                print("Unknown error occurred")

    def Speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    