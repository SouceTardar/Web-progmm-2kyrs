from flask import Blueprint, render_template, request
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
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    result= cur.fetchall()
    print(result)

    return render_template('lab5.html')

@lab5.route('/lab5/users')
def users():
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute("SELECT username FROM users")
    result = cur.fetchall()
    conn.close()
    return render_template('users.html', users=result)

