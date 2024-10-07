import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.chatgpt.com/")


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit =1)
                
            command = r.recognize_google(audio)
            if(command.lower() == "jarvis"):
                speak("Yes")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

            print(command)
        except Exception as e:
            print("Error: {0}".format(e))