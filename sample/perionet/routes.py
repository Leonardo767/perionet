from flask import render_template, url_for, flash, redirect
from perionet import app


@app.route("/")
@app.route("/home")
def home():
    flash('hello', 'success')
    flash('test', 'danger')
    return render_template('home.html')


@app.route("/chart")
def chart():
    tooth_group = [0]*4
    return render_template('chart.html', teeth=tooth_group)


@app.route("/patient_profile")
def patient_profile():
    return render_template('patient_profile.html')


@app.route("/register_patient")
def register_patient():
    return render_template('register_patient.html')
