#~!/usr/bin/env python

import SimpleMFRC522
import RPi.GPIO as GPIO
import sys, time

redPin = 17
greenPin = 27
bluePin = 22

def setup():
    print("Setting up")
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(redPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(greenPin, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(bluePin, GPIO.OUT, initial=GPIO.LOW)
    print("Setup complete")
    
def ledRed():
    GPIO.output(redPin, GPIO.HIGH)
    
def ledGreen():
    GPIO.output(greenPin, GPIO.HIGH)
    
def ledBlue():
    GPIO.output(bluePin, GPIO.HIGH)
 
def ledOff(pin):
    if pin != None:
        GPIO.output(pin, GPIO.LOW)

def ledOffAll():
    GPIO.output(redPin, GPIO.LOW)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(bluePin, GPIO.LOW)

setup()
reader = SimpleMFRC522.SimpleMFRC522()
currentState = {}
try:
    while True:
	id, text = reader.read()
##	print(id)
##	print(text)
	text = text.strip()
        if currentState.has_key(text):
            ledOff(currentState[text])
            del currentState[text]
        else:
            if text == "1002381683":
                ledRed()
                currentState[text] = 17       
            elif text ==  "1013568194":
                ledBlue()
                currentState[text] = 22
        time.sleep(1)
finally:
        print("cleaning up ...")
        ledOffAll
	GPIO.cleanup()





