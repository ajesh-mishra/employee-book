from sqlite3 import Cursor, Connection
from typing import Dict, List, Any, Tuple


def query_users(query_string: str = None, data: Dict[str, Any] = None, create_table: bool = False) -> List:
    """
    Queries users table and returns a List of users
    """
    import sqlite3
    conn: Connection = sqlite3.connect('employee.db')
    cursor: Cursor = conn.cursor()

    if create_table:
        cursor.execute('''CREATE TABLE users (
            email text,
            password text
        )''')

    if query_string:
        with conn:
            cursor.execute(query_string, data)
    else:
        cursor.execute('''SELECT * FROM users''')

    users_fetched: List[Any] = cursor.fetchall()
    conn.close()
    return users_fetched


def query_employee(query_string: str = None, data: Tuple | Dict = None, create_table: bool = False) -> List:
    """
    Queries employees table and returns a List of employees
    """
    import sqlite3
    conn: Connection = sqlite3.connect('employee.db')
    cursor: Cursor = conn.cursor()

    if create_table:
        cursor.execute('''CREATE TABLE employees (
            id integer PRIMARY KEY,
            first text,
            last text,
            pay integer
        )''')

    if query_string:
        with conn:
            cursor.execute(query_string, data)
    else:
        cursor.execute('''SELECT * FROM employees''')

    employees: List[Any] = cursor.fetchall()
    conn.close()
    return employees


if __name__ == '__main__':
    """
    User Table
    """
    # query = '''INSERT INTO users VALUES (:email, :password)'''
    # data = {'email': 'ajesh@email.com', 'password': '1234'}
    # users = query_users()
    # print(users)

    """
    Employee Table
    """
    # query: str = '''INSERT INTO employees(first, last, pay) VALUES (?, ?, ?)'''
    # data: Tuple[str, str, int] = ('Ajesh', 'Mishra', 50_000)

    # query: str = '''INSERT INTO employees VALUES (:id, :first, :last, :pay)'''
    # data: Dict[str, int | str] = {'id': None, 'first': 'Sam', 'last': 'Smith', 'pay': 50_000}

    query: str = '''UPDATE employees SET first = :first, last = :last, pay = :pay WHERE id = :id'''
    data: Dict[str, int | str] = {'id': 5, 'first': 'Sam', 'last': 'Smith', 'pay': 51_000}

    # emp_id = 3
    # query_string = '''SELECT * FROM employees WHERE id = :id'''
    # employee = query_employee(query_string, {'id': int(emp_id)})

    employees = query_employee()
    print(employees)
