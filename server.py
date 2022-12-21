'''This is the main entry point for the web server.'''
from flask import Flask, render_template, request, redirect
import csv 

app = Flask(__name__)

@app.route("/")
def home_page():
    '''Renders home page.'''
    return render_template("index.html")

@app.route("/thankyou.html")
def thank_you():
    '''Renders thank you page.'''
    return render_template("thank_you.html")

def write_to_file(data):
    '''Writes data to a file.'''
    with open("database.txt", mode="a") as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{name}, {email}, {subject}, {message}")
        
def write_to_csv(data):
    '''Writes data to a csv file.'''
    with open("database.csv", mode="a", newline='') as database2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])

@app.route("/submit_form", methods=["GET", "POST"])
def submit_form():
    '''Submits contact form.'''
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html" )
        except: 
            return 'did not save to database'
    else:
        return 'something went wrong'
