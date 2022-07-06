#sudo apt-get install portaudio19-dev python3-pyaudio
#pip3 install pyaudio
#pip3 install pipwin
#pip3 install speechrecognition 
#pip3 install --upgrade speechrecognition

import webbrowser
import speech_recognition as sr
from time import sleep

r = sr.Recognizer() 
while True:
    with sr.Microphone() as source:
        print('Hola, soy tu asistente por voz: ')
        audio = r.listen(source)
 
        try:
            text = r.recognize_google(audio)
            print('Has dicho: {}'.format(text))
            print(text)
            if "Amazon" in text:
                webbrowser.open('https://www.amazon.com.mx/')
            if "PlayStation" in text:
                webbrowser.open('https://store.playstation.com/es-mx')
            if "que tal" in text:
                print("Bien y tu?")
            if "out" in text:
                print("Apagado")
                sleep(1)
                break
        except:
            print('No te he entendido')