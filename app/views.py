from flask import Blueprint, render_template, request, flash, redirect
from app.db import employee_db

views = Blueprint('view', __name__)

@views.route('/home', methods=['GET', 'POST'])
def home():
    # return '<h1>Views Page<h1>'
    employees = employee_db()
    print(employees)

    return render_template('home.html', employees=employees)


@views.route('/new-employee', methods=['GET', 'POST'])
def new_employee():
    if request.method == 'POST':
        first = request.form.get('first')
        last = request.form.get('last')
        pay = request.form.get('pay')

        if not first:
            flash('First Name is Mandatory', 'error')
        elif not last:
            flash('Last Name is Mandatory', 'error')
        elif int(pay) < 1_000:
            flash('Pay cannot be less than 1000', 'error')
        else:
            query_string='''INSERT INTO employees VALUES (:first, :last, :pay)'''
            data={'first': first, 'last': last, 'pay': pay}
            employee_db(query_string, data)

            flash('Employee Added!', 'success')
            return redirect('/home')

    return render_template('new-employee.html')