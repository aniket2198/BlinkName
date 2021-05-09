#morse code blinker



import RPi.GPIO as GPIO

import time



GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setwarnings(False)

aniket = [".-", "-.","..", "-.-", ".", "-"]

dot = 0.5 #200 millis

i = 0



def fs():
    #print("flashSeq")
    for x in aniket:
        flash(x)

    time.sleep(dot * 3)


def flash(character):
    
    for x in character:
        if x == ".":
            GPIO.output(3, GPIO.HIGH)
            time.sleep(dot)
            GPIO.output(3, GPIO.LOW)
        elif x == "-":
            GPIO.output(3, GPIO.HIGH)
            time.sleep(dot * 3)
            GPIO.output(3, GPIO.LOW)
        time.sleep(dot)

try:

    while i != 1:
        fs()
        i = i + 1
except KeyboardInterrupt:
    GPIO.cleanup()

