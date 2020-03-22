from flask import render_template, url_for, flash, redirect
from perionet import app
from perionet.chartHandle import Patient
from perionet.forms import RegistrationForm, LoginForm

patient_name = 'John Doe'


@app.route("/")
@app.route("/home")
def home():
    flash('hello', 'success')
    flash('test', 'danger')
    return render_template('home.html')


@app.route("/chart")
def chart():
    currentPatient = Patient(patient_name)
    return render_template('chart.html', currentPatient=currentPatient)


@app.route("/patient_profile")
def patient_profile():
    return render_template('patient_profile.html')


@app.route("/register_patient", methods=['GET', 'POST'])
def register_patient():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(
            f'Patient created: {form.nameFirst.data} {form.nameLast.data}', 'success')
        return redirect(url_for('patient_profile'))
    if form.errors:
        flash('Could not register new patient. Please verify that the fields below are filled correctly.', 'danger')
    return render_template('register_patient.html', form=form)


@app.route("/select_patient", methods=['GET', 'POST'])
def select_patient():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(
            f'Patient selected: {form.nameFirst.data} {form.nameLast.data}', 'success')
        return redirect(url_for('patient_profile'))
    return render_template('select_patient.html')
