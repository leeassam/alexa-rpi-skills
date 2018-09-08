'''
Test Program to toggle a relay

Usage:
This program can be used to test a relay operation when connected to the Raspberry Pi
The relay is turned on for 2 secs and then off for 2 secs and this cycle repeats

Created by: Lee Assam
www.powerlearningacademy.com

Last Modified: 2018-09-02
'''
import RPi.GPIO as GPIO #use GPIO library
import time #use time library

GPIO.setwarnings(False)
outputPin = 11 #pin 11 is connected to the relay board
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(outputPin, GPIO.OUT)   # Set pin's mode as output
GPIO.output(outputPin, GPIO.HIGH) # Set outputPin  low to turn off the device



while True: # Continue looping indefinitely
  GPIO.output(outputPin, GPIO.LOW)  # Turn device on
  time.sleep(2) # Pause for 1 second
  GPIO.output(outputPin, GPIO.HIGH) # Turn device off
  time.sleep(2) # Pause for 1 second
