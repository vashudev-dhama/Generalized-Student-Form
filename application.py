import os
import smtplib
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

#Registered students
students = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("branch") or not request.form.get("email"):
        return render_template("failure.html")
    #write in csv file
    file = open("registered.csv", "a") # a for append mode
    writer = csv.writer(file)
    writer.writerow((request.form.get("name"), request.form.get("branch"), request.form.get("email"))) #extra braces for tuple
    file.close()
    #send confirmation mail
    email_msg = f"Hello {request.form.get('name')}, your response has been recorded. We're working on your payment issues and hope to resolve ASAP. Till then just have some patience and keep doing your good work."
    server = smtplib.SMTP("smtp.gmail.com", 587) #server to be used for mailing
    server.starttls() #encryption
    server.login("vashudev.1613121@kiet.edu", "itsforkietidOk?") #sender's credentials
    server.sendmail("vashudev.1613121@kiet.edu", request.form.get("email"), email_msg) #from-to with msg
    return render_template("success.html", name = request.form.get("name"))

@app.route("/registered")
def registered():
    file = open("registered.csv", "r")
    reader = csv.reader(file)
    students = list(reader)
    file.close()
    '''Below code will handle the opening and closing of file itself--
    with open("registered.csv", "r") as file:
        reader = csv.reader(file)
        students = list(reader)'''
    return render_template("registered.html", students = students)