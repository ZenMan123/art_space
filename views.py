from main import app
from flask import render_template


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/register')
def register():
    return 'Register page'


@app.route('/login')
def login():
    return 'Login page'
