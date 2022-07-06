from gps import *
from geopy.geocoders import Nominatim
import pyttsx3

running = True

def getPositionData(gps):
    nx = gpsd.next()
        
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
        #print ("Tu posicion: lon = " + str(longitude) + ", lat = " + str(latitude))

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

geolocalizador = Nominatim(user_agent= 'master_gps')
ubicacion=geolocalizador.reverse('longitude','latitude')
ubi=ubicacion.address
print(ubi)


engine = pyttsx3.init('espeak')
engine.setProperty("rate",120)
engine.say('Your position ' +ubi)
#text = ("Tu posicion " +ubi)
#output_file = "audio.mp3"
#engine.save_to_file("text", "output_file")
engine.runAndWait()