from flask import Flask

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return "<p>Hello, World jailsn e viado!</p>"

@app.route("/casa")
def ola_mundo():
    return "Oi, mundo josé carlo é frango"