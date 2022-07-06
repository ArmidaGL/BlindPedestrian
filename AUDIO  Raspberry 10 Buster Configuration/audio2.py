from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_mp3('/home/pi/Desktop/iniciado.mp3')
play(sound)
