import speech_recognition as sr
import subprocess
import os

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
                say('what the fuck did you say to me?')
                return False    
    except:
        print('listening')
           
          
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
                    if phrase in transcript.lower():
                        search_term = transcript.lower().split(phrase)[-1]
                        say(f"Yes sir, here is {search_term} for you!")
                        d = '/Applications'
                        apps = list(map(lambda x: x.split('.app')[0], os.listdir(d)))
                        app = search_term
                        os.system('open '+d+'/%s.app' %app.replace(' ','\ '))
                        print(apps)   
                    else:
                        say('I could not understand your query, please try again..')
            except:
                print("pass1")
        else:
            print("pass2")    
                  
loop()
      
        

        
    

    
   
   