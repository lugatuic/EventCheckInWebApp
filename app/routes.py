from flask import Flask
from flask import render_template
from app import app

routes = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Events for the month</h1>'

#Personalizing with a dynamic route
@app.route('/login/<name>')
def swipe_manual(name):
    return '<h1>Please swipe/Thank you, {}!</h1>'.format(name)

@app.route('/login/<name>')
def manual_login(name):
    return '<h1>Manual Login</h1>'

