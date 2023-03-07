from flask import Blueprint, render_template, request, redirect, flash, Response
from typing import Optional, List, Any, Pattern, Dict
from app.db import query_users
import re

auth: Blueprint = Blueprint('auth', __name__)


@auth.route('/', methods=['GET', 'POST'])
def login() -> str | Response:
    """
    Login Page for the application
    """
    if request.method == 'POST':
        email: Optional[str] = request.form.get('email')
        password: Optional[str] = request.form.get('password')
        users: List[Any] = query_users('''SELECT * FROM users WHERE email = :email''', {'email': email})

        if len(users) < 1:
            flash('Incorrect Email', 'error')
        elif users[0][1] != password:
            flash('Incorrect Password', 'error')
        else:
            flash(f'Welcome {email}', 'success')
            return redirect('/home')
    
    return render_template('login.html')


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up() -> str | Response:
    """
    Sign-up Page for the application
    """
    if request.method == 'POST':
        email: Optional[str] = request.form.get('email')
        password1: Optional[str] = request.form.get('password1')
        password2: Optional[str] = request.form.get('password2')

        pattern: Pattern[str] = re.compile(r'^\w+[-.]?\w+@\w+\.\w+$')
        matches: List[Any] = pattern.findall(email)
        
        if not matches:
            flash('Invalid Email ID', 'error')
        elif len(password1) < 4:
            flash('Password Should be at least 4 chars long', 'error')
        elif password1 != password2:
            flash('Passwords don\'t match', 'error')
        else:
            query_string: str = '''INSERT INTO users VALUES (:email, :password)'''
            data: Dict = {'email': email, 'password': password1}
            query_users(query_string, data)

            flash('Account Created!', 'success')
            return redirect('/')

    return render_template('sign-up.html')
