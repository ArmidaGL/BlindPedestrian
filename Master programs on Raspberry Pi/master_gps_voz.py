#pip3 install pydub
#pip3 install playsound

from gps import *
from geopy.geocoders import Nominatim
import pyttsx3

from pydub import AudioSegment
from pydub.playback import play
from time import time

import speech_recognition as sr

sound = AudioSegment.from_mp3('/home/pi/Desktop/Sistema_Master/Audio/subsistema_localizacion.mp3')
play(sound)
r = sr.Recognizer() 
while True:
    with sr.Microphone() as source:
        print('Subsistema de Localizacion: ')
        audio = r.listen(source)
 
        try:
            text = r.recognize_google(audio)
            print('Has dicho: {}'.format(text))
            print(text)
            if "location" in text:
                sound = AudioSegment.from_mp3('/home/pi/Desktop/Sistema_Master/Audio/dicho_ubicacion.mp3')
                play(sound)
                
                cont=1
                while (cont<=1):
                    
                    running = True

                    def getPositionData(gps):
                        nx = gpsd.next()
                            
                        if nx['class'] == 'TPV':
                            latitude = getattr(nx,'lat', "Unknown")
                            longitude = getattr(nx,'lon', "Unknown")
                            print ("Tu posicion: lon = " + str(longitude) + ", lat = " + str(latitude))

                        gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

                        try:
                            print ("Aplicacion iniciada!")
                            while running:
                                getPositionData(gpsd)
                                time.sleep(1.0)

                        except (KeyboardInterrupt):
                            running = False
                            print ("Aplicacion cerrada!")


                    def formatDegreesMinutes(coordinates, digits):
                        parts = coordinates.split(".")

                        if (len(parts) != 2):
                            return coordinates

                        if (digits > 3 or digits < 2):
                            return coordinates
                        
                        left = parts[0]
                        right = parts[1]
                        degrees = str(left[:digits])
                        minutes = str(right[:5])

                        return degrees + "." + minutes

                    geolocalizador=Nominatim(user_agent= 'Pruebas')
                    ubicacion=geolocalizador.reverse("20.391670, -99.994186")
                    ubi=ubicacion.address
                    print(ubi)


                    engine = pyttsx3.init('espeak')
                    engine.setProperty("rate",120)
                    engine.say('Your position ' +ubi)
                    #text = ("Tu posicion " +ubi)
                    #output_file = "audio.mp3"
                    #engine.save_to_file("text", "output_file")
                    engine.runAndWait()
                    cont+=1
                    
            if "out" in text:
                sound = AudioSegment.from_mp3('/home/pi/Desktop/Sistema_Master/Audio/sistema_apagado.mp3')
                play(sound)
                print("Apagado")
                break

        except:
            sound = AudioSegment.from_mp3('/home/pi/Desktop/Sistema_Master/Audio/repita.mp3')
            play(sound)
            print('No te he entendido')
