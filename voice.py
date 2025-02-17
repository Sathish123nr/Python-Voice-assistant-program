import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Start Speaking!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)

    except:
       pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%m:%p')
        talk('the current time is' + time)
    elif 'who is ' in command:
        name = command.replace('who is','')
        info = wikipedia.summary(name,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_jokes())
    elif 'stop' in command:
            sys.exit()
    else:
        talk('please say the command again')

while(10):
    run_alexa()
