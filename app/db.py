def query(query_string=None, data=None):
    import sqlite3
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()

    # cursor.execute('''CREATE TABLE users (
    #     email text,
    #     password text
    # )''') 

    if query_string:
        with conn:
            cursor.execute(query_string, data)
    else:
        cursor.execute('''SELECT * FROM users''')
    
    users_fetched = cursor.fetchall()
    conn.close()
    return users_fetched


def employee_db(query_string=None, data=None):
    import sqlite3
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()

    # cursor.execute('''CREATE TABLE employees (
    #     first text,
    #     last text,
    #     pay integer
    # )''')

    # first = 'Rajesh'
    # last = 'Mishra'
    # pay = 60_000

    # with conn:
    #     cursor.execute('''INSERT INTO employees VALUES (:first, :last, :pay)''',
    #         {'first': first, 'last': last, 'pay': pay}
    #     )

    if query_string:
        with conn:
            cursor.execute(query_string, data)
    else:
        cursor.execute('''SELECT * FROM employees''')
        
    employees = cursor.fetchall()
    conn.close()
    return employees


if __name__ == '__main__':
    # users = query('''DELETE from users WHERE email = :email''',
    #            {'email': 'admin@email.com'})
    users = employee_db()
    print(users)
    # import sqlite3
    # conn = sqlite3.connect('employee.db')
    # cursor = conn.cursor()

    # email = 'ajesh@email.com'
    # password = '1234'

    # with conn:
    #     cursor.execute('''INSERT INTO users VALUES (:email, :password)''',
    #         {'email': email, 'password': password})

    # with conn:
    #     cursor.execute('''DELETE from employees WHERE email = :email''',
    #           {'email': email})
        
    # cursor.execute('''SELECT * FROM users''')

    # print(cursor.fetchall())
    # conn.close()
