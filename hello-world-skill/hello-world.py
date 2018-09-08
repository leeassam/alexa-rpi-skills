'''
Alexa Hello World Custom Skill to demonstrate how flask-ask works
    - Uses the flask-ask library

Usage:
Alexa, tell hello world to say hi to {firstname}
Alexa, ask hello world to say hi to {firstname}

Created by: Lee Assam
www.powerlearningacademy.com

Last Modified: 2018-09-02
'''

from flask import Flask, render_template
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launch():
    welcome_text = render_template('welcome_text')
    return question(welcome_text)

@ask.intent('AMAZON.FallbackIntent')
def fallback():
    reprompt_text = render_template('ask_name_reprompt')
    return question(reprompt_text)

@ask.intent('HelloWorldIntent')
def hello(firstname):
    if firstname is None:
        #no name was given
        ask_name_text = render_template('ask_name')
        return question(ask_name_text)
    response_text = render_template('hello', firstname=firstname)
    return statement(response_text).simple_card('Hello', response_text)

if __name__ == '__main__':
    app.run(debug=True)
