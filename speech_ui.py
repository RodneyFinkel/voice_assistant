import speech_recognition as sr
import subprocess
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s = Service('/usr/local/bin/chromedriver')


def say(text):
    subprocess.call(['say', text])

def activate(phrase='activate'):
    r = sr.Recognizer()
    mic = sr.Microphone()
    try:
        with mic as source:
            # r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            if transcript.lower() == phrase:
                say('activated')
                return True
            else:
                say('what the hell did you say to me?')
                return False    
    except:
        print('listening')
 
        
def find_app(search_term):
    d = '/Applications'
    apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
    app = search_term
    os.system('open '+d+'/%s.app' %app.replace(' ','\ '))
    print(apps)
    
    
def google_search(search_term):
    print('activating selenium')
    browser = webdriver.Chrome()
    browser.get('http://www.google.com')
    search = browser.find_element_by_name('q')
    search.send_keys(search_term)
    search.send_keys(Keys.RETURN)


def close_app(search_term):
    d = '/Applications'
    apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
    app=search_term
    os.system('TASKKILL /F '+d+'/%s.app' %app.replace(' ','\ '))
        
                                           
def loop():         
    r = sr.Recognizer()
    mic = sr.Microphone() 
    while True:
        if activate() == True:
            try:
                say("Hello Sir, which application would you prefer?")
                with mic as source:
                    print('Say Something!')
                    # r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    transcript = r.recognize_google(audio)  
                    phrase = 'open '
                    phrase2 = 'go to'
                    phrase3 = 'close '
                    if phrase in transcript.lower():
                        search_term = transcript.lower().split(phrase)[-1]
                        say(f"Yes sir, here is {search_term} for you!")
                        find_app(search_term)
                    elif phrase2 in transcript.lower():
                        search_term = transcript.lower().split(phrase2)[-1]
                        say(f'taking you to google search for {search_term} sir!')
                        google_search(search_term)
                    elif phrase3 in transcript.lower():
                        search_term = transcript.lower().split(phrase3)[-1]
                        say(f'closing {search_term} for you!')
                        close_app(search_term)
                    else:
                        say('please try again')
                        
            except:
                print("pass1")
        else:
            print("pass2")    
            
loop()



    
   

    
    
    
    
    
    
    
    
    
    