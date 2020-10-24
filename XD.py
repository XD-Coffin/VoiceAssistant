import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os 
import smtplib
import pyautogui

running = True
os.system("color a")
# Voice Setup;
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # Microphone input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening...")
        # increase seconds before completation of phrase
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio , language='en-us')
        print("User said: " +query)
    except Exception as e:
        print(e)
        print("Sorry sir please repeat sir..")
        return "None"
    return query

    
def wishMe():
    print("""
    o    o .oPYo.  o    o      .oo   .oPYo.        .oPYo. 
    8    8 8       8    8     .P 8       `8        8  .o8 
    8    8 `Yooo. o8oooo8    .P  8      oP'        8 .P'8 
    8    8     `8  8    8   oPooo8   .oP'          8.d' 8 
    8    8      8  8    8  .P    8   8'            8o'  8 
    `YooP' `YooP'  8    8 .P     8   8ooooo   88   `YooP' 
    :.....::.....::..:::....:::::..::.......::..::::.....:
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    """)
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<18:
        speak("Good Evening sir")
    else:
        speak("Good Evening sir")
    speak("Hi sir i am ussha your personal assistant please order me how may i help you")

if __name__ == "__main__":
    wishMe() 
    
    while running:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia sir')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query , sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("open google")
            webbrowser.open("google.com")

        elif 'bad' in query:
            speak("opening Porn")
            webbrowser.open("pornmilo.com")

        elif query=="who are you":
            speak("I am uusha your assistant")
        
        elif query=="who is your boss":
            speak("Mr Sahil Singh is whom i belong to")

        elif 'code' in query:
            speak("i would like vs code for you to code in")
            Code = "C:\\Users\\Coffin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(Code)

        elif query == "shut down please":
            speak("as you wish shutting down sir")
            running = False

        elif 'java ide' in query:
            speak("I know you hate this language but this is for your own good")
            java = "C:\\Program Files\\BlueJ\\BlueJ.exe"
            os.startfile(java)

        elif 'thank you' in query:
            speak("You dont need to say so sir but anyways you are most welcome.")

        elif 'open packet tracer' in query:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Cisco Packet Tracer\\Cisco Packet Tracer.exe"
            os.startfile(path)
        
        elif query == "i love you":
            speak("Ohh ,i love you a lot more too.")

        elif "hacking mode" in query:
            speak("Launching linux sir")
            path = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
            os.startfile(path)

        elif "notepad" in query:
            speak("opening notepad")
            os.startfile("notepad")

        elif "sweet" in query:
            speak("Playing in Youtube")
            speak("Checking Connection")
            speak("playing now")
            pyautogui.press("win")
            pyautogui.typewrite("firefox")
            pyautogui.press("enter" ,interval=0.2)
            pyautogui.click(417,65, interval=0.2)
            pyautogui.typewrite("youtu")
            pyautogui.press("enter" ,interval=3)
            pyautogui.click(644,127,interval=3)
            pyautogui.typewrite("sweet but phyco")
            pyautogui.click(1291,119, interval=2)
            pyautogui.click(505,321 ,interval=2)

        elif query == "search in youtube":
            r = sr.Recognizer()

            speak("What do you want to search in youtube")
            with sr.Microphone()as source:
                audio = r.listen(source)
                r.pause_threshold = 1
            
            try:
                search = r.recognize_google(audio,language="en-in")
                print(search)
                speak("searching "+search)
                pyautogui.press("win")
                pyautogui.typewrite("firefox")
                pyautogui.press("enter" ,interval=1)
                pyautogui.click(417,65, interval=1)
                pyautogui.typewrite("youtu",interval=2)
                pyautogui.press("enter" ,interval=3)
                pyautogui.click(644,127,interval=3)
                pyautogui.typewrite(search)
                pyautogui.click(1291,119, interval=2)
                pyautogui.click(505,321 ,interval=2)
            except Exception as e:
                speak("please speak again i don't understand.")
        
        elif query == "close background":
            pyautogui.hotkey("alt","f4")

        elif query == "close page":
            pyautogui.keyDown("ctrl")
            pyautogui.keyDown("w")   

        elif query == "wish me":
            wishMe()    

        elif query == 'pc sleep':
            pag = pyautogui
           
            pag.hotkey("win","x")
            pag.press("u")
            pag.press("s")   
        
        elif query == "pc shut down":
            pag = pyautogui
            pag.hotkey("win","x")
            pag.press("u")
            pag.press("u")
            
        elif query == 'text mode on':
            speak('Turning text mode on')
            query = input("write your query:")
            results = wikipedia.summary(query,sentences=4)
            speak(results)