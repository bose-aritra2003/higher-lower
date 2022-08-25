import random
from flask import Flask

app = Flask(__name__)

correct_num = random.randint(0, 9)
message = ['Too low, try again', 'Too high, try again', 'You found me']
images = [
    'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif',
    'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif',
    'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'
]


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<number>')
def play(number):
    guess = int(number)
    if guess == correct_num:
        return '<h1 style="color:green">' + message[2] + '</h1>' + '<img src="' + images[2] + '">'
    elif guess > correct_num:
        return '<h1 style="color:red">' + message[1] + '</h1>' + '<img src="' + images[1] + '">'
    else:
        return '<h1 style="color:blue">' + message[0] + '</h1>' + '<img src="' + images[0] + '">'


if __name__ == "__main__":
    app.run(debug=True)
