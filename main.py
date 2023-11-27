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


@app.route('/api/random')
def random():
    '''
    Return to user a random number
    '''
    number_input = request.args.get('number', type=int, default=100)
    text_input = request.args.get('text', type=str, default='default_text')

    if isinstance(number_input, int):
        return {
            'input': number_input,
            'random': randint(0, number_input),
            'text': text_input,
            'date': datetime.now()
        }
    else:
        return {'Error': 'Please enter only numbers!'}


if __name__ == '__main__':
    app.run()