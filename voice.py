import pyttsx3 
from pathlib import Path
import json

def finalvoice():
    engine = pyttsx3.init()  
    raw_voice = Path("post_data.json").read_text()
    final_voice = json.loads(raw_voice.replace("post_body",""))
    
    #female voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  
    
    #slow voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    
    #say voice
    #engine.say(final_voice)
    print("passed 3")
    
    #save to path
    output_path = r'C:\Users\Lenovo\OneDrive\Desktop\reddit video\test.mp3'
    engine.save_to_file(final_voice, output_path)
    
    #run
    engine.runAndWait()



