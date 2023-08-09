import speech_recognition as sr
import pyautogui

def scroll_down():
    pyautogui.scroll(-1)  

def scroll_up():
    pyautogui.scroll(1)  

recognizer = sr.Recognizer()
microphone = sr.Microphone()

while True:
    with microphone as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        if "scroll down" in command:
            scroll_down()
        elif "scroll up" in command:
            scroll_up()

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Could not request results")
