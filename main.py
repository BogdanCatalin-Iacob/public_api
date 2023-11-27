from flask import Flask, request
from random import randint, choice
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():
    '''
    Returns the date, time, and a random phrase
    '''
    phrases: list[str] = ['Welcome', 'You are looking good today!', 'The weather is great!']
    return {'phrase': choice(phrases),
            'date': datetime.now()}


if __name__ == '__main__':
    app.run()