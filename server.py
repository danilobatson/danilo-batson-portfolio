'''This is the main entry point for the web server.'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    '''Renders home page.'''
    return render_template("index.html")
