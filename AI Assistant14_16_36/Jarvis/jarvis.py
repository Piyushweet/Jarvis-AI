from math import perm
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pywhatkit
from plyer import notification
from bs4 import BeautifulSoup
import pyjokes
import pyautogui
import operator
import winshell
import feedparser
import smtplib
import ctypes
import shutil
from twilio.rest import Client
from clint.textui import progress
import win32com.client as wincl
from urllib.request import urlopen
import playsound
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui,QtCore
import geocoder
from speedtest import Speedtest
from PyQt5.QtGui import QMovie
import sys

from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr 
import os
import time
import webbrowser
from datetime import datetime
import pytz
import datetime
import speedtest
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    playsound.playsound("power up.mp3")
    import initi
    #playsound.playsound("Jarvis Start Up.wav")
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Sir")
    columns = shutil.get_terminal_size().columns

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            #speak("Pardon me, please say that again")
            return "None"
        return statement

wishMe()
'''
print("Initializing JARVIS")
speak("Initializing JARVIS")
print("Starting all system applications")
speak("Starting all system applications")
print("Installing and checking all drivers")
speak("Installing and checking all drivers")
print("Calibrating and examining all core processors")
speak("Calibrating and examining all core processors")
print("Checking the internet connection")
speak("Checking the internet connection")
usrname()
print("Wait a moment sir")
speak("Wait a moment sir")'''

#print("Loading your AI personal assistant JARVIS")
#speak("Loading your AI personal assistant JARVIS")

#wishMe()


