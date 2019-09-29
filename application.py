# import os
# import smtplib
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

#Registered students
students = []

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/registrants")
# def registrants():
#     return render_template("registered.html", students = students)

#listen for '/register'
@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("branch") or not request.form.get("email"):
        return "failure"
    file = open("registered.csv", "a") # a for append mode
    writer = csv.writer(file)
    writer.writerow((request.form.get("name"), request.form.get("branch"))) #extra braces for tuple
    file.close()
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