from flask import render_template, flash, redirect, url_for, request,session
from app import app
import json


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html",)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
