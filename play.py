import time
from pygame import mixer


mixer.init()
mixer.music.load("C:/Users/akasp/OneDrive/Desktop/die-melodie/Calm-and-Peaceful.mp3")
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(0.5)