def TaskExe():
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()


    
    FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

    class Main(QMainWindow,FROM_MAIN):
        def __init__(self,parent=None):
            super(Main,self).__init__(parent)
            self.setupUi(self)
            self.setFixedSize(1920,1080)
            self.label_7 = QLabel
            self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png)")
            self.exitB.clicked.connect(self.close)
            self.setWindowFlags(flags)
            self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
            self.label_7.setCacheMode(QMovie.CacheAll)
            self.label_4.setMovie(self.label_7)
            self.label_7.start()

        # total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
            #ram=round((used_memory/total_memory) * 100, 2)
            import psutil
            cpu_per = str(psutil.cpu_percent(4))
            memory = str(psutil.virtual_memory()[2])

            st=Speedtest()
            download=st.download()/(1024*1024)
            upload=st.upload()/(1024*1024)

            spd=("Do",round(download,2),"Up",round(upload,2))
            spd1=str(spd)
            g=geocoder.ip('me')
            locatiodn=g.latlng
            #print(locatiodn)
            
            ram= geocoder.google(locatiodn,method='reverse')
            city=g.state
            country=g.country
            #print(city,",",country)
            loc=str(locatiodn)
            loc1=str(city)
            loc2=str(country)
            UTC = pytz.utc
            IST = pytz.timezone('Asia/Kolkata')
            datetime_ist = datetime.datetime.now(IST)
            display=datetime_ist.strftime('%I:%M:%S %p %Z')

            

            self.ts = time.strftime("%A, %d %B")
            self.label.setPixmap(QPixmap("./lib/tuse.png"))
            self.label_2.setText("<font size=8 color='white'>"+self.ts+"</font>")
            self.label_2.setFont(QFont(QFont('Acens',8)))

            self.label_8.setText("<font size=8 color='white'>"+display+"</font>")
            self.label_8.setFont(QFont(QFont('Acens',8)))


            self.label_3.setText("<font size=8 color='white'>"+loc+","+loc1+","+loc2+"</font>")
            self.label_3.setFont(QFont(QFont('Acens',7)))

            self.label_5.setText("<font size=8 color='white'>"+spd1+"</font>")
            self.label_5.setFont(QFont(QFont('Acens',7)))

            self.label_6.setText("<font size=8 color='white'>"+"CPU: "+cpu_per+" RAM: "+memory+"</font>")
            self.label_6.setFont(QFont(QFont('Acens',8)))

    app = QtWidgets.QApplication(sys.argv)
    main_2 = Main()
    main_2.show()
    print("All drivers are up and running")
    speak("All drivers are up and running")
    print("All system has been activated")
    speak("All system has been activated")
    print("Now I am online")
    speak("Now I am online")
    
    

    while True:
        speak("Tell me how can I help you now?")
        
        statement = takeCommand().lower()
        if statement==0:
            continue
        
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
            
        elif 'play music' in statement or 'play song' in statement or 'play' in statement:
            statement = statement.replace("play", "")
            speak("Playing "+statement)
            pywhatkit.playonyt(statement)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        
        elif 'send a mail' in statement:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whom should i send")
                to = takeCommand()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")


        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                    str(current_temperature) + 
                    "\n pressure in pascal is " +
                    str(current_pressure) +
                    "\n humidity in percentage is " +
                    str(current_humidiy) +
                    "\n description  " +
                    str(weather_description))
                print(" Temperature in kelvin unit = " +
                    str(current_temperature) +
                    "\n humidity (in percentage) = " +
                    str(current_humidiy) +
                    "\n description = " +
                    str(weather_description))

            else:
                speak(" City Not Found ")

        
        elif 'date' in statement or 'dates' in statement:
            date = datetime.date.today()
            print(date)
            speak(date)
        
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            playsound.playsound("Jarvis.mp3")
            '''speak('I am JARVIS version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')'''


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Trio")
            print("I was built by Trio")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        
        elif 'news' in statement:
            
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                
                print(str(e))

                                
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement or 'open' in statement:
            new_url="https://www.google.com/search?q="
            statement = statement.replace("search","")
            webbrowser.open_new_tab(new_url+statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="KRTYYR-PRPXE4UV83"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        
    
            
        elif 'joke' in statement:
            random_joke = pyjokes.get_joke()
            print(random_joke)
            speak(random_joke)
        elif 'screenshot' in statement:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken.')
                                
        elif 'change background' in statement:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                    0,
                                                    "Location of wallpaper",
                                                    0)
            speak("Background changed successfully")
        elif 'lock window' in statement:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in statement:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
                
        elif 'empty recycle bin' in statement:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        
        elif "restart" in statement:
            subprocess.call(["shutdown", "/r"])
            
        elif "hibernate" in statement or "sleep" in statement:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "calculate" in statement:
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "write a note" in statement:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                e = datetime.datetime.now()
                strTime=e.strftime("%Y-%m-%d %H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        
        elif "show note" in statement:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            
            speak(print(file.read()))
        
        elif "who i am" in statement:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in statement:
            speak("Thanks to TRIO. Further It's a secret")
        
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
        elif "sleep" in statement or "sleep down" in statement or "sleepdown" in statement or "slip" in statement or "slip down" in statement or "slipdown" in statement:
            speak("Okay sir, I am going to sleep you can call me anytime")
            break
        elif "good bye" in statement or "ok bye" in statement or "stop" in statement or "goodbye" in statement or "shutdown yourself" in statement or "shut down yourself" in statement or "shutdown jarvis" in statement or "shut down jarvis" in statement:
                speak('your personal assistant JARVIS is shutting down,Good bye')
                playsound.playsound("power down.mp3")
                print('your personal assistant JARVIS is shutting down,Good bye')
                sys.exit()
        else:
            speak("Pardon me, please say that again")

if __name__=='__main__':
        clear = lambda: os.system('cls')
        clear()
        usrname()
        TaskExe()
        while True:
            permission = takeCommand()
            if 'wakeup' in permission or 'wake up' in permission:
                TaskExe()
            elif "good bye" in permission or "ok bye" in permission or "stop" in permission or "goodbye" in permission or "shutdown yourself" in permission or "shut down yourself" in permission or "shutdown jarvis" in permission or "shut down jarvis" in permission:
                speak('your personal assistant JARVIS is shutting down,Good bye')
                playsound.playsound("power down.mp3")
                print('your personal assistant JARVIS is shutting down,Good bye')
                sys.exit()


