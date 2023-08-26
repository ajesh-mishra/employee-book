from typing import List, Any, Optional, Dict

from flask import Blueprint, render_template, request, flash, redirect
from werkzeug import Response

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


@views.route('/add-update-employee', methods=['GET', 'POST'])
def add_update_employee() -> str | Response:
    """
    HTML Form for Adding a new Employee or Updating an existing Employee.
    """
    emp_id: str | None = request.args.get('id')
    employee = {}

    if emp_id:
        query_string = '''SELECT * FROM employees WHERE id = :id'''
        res = query_employee(query_string, {'id': int(emp_id)})
        res = res[0]

        employee['id'] = res[0]
        employee['first'] = res[1]
        employee['last'] = res[2]
        employee['pay'] = res[3]

    if request.method == 'POST':
        emp_id: Optional[str] = request.form.get('id')
        first: Optional[str] = request.form.get('first')
        last: Optional[str] = request.form.get('last')
        pay: Optional[str] = request.form.get('pay')

        if not first:
            flash('First Name is Mandatory', 'error')
        elif not last:
            flash('Last Name is Mandatory', 'error')
        elif int(pay) < 1_000:
            flash('Pay cannot be less than 1000', 'error')

        if emp_id == 'None':
            query_string: str = '''INSERT INTO employees VALUES (:id, :first, :last, :pay)'''
            data: Dict = {'id': None, 'first': first, 'last': last, 'pay': pay}
            query_employee(query_string, data)
            flash('Employee Added!', 'success')
        elif emp_id:
            query_string: str = '''UPDATE employees SET first = :first, last = :last, pay = :pay WHERE id = :id'''
            query_employee(query_string, {'id': emp_id, 'first': first, 'last': last, 'pay': pay})
            flash('Employee Updated!', 'success')
        else:
            flash('Something went wrong, try again!', 'error')

        return redirect('/home')

    return render_template('add-update-employee.html', employee=employee)


@views.route('/show-employee', methods=['GET'])
def show_employee() -> str:
    """
    Shows more details about a particular employee
    when employee ID is passed as query parameter in the url.
    """
    emp_id: str | None = request.args.get('id')

    if not emp_id:
        redirect('/home')

    query_string = '''SELECT * FROM employees WHERE id = :id'''
    employee = query_employee(query_string, {'id': int(emp_id)})

    return render_template('show.html', employee=employee[0])


@views.route('/delete-employee', methods=['GET'])
def delete_employee() -> Response:
    """
    Deletes an employee from the database
    when employee ID is passed as query parameter in the url.
    """
    emp_id: str | None = request.args.get('id')

    if not emp_id:
        redirect('/home')

    query_string = '''DELETE FROM employees WHERE id = :id'''
    query_employee(query_string, {'id': int(emp_id)})

    flash(f'Employee with emp_id: {emp_id} deleted!', 'success')
    return redirect('/home')
