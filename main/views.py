from flask import (render_template, url_for, redirect, session, request)
from main import app

@app.route('/')
def top():
    return render_template('top.html', type='top', title='Top')

@app.route('/sign_up')
def sign_up():
    return render_template('sign.html', type='sign_up', title='Sign up')

@app.route('/sign_in')
def sign_in():
    return render_template('sign.html', type='sign_in', title='Sign in')