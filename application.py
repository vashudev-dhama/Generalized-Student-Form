import os
import smtplib
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#Registered students
students = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrants")
def registrants():
    return render_template("registered.html", students = students)

#listen for '/register'
@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name") #coming via POST not GET
    email = request.form.get("email")
    branch = request.form.get("branch")
    if not name or not branch or not email:
        return "failure"
    students.append(f"{name} from {branch}") #formatted string appended
    message = f"Hello {name}, thanks for the registration"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("vashudev.1613121@kiet.edu", "itsforkietidOk?")
    server.sendmail("vashudev.1613121@kiet.edu", email, message)
    return render_template("success.html", name = name) 
    #return redirect("/registrants")