from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        ninja = request.form['ninja']
        if name and age and ninja:
            return render_template('login.html',name = name, age = age, ninja = ninja)
        else:
            return redirect(url_for('error'))


@app.route('/error', methods=['GET', 'POST'])
def error():
    if request.method == 'POST':
        return redirect(url_for('home_page'))
    return render_template('error.html')


if __name__ == '__main__':
    app.run()
