import  random
from flask import Flask
app = Flask(__name__)

print(__name__) # __main__

random_number = random.randint(0,9)
print(f"The random number between 0 and 9 is {random_number}")


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9, Type in the URL </h1><br>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:guess_number>")
def guess_number(guess_number):
    if random_number > guess_number:
        return f"<h1> You have guessed a lower number, Guess again, the correct number was {random_number}</h1><br>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

    elif random_number < guess_number:
        return f"<h1>You have guessed a higher number, Guess again, the correct number was {random_number}</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

    else: # check_number == guess_number
        return "<h1>You have guessed the correct number, Congratulations!!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

if __name__=="__main__":
    app.run(debug=True)
