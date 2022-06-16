import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wish():
    Hour=int(datetime.datetime.now().hour)
    Mint=(datetime.datetime.now().minute)
    if Hour>=0 and Hour<12:
        speak('good morning sir'),speak('the time is')
        speak(Hour),speak(Mint),speak('AM')
    elif Hour>=12 and Hour<18:
        speak('good afternoon sir')
        speak(Hour),speak(Mint),speak('PM')
    else:
        speak('good evening sir'),speak('the time is')
        speak(Hour),speak(Mint),speak('PM')
def command():
    s=sr.Recognizer()
    with sr.Microphone() as m:
        print('listening')
        s.adjust_for_ambient_noise(m, duration=5)
        s.dynamic_energy_threshold = True
        audio=s.listen(m)
        try:
            print('recoginizing')
            query=s.recognize_google(audio,language='eng:in')
            print('you said',query)
        except Exception as e:
           print('Please say that again.')
           query=None
        return query
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('antshant12@gmail.com','syedasadullahali19@gmail.com')
    server.sendmail('antshant12@gmail.com',to,content)
    server.close()
speak('Hi I am Siri')
speak ('initializing system...')
wish()
query = command().lower()

while True:
    if 'wikipedia' in query:
     speak('searching wikipedia')
     query=query.replace("wikipedia","")
     results=wikipedia.summary(query,sentences=2)
     speak(results)
     print(results)
    elif 'open youtube' in query:
         webbrowser.open('youtube.com')
    elif 'open google' in query:
        webbrowser.open('google.com')
    elif 'play music' in query:
        music_dir='C:/Users/Syed Asadullah/Music'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'tell me time' in query:
        strtime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,the time is {strtime}")
    elif 'open Python' in query:
        python='C:/Users/Syed Asadullah/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.9/IDLE (Python 3.9 64-bit).lnk'
        os.startfile(python)
    elif 'send email' in query:
        try:
            speak('what should I say')
            content= command()
            to='syedasadullahali19@gmail.com'
            sendemail(to,content)
            speak('email has been sent')
        except Exception as e:
            print(e)
            speak('email has not sent')
        
        
   




    
