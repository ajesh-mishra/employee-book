from sqlite3 import Cursor, Connection
from typing import Dict, List, Any


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


def query_employee(query_string: str = None, data: Dict[str, Any] = None, create_table: bool = False) -> List:
    """
    Queries employees table and returns a List of employees
    """
    import sqlite3
    conn: Connection = sqlite3.connect('employee.db')
    cursor: Cursor = conn.cursor()

    if create_table:
        cursor.execute('''CREATE TABLE employees (
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
    # data = {'email': 'admin@email.com', 'password': '1234'}
    # users = query_users()
    # print(users)

    """
    Employee Table
    """
    # first: str = 'Rajesh'
    # last: str = 'Mishra'
    # pay: int = 60_000
    #
    # query: str = '''INSERT INTO employees VALUES (:first, :last, :pay)'''
    # data: Dict[str, str | int] = {'first': first, 'last': last, 'pay': pay}
    #
    # employees = query_employee()
    # print(employees)
