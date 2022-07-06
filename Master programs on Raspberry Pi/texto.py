import pyttsx3
engine = pyttsx3.init('espeak')
engine.say('Hello World')
engine.runAndWait()