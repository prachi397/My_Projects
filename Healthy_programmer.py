#_____________________________________________________________________HEALTHY PROGRAMMER_____________________________________________________________________________________
"""9am - 5pm
water - water.mp3  (3.5 liter in every 40 min) - to stop this mp3 - drank - a log will be generated in a text file
eyes - eyes.mp3 -  every 30 min - eydone - log
physical activity - physical.mp3 every 45 min - exdone -log
rules -->
you will have to manage the clashes between the reminders
pygame module to play audio

"""
from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):# file is that file which we have to play and stopper is to stop
     mixer.init()   #init function resides inside the mixer
     mixer.music.load(file)
     mixer.music.play()
     while True:
         a = input()
         if a == stopper:
             mixer.music.stop()
             break
def log_now(msg):
     with open("mylogs.txt", "a") as f:
          f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs = 10
    eyesecs =20
    while True:
         if time() - init_water > watersecs:
              print("water drinking time. enter 'drank' to stop the alarm")
              musiconloop("water.mp3", "drank")
              init_water = time()
              log_now("drank water at")
         if time() - init_eyes > eyesecs:
              print("eye exercise time. enter 'doneeyes' to stop the alarm")
              musiconloop("eyes.mp3", "doneeyes")
              init_eyes = time()
              log_now("eyes relaxed at")
         if time() - init_exercise > exsecs:
              print("physical activity time. enter 'donephy' to stop the alarm")
              musiconloop("physical.mp3", "donephy")
              init_exercise = time()
              log_now("physical activity done at")
                  
