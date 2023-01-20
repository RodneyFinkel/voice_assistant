import speech_recognition as sr
import subprocess
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
s = Service('/usr/local/bin/chromedriver')

class voice_assistant(object):
    
    def __init__(self):
        self.self = self
        

    def say(self, text):
        subprocess.call(['say', text])


    def activate(self, phrase='activate'):
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
                    say('what the fuck did you say to me?')
                    return False    
        except:
            print('listening')
    
            
    def find_app(self, search_term):
        d = '/Applications'
        apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
        app = search_term
        os.system('open '+d+'/%s.app' %app.replace(' ','\ '))
        print(apps)
        
        
    def google_search(self, search_term):
        print('activating selenium')
        browser = webdriver.Chrome()
        browser.get('http://www.google.com')
        search = browser.find_element_by_name('q')
        search.send_keys(search_term)
        search.send_keys(Keys.RETURN)
        
                        
                        
    def loop(self):         
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
                        if phrase in transcript.lower():
                            search_term = transcript.lower().split(phrase)[-1]
                            say(f"Yes sir, here is {search_term} for you!")
                            find_app(search_term)
                        
                        else:
                            phrase2='go to'
                            search_term = transcript.lower().split(phrase2)[-1]
                            say(f'{search_term} hmmmm would you prefer google search instead sir?')
                            google_search(search_term)
                except:
                    print("pass1")
            else:
                print("pass2")    



if __main__ == '__main__':
    loop(self)
    





