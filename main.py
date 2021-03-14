"""
*************************************************************************
*    Course: 100 Days of Code - Dra. Angela Yu                          *
*    Author: Jorge Chavarriaga                                          *
*    Day: 55- Higher or Lower                                           *
*    Date: 2021-01-19                                                   *
*************************************************************************
"""

from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def game():
    global number
    number = random.randint(1, 10)
    return '<h1 style="color: Red">Guess the Number between 1 and 10:</h1><br>\n'\
           '<img src="https://media1.giphy.com/media/fsmjYTraGhq7Gp1WmB/giphy.gif">' \
           f'<h2>Please enter your answer in the URL as: <br><br>' \
           f'http://127.0.0.1/<b><em>YOUR_NUMBER</em></b>' \


@app.route('/<user_guess>')
def guess(user_guess):
    if user_guess.isalpha():
        you_are = "You must enter a number !!! "
        image = "https://media.giphy.com/media/SACoDGYTvVNhZYNb5a/giphy.gif"
        color = "blue"
    elif int(user_guess) < 1 or int(user_guess) > 10:
        you_are = "Out of the range !!!"
        image = "https://media.giphy.com/media/SACoDGYTvVNhZYNb5a/giphy.gif"
        color = "grey"
    elif int(user_guess) == number:
        you_are = "You found me !!!"
        color = "green"
        image = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
    elif int(user_guess) > number:
        you_are = "Too High, try again !"
        color = "magenta"
        image = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
    elif int(user_guess) < number:
        you_are = "Too Low, try again !"
        color = "red"
        image = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    else:
        you_are = "You are Wrong !!!"
    return f'<h1 style="color: {color}">{you_are}!! </h1><br>\n'\
           f'<img src="{image}">' \
           f'<h2>Please enter your answer in the URL as: <br><br>' \
           f'http://127.0.0.1/<b><em>YOUR_NUMBER</em></b>' \

@app.route('/answer')
def answer():
    return f'The right answer is: {number}'


if __name__ == "__main__":
    app.run(debug=True, port=8085)