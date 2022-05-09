import random
from flask import Flask

app = Flask(__name__)

greetings = ["hello", "greetings", "hey", "howdy"]
places = ["world", "city", "borough", "municipality", "galaxy"]

@app.route("/hello") # handler
def hello():
    greeting = random.choice(greetings) + " " + random.choice(places)
    return greeting

@app.route('/')
def index():
    return "hello welcome to my website"

if __name__ == '__main__':
    app.run()