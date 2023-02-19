import requests
import pyttsx3
engine = pyttsx3.init()

response = requests.get("https://api.kanye.rest/text")

print(response.text)

text = response.text

text = text.replace(' ','%20')

print ("before : "+ text)
#
response = requests.get("https://api.funtranslations.com/translate/yoda.json?text=" + text)
#
print(response.json())

json = response.json()

translated = json['contents']["translated"]

print("after : " + translated)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.say("I AM YANYE")
engine.say(translated)
engine.runAndWait()

