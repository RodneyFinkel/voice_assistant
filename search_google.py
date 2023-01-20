import speech_recognition as sr
import subprocess
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
    
def say(text):
    subprocess.call(['say', text])

# Using Selenium
s = Service('/usr/local/bin/chromedriver')
def google_search(search_term):
    print('activating selenium')
    browser = webdriver.Chrome()
    browser.get('http://www.google.com')
    search = browser.find_element_by_name('q')
    search.send_keys(search_term)
    search.send_keys(Keys.RETURN)
    
def activate(phrase='computer activate'):
    r = sr.Recognizer()
    mic = sr.Microphone()
    try:
        with mic as source:
            # r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            if transcript.lower() == phrase:
                say('Activated!')
                return True
            else:
                say('what is your request sir?')
                return False
    except:
        print("listening")

r = sr.Recognizer()
mic = sr.Microphone() 

while True:
    if activate() == True:
        try:
            say("Hello Sir, how can I help you today?")
            with mic as source:
                print('Say Something!')
                # r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                transcript = r.recognize_google(audio)
                phrase = 'search for'
                if phrase in transcript.lower():
                    search_term = transcript.lower().split(phrase)[-1]
                    say(f"Yes sir, I will begin searching for {search_term} immediately!")
                    google_search(search_term)
                    say("Here are the results Sir!")
                else:
                    say('I could not understand your query {search_term}, please try again..')
        except:
            print("pass1")
    else:
        print("pass2")
            
            
            