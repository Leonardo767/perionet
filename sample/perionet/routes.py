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
    return render_template('chart.html')
