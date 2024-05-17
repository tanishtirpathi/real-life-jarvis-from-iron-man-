import pyttsx3  
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import ctypes
import pywhatkit
import keyboard
from pyautogui import hotkey
import wolframalpha
import pyaudio      
import struct
import math
from time import sleep
from keyboard import add_hotkey
from keyboard import press_and_release
from keyboard import press
from pyautogui import click
# import pyautogui
import psutil
import os
from plyer import notification
import random
import wikipedia as googleScrap
# import openai
# import time
# import smtplib
import requests
# from bs4 import BeautifulSoup
from time import sleep
INITIAL_TAP_THRESHOLD = 0.2
FORMAT = pyaudio.paInt16
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 2
RATE = 44100  
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME                    
UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME 
MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engne = pyttsx3.init('sapi5')
voices = engne.getProperty('voices')
engne.setProperty('voices',voices[1].id)
def get_rms( block ):
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )
    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt( sum_squares / count )
class TapTester(object):

    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        self.noisycount = MAX_TAP_BLOCKS+1 
        self.quietcount = 0 
        self.errorcount = 0

    def stop(self):
        self.stream.close()

    def find_input_device(self):
        device_index = None            
        for i in range( self.pa.get_device_count() ):     
            devinfo = self.pa.get_device_info_by_index(i)   
            # print( "Device %d: %s"%(i,devinfo["name"]) )

            for keyword in ["mic","input"]:
                if keyword in devinfo["name"].lower():
                    # print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
                    device_index = i
                    return device_index

        if device_index == None:
            print( "No preferred input found; using default input device." )

        return device_index

    def open_mic_stream( self ):
        device_index = self.find_input_device()

        stream = self.pa.open(   format = FORMAT,
                                 channels = CHANNELS,
                                 rate = RATE,
                                 input = True,
                                 input_device_index = device_index,
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

        return stream

    def listen(self):

        try:
            block = self.stream.read(INPUT_FRAMES_PER_BLOCK)

        except IOError as e:
            self.errorcount += 1
            print( "(%d) Error recording: %s"%(self.errorcount,e) )
            self.noisycount = 1
            return

        amplitude = get_rms( block )

        if amplitude > self.tap_threshold:
            self.quietcount = 0
            self.noisycount += 1
            if self.noisycount > OVERSENSITIVE:

                self.tap_threshold *= 1.1
        else:            

            if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
                return "True-Mic"
            self.noisycount = 0
            self.quietcount += 1
            if self.quietcount > UNDERSENSITIVE:
                self.tap_threshold *= 2
def Tester():

    tt = TapTester()

    while True:
        kk = tt.listen()
        if "True-Mic" == kk:
            print("Hi ! sir my name is JARVIS A virtual assistant your welcome Mr Tanish " )
            break
Tester()
def takecommand():  
       r = sr.Recognizer()   
       with sr.Microphone() as source:
        #print("listening....................")
        #speak("yes sir speak")
        #r.pause_threshold = 1
       # audio = r.listen(source,0,9)
        print('Listening........................')
        r.pause_threshold = 1
       # r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

        try:
            print(" recognisinging ")
           # speak("wait sir")   
            query = r.recognize_google(audio,language='en-in')
            print(" ")
            print(f"you:{query}")
            print(" ")
            print("JARVIS :- ")
            return query
        except Exception as e:
             speak(" b.....")   
             print("please speak again............")
             return "some internet issue boss please forgive me"
         
         
         
def speak(audio):
   engine.say(audio)
   engine.runAndWait()
def temp():
    api_key = "3GRREJ-UKAW3UAWY4"
    client = wolframalpha.Client(api_key)
    res = client.query(' weather at hemicahal ,punjab')
    return 298  
current_temp = temp()
celsius_temp = current_temp - 273.15  


def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        tim = datetime.datetime.now().strftime("%I %M %p ")
        speak("good morning  boss")
        speak(f"its {tim}")
        speak(f"Current temperature is {celsius_temp:.2f} °C")
        speak("lets start the work boss")
        
    elif hour>=12 and hour<16:
        tim = datetime.datetime.now().strftime("%I %M %p")
        speak("welcome back boss")
        speak(f"its {tim}")
        speak(f"Current temperature is {celsius_temp:.2f} °C")
        speak("lets start the work boss")
        
    elif hour>=16 and hour<19:
        time = datetime.datetime.now().strftime("%I %M %p ")
        speak("welcome back boss")
        speak("lets start the work boss")
        
        
    elif hour>=19 and hour<23:
        time = datetime.datetime.now().strftime("%I %M %p ")
        speak("welcome back boss")
        speak("how s you day sir ")
        speak("lets start the work boss")
        
    else:
        time = datetime.datetime.now().strftime("%I %M %p ")
        speak(f"its {tim}")
        speak(f"Current temperature is {celsius_temp:.2f} °C")
        speak("its time to sleep boss   ")
        
        
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)
if __name__ == "__main__": 
    wishMe()   
    while  True:
        query = takecommand().lower() 
        
        if 'google ' in query or'show ' in query or'dikhao' in query  or'dikhna' in query:       
            query = query.replace("jarvis","")
            query = query.replace("show that","")
            query = query.replace("google search","")
            query = query.replace("show me","")
            query = query.replace("google","")
            query = query.replace("kro","")
            query = query.replace("karo","")
            query = query.replace("kardo","")
            query = query.replace("krodo","")   
            query = query.replace("about","")
            speak("This Is What I Found On The Web!")   
            pywhatkit.search(query)
            try:
                result = googleScrap.summary(query,2)
                speak(result)
                print(result)
            except: 
                  speak("No Speakable Data Available!") 
        elif 'close all tab' in query:
            speak("ok sir as your wish")
            keyboard.press_and_release('ctrl+shift+w')   
        elif 'close tab' in query:
            speak("ok sir as your wish")
            keyboard.press_and_release('ctrl+w')
        elif 'lock' in query:
            speak('As You Wish')
            ctypes.windll.user32.LockWorkStation()
            exit()
        elif 'website'in query:
            speak("booss which website i have to open ") 
            name = takecommand().lower()
            we = 'https://www.' + name +'.com'
            webbrowser.open(we)
            speak(f"opening{name}") 
        elif 'song'in query:
            speak("booss which song you have to listen ") 
            nme = takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={nme}")
            speak(f"you can choose any music related to {nme}")  
        elif 'youtube'in query:
            webbrowser.open(f"https://www.youtube.com")
            speak(f"yyoutube opening")  
        elif 'cmd' in query:
            speak("starting ")
            os.system("start cmd") 
        elif 'music' in query:
            music_dir = "C:\\Users\\tanish\\Music\\music song"
            song = os.listdir(music_dir)
            rd = random.choice(song)
            os.startfile(os.path.join(music_dir, rd))  
        elif 'goodbye friday'in query:
            speak("good bye boss you can call me anytime ")
            speak("bye bye ")
            break
        elif 'weather' in query or'temperature' in query or'mosam' in query  or'masom' in query:    
            speak("speak the place sir")  
            l=takecommand().lower()  
            if 'outside 'in l or 'bhar ' in l or 'bhr' in l:
                pywhatkit.search(f"weather today near Jhakhar Pindi, Punjab")
                speak("see the weather boss ")
            else:
                pywhatkit.search(f"today weather in {l}")
                speak(f"sir the weather in {l} is ")
        elif ' play  sad song' in query:
            webbrowser.open("https://youtu.be/lyOo1MZawU0?si=5_DUaA7GEOYVRyho") 
            speak("playing song")
        elif 'gpt' in query:
            speak('opening gemini sir ') 
            webbrowser.open("https://gemini.google.com/app/8fb4f1d730e5a5d2")
        elif 'gpt4' in query or 'gpt four ' in query or 'gpt for 'in query :
            speak('opening gpt sir ') 
            webbrowser.open("https://chat.openai.com/")
        elif 'Trucaller ' in query:
            webbrowser.open("truecaller.com")
            speak("ok now sir ") 
        elif 'google open' in query:    
           speak("what sould i have to search ")   
           cm = takecommand().lower()   
           webbrowser.open(f"{cm}")    
        elif 'youtube search' in query:          
            speak("sir what should i have to search ") 
            cm = takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")
            speak("searching")
            pywhatkit.playonyt(cm)
            speak("this may also help you boss")
        elif 'whatsapp ' in query:
             speak("speak the number boss")
             contact= takecommand().lower()
             num = '+91'+ contact
             speak("What do you want to say?")
             message = takecommand().lower()
             speak("When to send?")
             s_time= takecommand().lower()
             if 'later' in s_time:
                 speak ("Tell me about the hour?")
                 hour__ =int(takecommand().lower())
                 speak("Tell me about the minutes?")
                 minute__ =int(takecommand().lower())
             elif 'now' in s_time:
                hour__ = (datetime.datetime.now().hour)
                if (datetime.datetime.now().second) < 30:
                    minute__ = (datetime.datetime.now().minute) + 1
                else:
                    minute__=(datetime.datetime.now().minute) + 2
             speak("Sending Message.")
             pywhatkit.sendwhatmsg(num, message, hour__,minute__)        
        elif ' Instagram' in query:
            webbrowser.open("https://www.instagram.com//")
            speak("ok now sir ") 
        elif 'snapchat' in query:
            webbrowser.open("https://www.snapchat.com//")
            speak("ok now sir ") 
        elif 'gmail ' in query:
            webbrowser.open("gmail.com")
            speak("ok now sir ") 
        elif 'papa ko message ' in query:  
             num = '+918437493081' 
             speak("What do you want to say?")
             message = takecommand().lower()
             speak("When to send?")
             s_time= takecommand().lower()
             if 'later' in s_time:
                 speak ("Tell me about the hour?")
                 hour__ =int(takecommand().lower())
                 speak("Tell me about the minutes?")
                 minute__ =int(takecommand().lower())
             elif 'now' in s_time:
                hour__ = datetime.datetime.now().hour
                if (datetime.datetime.now().second) < 30:
                    minute__ = (datetime.datetime.now().minute) + 1
                else:
                    minute__=(datetime.datetime.now().minute) + 2
             speak("Sending Message.")
             pywhatkit.sendwhatmsg(num, message, hour__,minute__)  
             speak(f"done boss message sent to{num} ")
        elif 'plan' in query:
            webbrowser.open("https://www.notion.so/School-jee-framewok-7a58dbfbbfe141fe96a7663db2619bfd")
            speak("tanish boss plan your day")          
        elif 'coding time' in query:
            e= "jarvis app backup\\Visual Studio Code.lnk"
            os.startfile(e)    
            speak("opening vs code") 
        elif 'my day ' in query:
             webbrowser.open("https://calendar.google.com/calendar/u/0/r")
             speak("ok sir i will")
        elif 'time table ' in query:
             webbrowser.open("https://docs.google.com/document/d/1ptEb30nZxz2P-uKjZkLpzhGCZoZAK2_gS27FlycFtO8/edit#heading=h.h4kgoop6fffj")
             speak("ok sir i will")
        elif 'message' in query:
             ont = takecommand().lower()
             cont = '+91'+ ont 
             mess = takecommand().lower()    
        elif 'what is your name ' in query:
            speak("my name is jarvis boss") 
            print("my name is jarvis boss")
        elif 'how are you friday ' in query:
            speak("i am fine boss what about you") 
            print("my name is friday boss")  
        elif 'charge' in query or 'power' in query or 'jaan' in query or 'batery' in query or 'jan' in query: 
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent) 
            time_left = secs2hours(battery.secsleft)
            print (percent)
            if percent < 45:
                speak('sir, please connect charger because i can survive only '+ time_left)
            if percent > 45:
                speak("boss its your choice t charge me but i can survive  "+ time_left)
            else:
                speak("don't worry sir, charger is connected")       
        elif 'name'  in query:
            speak('My name is JARVIS boss')
        elif 'who made you' in query:
            speak ("I was created by Mr.Tanish sharma")
        elif "mark 2" in query or "mark two" in query or "mark-2" in query  or "mark to" in query:
            speak("voice activation required boss")
            e_passcode = takecommand().lower()
            v_passcode = "iron man"
            if e_passcode == v_passcode:
                speak("acess granted!, Welcome back! Mr.Tanish")
                webbrowser.open("https://github.com/tanishtirpathi/") 
                speak("boss i'm saving the progress")
                ol =takecommand().lower()
                if 'ok'in ol or 'thik hai 'in ol or 'yes' in ol: 
                    speak("saving...............")
                    speak("thank you sir for your permission")  
                else:
                    speak("ok sir as your wish boss")       
            else:
                speak("access decline")