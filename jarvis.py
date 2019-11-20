import pyttsx3 #module for setup the engine
import datetime # for date and time
import speech_recognition as sr #for speech recognition
import wikipedia #to get wikipedia  information
import webbrowser # to access webbrowser
import os
import random # to get genrate random number
import smtplib # to send email

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[2].id)
engine.setProperty('voices', voices[2].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning')
    elif hour>12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak('hello, i am jarvis , how may i help you')

def takeCommand():
    ''' to take microsoft input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-ind')
        print('user said : ', query)
    except Exception as e:
        print(e)
        speak("say that again please.....")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP(" smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('girijeshwar15795@gmail.com', 'password')
    server.sendmail('girijeshwar15795@gmail.com', to , content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
        query= takeCommand().lower()
        # logic for executing takes based on query
        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'open internshala' in query:
            webbrowser.open('internshala.com')

        elif 'open ytsMovies' in query:
            webbrowser.open('ytsMovies.com')

        elif 'linkdln youtube' in query:
            webbrowser.open('linkdln.com')
        
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        
        elif 'open github' in query:
            webbrowser.open('github.com')

        elif 'play music' in query:
            music_dir = 'D:\\New folder'
            songs = os.listdir(music_dir)
            i = random.randint(0,25)
            print(i)
            os.startfile(os.path.join(music_dir, songs[i]))
        
        elif 'what is the time ' in query:
            time= datetime.datetime.now(). strftime("%H:%M")
            speak("the Time is ", str(time))
        
        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\girij\\AppData\\Local\Programs\\Microsoft VS Code"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak('what should i write?')
                content = takeCommand()
                to = "girijeshwar15795@gmail.com"
                sendEmail(to, content)
                speak('email has been sent!')
            except Exception as e:
                print(e)
                speak(' sorry bro i am not able to send email')
        elif 'stop' in query:
            engine.runAndWait()

        elif 'introduce yourself' in query:
            speak(" hello, i am desktop assistant made by girijeshwar singh. my name is jarvis, i am a python program, i come into the existance on 20th november 2019, thats all aboutme, my now tell me what i can do for you sir")

        else:
            if 'okay bye' in query:
                speak('bye sir, see you again soon')
                print('see you next time')
                break
