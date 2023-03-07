from flask import Blueprint, render_template, request, flash, redirect, Response
from typing import List, Any, Optional, Dict
from app.db import query_employee

views = Blueprint('view', __name__)


@views.route('/home', methods=['GET', 'POST'])
def home() -> str:
    """
    Home page of the application which lists all the employees
    """
    employees: List[Any] = query_employee()
    print(employees)

    return render_template('home.html', employees=employees)


@views.route('/new-employee', methods=['GET', 'POST'])
def new_employee() -> str | Response:
    """
    Page for adding new Employee
    """
    if request.method == 'POST':
        first: Optional[str] = request.form.get('first')
        last: Optional[str] = request.form.get('last')
        pay: Optional[str] = request.form.get('pay')

        if not first:
            flash('First Name is Mandatory', 'error')
        elif not last:
            flash('Last Name is Mandatory', 'error')
        elif int(pay) < 1_000:
            flash('Pay cannot be less than 1000', 'error')
        else:
            query_string: str = '''INSERT INTO employees VALUES (:first, :last, :pay)'''
            data: Dict = {'first': first, 'last': last, 'pay': pay}
            query_employee(query_string, data)

            flash('Employee Added!', 'success')
            return redirect('/home')

    return render_template('new-employee.html')
