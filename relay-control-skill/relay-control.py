'''
Alexa Custom Skill to control any device using a relay
    - Uses the flask-ask library

Usage:
Alexa, tell my device to turn on
Alexa, ask my device to turn off

Created by: Lee Assam
www.powerlearningacademy.com

Last Modified: 2018-09-02
'''

from flask import Flask, render_template
from flask_ask import Ask, statement, question
import RPi.GPIO as GPIO #use GPIO library

#initializing GPIO
GPIO.setwarnings(False)
outputPin = 11 #pin 11 is connected to the relay board
GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(outputPin, GPIO.OUT)   # Set pin's mode as output
GPIO.output(outputPin, GPIO.HIGH) # Set outputPin  high to turn off the device

#initializing flask ask
app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launch():
    welcome_text = render_template('welcome_text')
    return question(welcome_text)

@ask.intent('AMAZON.FallbackIntent')
def fallback():
    reprompt_text = render_template('command_reprompt')
    return question(reprompt_text)

@ask.intent('OnOffIntent')
def control(OnOff):
    command = OnOff
    if command is None:
        #no command was given
        reprompt_text = render_template('command_reprompt')
        return question(reprompt_text)
    elif command == "on" or command == "off":
        if command == "off":
            #turn OFF
            GPIO.output(outputPin, GPIO.HIGH)
        else:
            #turn ON
            GPIO.output(outputPin, GPIO.LOW)
        response_text = render_template('command', onOffCommand=command)
        return statement(response_text).simple_card('Command', response_text)
    else:
        #a valid command was not given
        reprompt_text = render_template('command_reprompt')
        return question(reprompt_text)

if __name__ == '__main__':
    app.run(debug=True)
