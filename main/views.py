from flask import render_template, url_for, redirect, session, request, Response
from main import app
from main import key
from main import db
from main.models import User, Post
from hashlib import sha256

# Top page listing up user's blogs
@app.route('/')
def top(status=None, post_title=None):
    posts = Post.query.all()
    status = request.args.get('status')
    post_title = request.args.get('post_title')
    # If not signed in, transfers to a sign-in page
    if 'user_name' in session:
        user = User.query.filter_by(name=session['user_name']).first()
        return render_template('top.html', type='top', title='Top', session=session, user=user, status=status, post_title=post_title)
    else:
        return redirect(url_for('sign_in'))

# Sign in page, and deals with sign in request
@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    status = request.args.get('status')
    # Deals with User's request to sign in
    if request.method == 'POST':
        # Tries to pull date of user instance based of actual user input
        user_name = request.form['user_name']
        user = User.query.filter_by(name=user_name).first()
        if user:
            password = request.form['password']
            hashed_password = sha256((user_name + password + key.SALT).encode('utf-8')).hexdigest()
            if user.hashed_password == hashed_password:
                session['user_name'] = user_name
                return redirect(url_for('top', status='sign'))
            else:
                return render_template('sign.html', type='sign_in', title='Sign in', error='Password is wrong.')
        else:
            return render_template('sign.html', type='sign_in', title='Sign in', error='User doesn\'t exist.')
    # If signed in already, transfers to a top page
    if 'user_name' in session:
        return redirect(url_for('top'))
    # Output HTML form
    return render_template('sign.html', type='sign_in', title='Sign in', error='', status=status)
        

# Sign up page, and deals with a request to sign up
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    # Deals with User's request to sign up
    if request.method == 'POST':
        user_name = request.form['user_name']
        if not user_name:
            return render_template('sign.html', type='sign_up', title='Sign up', error='User name is missed.')
        user = User.query.filter_by(name=user_name).first()
        if user:
            return render_template('sign.html', type='sign_up', title='Sign up', error='User name already exists.')
        else:
            password = request.form['password']
            if not password:
                return render_template('sign.html', type='sign_up', title='Sign up', error='Password is missed.')
            hashed_password = sha256((user_name + password + key.SALT).encode('utf-8')).hexdigest()
            user = User(user_name, hashed_password)
            db.session.add(user)
            db.session.commit()
            session['user_name'] = user_name
            return redirect(url_for('top', status='sign'))
    # If signed in already, transfers to a top page
    if 'user_name' in session:
        return redirect(url_for('top'))
    # Output HTML form
    return render_template('sign.html', type='sign_up', title='Sign up', error='')

# Execute sign out
@app.route('/sign_out')
def sign_out():
    session.clear()
    return redirect(url_for('sign_in', status='sign_out'))

# Page where user upload a post, and deals with the request
@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    user = User.query.filter_by(name=session['user_name']).first()
    # Deals with User's a request to upload a post
    if request.method == 'POST':
        user_id = user.id
        title = request.form['title']
        if not title:
            return render_template('posting.html', type='add_post', title='Add post', error='Title is missed')
        detail = request.form['detail']
        if not detail:
            return render_template('posting.html', type='add_post', title='Add post', error='Detail is missed')
        post = Post(user_id, title, detail)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('top', status='add', post_title=post.title))
    # Output HTML form
    return render_template('posting.html', type='add_post', title='Add post', user=user)

# Update info of a post instance
@app.route('/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    # Tries to pull date of user and post instances based of actual user input
    user = User.query.filter_by(name=session['user_name']).first()
    post = Post.query.filter_by(id=id).first()
    # Deals with User's a request to update a post
    if request.method == 'POST':
        title = request.form['title']
        detail = request.form['detail']
        if not title:
            return render_template('posting.html', type='add_post', title='Add post', error='Title is missed')
        if not detail:
            return render_template('posting.html', type='add_post', title='Add post', error='Detail is missed')
        post.title = title
        post.detail = detail
        db.session.commit()
        return redirect(url_for('top', status='update', post_title=post.title))
    # Output HTML form
    return render_template('posting.html', type='update', title='Update post', user=user, post=post)

# Deletes a post instance from database
@app.route('/<int:id>/delete')
def delete(id):
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('top', status='delete', post_title=post.title))