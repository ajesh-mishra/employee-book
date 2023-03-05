from flask import Blueprint, render_template, request, redirect, flash
from app.db import query
import re

auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        users = query('''SELECT * FROM users WHERE email = :email''', {'email': email})

        if len(users) != 1:
            flash('Incorrect Email', 'error')
        elif users[0][1] != password:
            flash('Incorrect Password', 'error')
        else:
            flash(f'Welcome {email}', 'success')
            return redirect('/home')
    
    return render_template('login.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        pattern = re.compile(r'^\w+[-.]?\w+@\w+\.\w+$')
        matches = pattern.findall(email)
        
        if not matches:
            flash('Invalid Email ID', 'error')
        elif len(password1) < 4:
            flash('Password Should be atleast 4 chars long', 'error')
        elif password1 != password2:
            flash('Passwords don\'t match', 'error')
        else:
            query_string='''INSERT INTO users VALUES (:email, :password)'''
            data={'email': email, 'password': password1}
            query(query_string, data)

            flash('Account Created!', 'success')
            return redirect('/')

    return render_template('sign-up.html')
