from flask import Flask
from flask import Flask
import random
random_number = random.randint(0,9)
print(random_number)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='color:black;'>Guess a Number between 0 and 9!</h1>" \
            \
           "<img src='https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp' alt=Girl in a jacket'>"


@app.route("/<int:number>")
def check(number):
    if number > random_number:
        return "<h1 style='color:red;'>Sorry, too high!</h1>" \
               \
               "<img src='https://media4.giphy.com/media/3FNCFXeaVSwEM/giphy.webp?cid=ecf05e47blrovuetsrq0lil4gwkrpecscvswuboiv6tjjynm&rid=giphy.webp&ct=g' alt=Girl in a jacket'>"
    if number < random_number:
        return "<h1 style='color:red;'>Sorry, too low!" \
               \
               "<img src='https://media1.giphy.com/media/gmslqIqkiMbgrvBqhZ/200w.webp?cid=ecf05e47blrovuetsrq0lil4gwkrpecscvswuboiv6tjjynm&rid=200w.webp&ct=g' alt=Girl in a jacket'>"
    if number == random_number:
        return "<h1 style='color:green;'>You right, congratulations!" \
               \
               "<img src='https://media1.giphy.com/media/BPJmthQ3YRwD6QqcVD/200w.webp?cid=ecf05e47y97zus8noktmydjb5z3gop1pztgvwe79spduasek&rid=200w.webp&ct=g' alt=Girl in a jacket'>"
app.run(debug=True)