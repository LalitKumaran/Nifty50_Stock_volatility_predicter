#import base64
#import datetime
#from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
#from dateutil import parser
from . import db
from .model import User, Stock
#import datetime
#import matplotlib.pyplot as plt

views = Blueprint('views', __name__)

curuser = 0

@views.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')
        from .model import User
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                flash('Logged in')
                global curuser
                curuser = user
                #return redirect(url_for('views.dashboard'))
                return render_template("dashboard.html", user=curuser)
            else:
                flash('Incorrect password')
        else:
            flash('User does not exist.')
    return render_template("login.html", user=curuser)

@views.route('/logout',methods=['GET','POST'])
def logout():
    global curuser
    curuser = 0
    flash('Logged out successfully.')
    return redirect(url_for('views.login'))

@views.route('/signup',methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        from .model import User
        user = User.query.filter_by(email=email).first()
        if user:
            flash('An account has already been created with this email.')
        elif password1 != password2:
            flash('Passwords don\'t match.')
        else:
            from . import db
            new_user = User(fname=fname, lname=lname, email=email,  phone=phone, password=password1)
            db.session.add(new_user)
            db.session.commit()
            flash('Successfully signed up.')
            return redirect(url_for('views.login'))

    return render_template("signup.html", user=curuser)

@views.route('/', methods=['GET', 'POST'])
def dashboard():
    if curuser != 0:
        return render_template("dashboard.html", user=curuser)
    else:
        return redirect(url_for('views.login'))

@views.route('/profile', methods=['GET', 'POST'])
def profile():
    if curuser != 0:
        return render_template("profile.html", user=curuser)
    else:
        return redirect(url_for('views.login'))