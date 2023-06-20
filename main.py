import os
import speech_recognition as sr
import win32com.client as wc
import webbrowser
import openai
from config import apikey
import datetime
import random

def ai(content):
    openai.api_key = apikey
    text = f"OpenAi response for message :{content}\n*******************************************************\n\n"
    
    completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'user', 'content': ''}
    ],
    temperature = 0  
    )
    print(completion['choices'][0]['message']['content'])
    text = text + completion['choices'][0]['message']['content']
    if not os.path.exists('Openai'):
        os.mkdir('Openai')

    with open(f"content- {random.randint(1,3242324534)}","w") as f:
        f.write(text)

def say(text):
    speaker = wc.Dispatch("Sapi.SpVoice")
    speaker.Speak(text)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        r.energy_threshold = 800  # minimum audio energy to consider for recording
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said :{query}")
            return query
        except Exception as e:
            return "some error occurred.Sorry from jarvis."


if __name__ == '__main__':
    say("myself jarvis how can i help you ")
    while True:
        print("Listening.....")
        query=takecommand()

        # say(query)
        sites=[["YouTube","https://youtube.com"],["Wikipedia","https://wikipedia.com"],["Postman","https://postman.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir.....")
                webbrowser.open(f"{site[1]}")
        if "play music" in query:
            musicPath = "https://www.youtube.com/watch?v=dsnuu20RSFU"
            os.startfile(musicPath)
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            print(strfTime)
            say(f"Sir the time is {hour} bajj k {min} minute")
        if "open whatsApp".lower() in query.lower():
            whatsapp = "https://web.whatsapp.com/"
            webbrowser.open(whatsapp)

        if "using AI".lower() in query.lower():
            ai(content=query)
