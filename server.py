'''This is the main entry point for the web server.'''
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home_page():
    '''Renders home page.'''
    return render_template("index.html")
@app.route("/thankyou.html")
def thank_you():
    '''Renders thank you page.'''
    return render_template("thank_you.html")

@app.route("/submit_form", methods=["GET", "POST"])
def submit_form():
    '''Submits contact form.'''
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return redirect("/thankyou.html")
    else:
        return 'something went wrong'
