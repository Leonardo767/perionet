from flask import render_template, url_for, flash, redirect
from perionet import app

dummyChartData = [['0 0 0', '1 2 1']]*32


@app.route("/")
@app.route("/home")
def home():
    flash('hello', 'success')
    flash('test', 'danger')
    return render_template('home.html')


@app.route("/chart")
def chart():
    return render_template('chart.html', data=dummyChartData)


@app.route("/patient_profile")
def patient_profile():
    return render_template('patient_profile.html')


@app.route("/register_patient")
def register_patient():
    return render_template('register_patient.html')
