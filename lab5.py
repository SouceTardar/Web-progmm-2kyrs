from flask import Blueprint, render_template, request, Blueprint, redirect
import psycopg2


lab5 = Blueprint('lab5', __name__)


def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base",
        user="maxim_knowledge_base",
        password="0811")
    return conn;

def dbClose(surcor, connection):
    cur = dbConnect()
    connection.close()

@lab5.route('/lab5/')
def main():  
    visibleUser = 'Anon'
    return render_template('lab5.html', username=visibleUser)

@lab5.route('/lab5/users')
def users():
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute("SELECT username FROM users")
    result = cur.fetchall()
    conn.close()
    return render_template('users.html', users=result)

@lab5.route('/lab5/register', methods = ['GET', 'POST'])
def regPage():
    errors = ""

    if request.method == "GET":
        return render_template('register.html', errors=errors)

    username = request.form.get('username')
    password = request.form.get('password')
   
    if not (username or password):
        errors = "Пожалуйтса, заполните все поля"
        print(errors)
        return render_template("register.html", errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    if cur.fetchone() is not None:
        errors = "Пользователь с данным именем уже существует"
        dbConnect(cur, conn)
        return render_template('register.html', errors=errors)
    
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}');")

    conn.commit()
    dbClose(cur, conn)

    return redirect('/lab5/register')

@lab5.route('/lab5/login', methods = ['GET', 'POST'])
def logPage():
    return render_template('lab5login.html')