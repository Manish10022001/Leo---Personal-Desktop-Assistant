import pyttsx3
import speech_recognition as sr
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui   ## pyatogui is very usefull, it basically control your keyboard
import keyboard
import random
import webbrowser
from plyer import notification
from pygame import mixer
import sys
import speedtest
from gui import Ui_MainWindow
import PyPDF2
from PyQt5 import   QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
# from PyQt5.QtGui import QMovie
# from PyQt5.QtCore import * 
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
# from leoui import Ui_leoui

##INTRO
from INTRO import play_gif
play_gif
## Password Protections
for i in range(3):
    a = input("Enter Password to open LEO :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate",170)
##1. Speek Function 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Undestanding..")
        query = r.recognize_google(audio,language="en-in")
        print(f"you said: {query}\n")
    except Exception as e:
        print("say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


def pdf_reader():
    book = open('asr report-2.pdf', 'rb')
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)  # Update here
    speak(f"Total numbers of pages in this book: {pages}")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.pages[pg]  # Update here
    text = page.extract_text()  # Update here
    speak(text)

##2. Greet Me Function 
if __name__=="__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak ("ok sir, you can call anytime")
                    break

                ## P.2 to change Password 
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                ##Conversations
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")


                #WEB SEARCH
                elif "google" in query:   
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)


                #TEMPERATURE
                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                ##time
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")

                ## finally sleep
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

                ## Open and Close apps/websites : Open and close apps like word, paint and various websites
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                    
                ##youtube controls
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                
                #location
                # elif 'location' in query:
                #     speak('What is the location?')
                #     location = takeCommand()
                #     url = 'https://google.nl/maps/place/' + location + '/&amp;'
                #     webbrowser.get('chrome').open_new_tab(url)
                #     speak('Here is the location ' + location)

                ##alarm
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

                ##Reminder
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("Leo","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())

                ## do this function later
                ##Personalized Playlist : Make your own playlist and let jarvis play a random song from it
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open  #(Here put the link of your video)

                ##News
                ##API - 38aa4834cf4247c789c4be909fab3f67
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                ##Calculator
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("leo","")
                    Calc(query)  

                ##WhatsApp
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                #send sms 
                elif "send message" in query:
                    speak("Sir what should i say")
                    msz = takeCommand()
                    
                    from twilio.rest import Client
                    import os

                    account_sid ='ACa526ab67c6fdd72033a203d4e19620f7'
                    auth_token ='7f9dd8709409c261f0214420ab5d27f2'
                    client = Client(account_sid, auth_token)

                    message = client.messages.create(
                        body=msz,
                        from_="+17163562165",
                        to="+918806903085"
                        )
                    
                #call
                elif "call" in query:
                    speak("Sir what should i say")
                    maz = takeCommand()

                    from twilio.rest import Clientl

                    account_sid ='ACa526ab67c6fdd72033a203d4e19620f7'
                    auth_token ='7f9dd8709409c261f0214420ab5d27f2'
                    client = Client(account_sid, auth_token)

                    message = client.calls .create(
                        twiml='msg',
                        from_="+17163562165",
                        to="+918806903085"
                    )

                #to open mobile camera
                # elif "Open mobile camera" in query:
                #     import urllib.request
                #     import cv2
                #     import numpy as np
                #     import time

                #     # URL of the mobile camera feed
                #     URL = "http://192.168.234.48:8080/shot.jpg"

                #     while True:
                #         try:
                #             # Read the image from the URL
                #             img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)

                #             # Decode the image
                #             img = cv2.imdecode(img_arr, -1)

                #             # Display the image
                #             cv2.imshow('IPWebcam', img)

                #             # Check for user input to quit (press 'q' to quit)
                #             q = cv2.waitKey(1)
                #             if q == ord("q"):
                #                 break
                #         except Exception as e:
                #             print("Error:", e)
                #             # Add any additional error handling as needed

                #     # Close all windows
                #     cv2.destroyAllWindows()

                # Password Protection
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                #Screenshot
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")


                #Read PDF
                elif "read pdf" in query:
                    pdf_reader()

                # ## Schedule my Day Function
                # elif "schedule my day" in query:
                #     tasks = []  # Empty list
                #     speak("Do you want to clear old tasks (Plz speak YES or NO)")
                #     query = takeCommand().lower()
                #     if "yes" in query:
                #         file = open("tasks.txt", "w")
                #         file.write("")
                #         file.close()
                #         no_tasks = int(input("Enter the no. of tasks :- "))
                # elif "no" in query:
                #         no_tasks = int(input("Enter the no. of tasks :- "))
                #         i = 0
                #         for i in range(no_tasks):
                #             tasks.append(input("Enter the task :- "))
                #             file = open("tasks.txt", "a")
                #             file.write(f"{i}. {tasks[i]}\n")
                #             file.close()
                #         # Add a condition to stop after entering a specific number of tasks
                #             if i + 1 == no_tasks:
                #                 speak("Tasks entered. Stopping the task entry.")
                #                 break


                # elif "show my schedule" in query:
                #     file = open("tasks.txt","r")
                #     content = file.read()
                #     file.close()
                #     mixer.init()
                #     mixer.music.load("notification.mp3")
                #     mixer.music.play()
                #     notification.notify(
                #     title = "My schedule :-",
                #     message = content,
                #     timeout = 15
                #     )
                
                ## Open any app
                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")  

                ## Internet speed
                #elif "internet speed" in query:
                 # download_net = wifi.download() / 1024 / 1024  # Convert to megabytes
                  #  print("Wifi Upload Speed is", upload_net)
                   # print("Wifi download speed is ", download_net)
                   # speak(f"Wifi download speed is {download_net:.2f} Mbps")  # Display with two decimal places
                    #speak(f"Wifi Upload speed is {upload_net:.2f} Mbps")
                
                # ##Cricket Score
                # elif "ipl score" in query:
                #     from plyer import notification  #pip install plyer
                #     import requests #pip install requests
                #     from bs4 import BeautifulSoup #pip install bs4
                #     url = "https://www.cricbuzz.com/"
                #     page = requests.get(url)
                #     soup = BeautifulSoup(page.text,"html.parser")
                #     team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                #     team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                #     team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                #     team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                #     a = print(f"{team1} : {team1_score}")
                #     b = print(f"{team2} : {team2_score}")

                #     notification.notify(
                #         title = "IPL SCORE :- ",
                #         message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                #         timeout = 15
                #     )
                
                ##FOCUS MODE
                elif "focus mode" in query:
                    if "focus mode" in query:
                        a = int(input("Are you sure that you want to enter focus mode? [1 for YES / 2 for NO] "))
    
                        if a == 1:
                            speak("Entering the focus mode....")
                            os.startfile("D:\\Leo\\FocusMode.py")
                            exit()
                    # a = (input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    # if(a==1):
                    # # speak("Are you sure that you want to enter focus mode? Say yes or no.")
                    # # a = takeCommand().lower()
                    # # if "yes" in a:
                    #     speak("Entering the focus mode....")
                    #     os.startfile("D:\\Leo\\FocusMode.py")
                    #     exit() ## if we want Leo to run the remove exit()
                    else:
                        pass

                
                elif "focus graph" in query:
                    from FocusGraph import focus_graph
                    focus_graph()

                # ##Translator
                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("Leo","")
                    query = query.replace("translate","")
                    translategl(query)
                    
                ## System Shutdown at last
                elif "shutdown the system" in query:
                    speak("Are you sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                        
                    elif shutdown == "no":
                        break
                

                # ##Send Email
                # elif 'email to adrito' in query:
                #     from sendEmail import sendEmail
                #     try:
                #         speak("What should I say?")
                #         content = takeCommand()
                #         to = "Receiver email address"
                #         sendEmail(to, content)
                #         speak("Email has been sent !")
                #     except Exception as e:
                #         print(e)
                #         speak("I am not able to send this email")

                # elif 'send a mail' in query:
                #     from sendEmail import sendEmail
                #     try:
                #         speak("What should I say?")
                #         content = takeCommand()
                #         speak("whome should i send")
                #         to = input()
                #         sendEmail(to, content)
                #         speak("Email has been sent !")
                #     except Exception as e:
                #         print(e)
                #         speak("I am not able to send this email")
                # elif "send a mail " in query:
                #     from sendEmail import sendEmail
                #     sendEmail()
                # class MainThread(QThread):
                #     def __init__(self):
                #         super(MainThread,self).__init__()

                #     def run(self):
                #         self.TaskExcecution(self):



                
            
