import speech_recognition as sr
import pyttsx3
import pyjokes
import webbrowser
import os
import time
import pyautogui
import subprocess
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

assis_name = "Naresh"
boss_name = "Naresh Kumar"

def say(text):
    """Function to speak the given text."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    """Function to listen to the user's voice and return the text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing..............")
            text = r.recognize_google(audio, language='en-in')
            print(f"user said: {text}\n")
            return text.lower()  
        except sr.UnknownValueError:
            print("Could not understand the audio")
            say("Sorry, I did not understand what you said. Could you please repeat?")
            return "none"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            say("There seems to be an issue with the speech recognition service.")
            return "none"
        except Exception as e:
            print(f"An error occurred: {e}")
            say("Sorry, something went wrong.")
            return "none"

def tell_joke():
    """Function to get a random joke."""
    return pyjokes.get_joke()

def search_youtube(query):
    """Function to search YouTube based on the user's input."""
    path = "D:\\Year-3 Term-1 Internship\\AI Voice Assistant Project\\chromedriver.exe"
    service = Service(executable_path=path)
    driver = webdriver.Chrome(service=service)
    url = 'https://www.youtube.com/'
    try:
        driver.get(url)
        search = driver.find_element(By.NAME, 'search_query')
        search.send_keys(query)
        search.send_keys(Keys.RETURN)
        input("Press Enter to close the browser...")
    except Exception as e:
        print(f"Error occurred while searching on YouTube: {e}")
    finally:
        driver.quit()  

def locate_with_retry(image_path, retries=5, confidence=0.75, delay=1):
    """Tries to locate the image on screen, retrying if not found."""
    for _ in range(retries):
        button = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if button is not None:
            return button
        time.sleep(delay)
    return None
def get_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    return Time

def get_date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)

    date = day + "/" + month + "/" + year
    return date

def Wishing():
    h = datetime.datetime.now().hour
    if h >= 0 and h < 12:
        wish = "Good Morning"
    elif h >= 12 and h < 15:
        wish = "Good Afternoon"
    elif h >= 15 and h < 19:
        wish = "Good Evening"
    else:
        wish = "Good Night"
    return wish

if __name__ == "__main__":
    print("The Time is: ", get_time())
    print("The Date is: ", get_date())
    print(Wishing())


def sign_in(meetingid):
    zoom_path = r"C:\\Users\\HP\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
    try:
        subprocess.call(zoom_path)
        time.sleep(7)  
        pyautogui.hotkey('alt', 'tab')  
        
        print("Taking a screenshot for debugging...")
        pyautogui.screenshot('screenshot.png')  

        print("Looking for the first join button...")
        join_btn1 = locate_with_retry(r'D:\\Year-3 Term-1 Internship\\AI Voice Assistant Project\\New folder\\join-2.png', retries=10, confidence=0.7)
        
        if join_btn1 is not None:
            pyautogui.moveTo(join_btn1)
            pyautogui.click()
            time.sleep(3)
        else:
            print("First Join button not found!")
            return
        
        pyautogui.write(meetingid)
        time.sleep(2)
        
        print("Looking for the second join button...")
        join_btn2 = locate_with_retry(r'D:\\Year-3 Term-1 Internship\\AI Voice Assistant Project\\New folder\\join-3.png', retries=10, confidence=0.7)
        
        if join_btn2 is not None:
            pyautogui.moveTo(join_btn2)
            pyautogui.click()
            time.sleep(3)
        else:
            print("Second Join button not found!")
            return
    except Exception as e:
        print(f"Error during sign in: {e}")  

def respond(text):
    """Function to respond based on the user input."""
    if 'hi' in text:
        say("Hi Sir!")
    elif "who are you" in text:
        say(f"My name is {assis_name}")
    elif "good morning" in text:
        say(f"A warm {text}")
        say(f"How are you, {boss_name}?")
    elif "i am fine" in text:
        say("Oh really good")
    elif "who am i" in text:
        say("If you talk then definitely you're human.")
    elif "where am i" in text:
        say("You are in a comfortable place, I hope!")
    elif 'thank you so much' in text:
        say("It's my pleasure!")
    elif 'fine' in text or "good" in text:
        say("It's good to know that you're fine.")
    elif 'tell me a joke' in text:
        engine2 = pyttsx3.init()
        engine2.setProperty('rate', 100)
        engine2.say(tell_joke())
        engine2.runAndWait()
    elif 'open my site' in text:
        webbrowser.open('https://github.com/')
    elif 'open' in text:
        text = text.replace("open", "").strip()
        if 'notepad' in text:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++.lnk")
        elif 'eclipse' in text:
            os.startfile("C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\eclipse.lnk")
    elif 'close' in text:
        text = text.replace("close", "").strip()
        if 'notepad' in text:
            os.system("TASKKILL /F /IM notepad++.exe")
        elif 'eclipse' in text:
            os.system("TASKKILL /F /IM eclipse.exe")
    elif 'search youtube' in text:
        query = text.replace("search youtube", "").strip()  
        search_youtube(query)
    elif 'join class' in text:
        sign_in('750 759 1770')

if __name__ == "__main__":
    while True:
        text = takecommand()
        if text != "none": 
            respond(text)
