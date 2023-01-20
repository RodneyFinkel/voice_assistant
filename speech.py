# brew install elasticsearch in env vpice_assistant directory
# start elasticsearch in terminal before running module
# in env pip install 'elasticsearch<7.14.0'

import speech_recognition as sr
import subprocess
import os
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
        
def transcribe():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        transcript = r.recognize_google(audio)
        print(transcript)
    
def say(text):
    subprocess.call(['say', text])
    
d = '/Applications'
records = []
apps = os.listdir(d)
for app in apps:
    record = {}
    record['voice_command'] = 'open ' + app.split('.app')[0]
    record['sys_command'] = 'open ' + d +'/%s' %app.replace(' ','\ ')
    records.append(record)
    
es = Elasticsearch(['localhost:9200'])
bulk(es, records, index='voice_assistant', raise_on_error=True)

def search_es(query):
    res = es.search(index="voice_assistant", body={                     
    "query" :{
        "match": {
            "voice_command": {
                "query": query,
                "fuzziness": 2
            }
            }
        },
    })
    
    res1 = res['hits']['hits'][1]['_source']['sys_command']
    print(f'this is the system command: {res1}')
    return res1

def activate(phrase='wake up'):
    r = sr.Recognizer()
    mic = sr.Microphone()
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            if transcript.lower() == phrase:
                say('Activated!')
                return True
            else:
                return False
    except:
        print("listening")
                
r = sr.Recognizer()
mic = sr.Microphone()        
while True:   
    if activate() == True:
        try:
            say("Hello Sir, how can I help you?")
            with mic as source:
                print("Say Something!")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                transcript = r.recognize_google(audio)
                sys_command = search_es(transcript)
                os.system(sys_command)
                say("Here you go Sir!")
        except:
            pass
       
