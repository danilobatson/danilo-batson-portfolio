'''This is the main entry point for the web server.'''
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home_page():
    '''Renders home page.'''
    return render_template("index.html")

@app.route("/submit_form", methods=["GET", "POST"])
def submit_form():
    '''Submits contact form.'''
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return 'form submitted successfully'
    else:
        return 'something went wrong'
