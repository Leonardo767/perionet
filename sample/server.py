from flask import Flask, render_template, url_for, flash, redirect
app = Flask(__name__)

app.config['SECRET_KEY'] = '38d8626329795e446589fb7e670f6797'


@app.route("/")
@app.route("/home")
def home():
    flash('hello', 'success')
    flash('test', 'danger')
    return render_template('home.html')


@app.route("/chart")
def chart():
    return render_template('chart.html')


if __name__ == '__main__':
    app.run(debug=True)
