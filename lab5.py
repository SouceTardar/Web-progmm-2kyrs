from flask import Blueprint, render_template, request
import psycopg2


lab5 = Blueprint('lab5', __name__)


@lab5.route('/lab5/')
def main():
    #Прописываем параметры подключения к БД
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base",
        user="maxim_knowledge_base",
        password="0811")
    
    #Получаем курсор. С помощью него мы можем выполнять SQL-запросы
    cur = conn.cursor()

    #Пишм запрос, который psycopg2 должен выполнять
    cur.execute("SELECT * FROM users;")

    #fetchall-получить все строчки, сохраняем в переменную
    result= cur.fetchall()

    #Закроем соединения с БД
    cur.close()
    conn.close()

    print(result)

    return render_template('lab5.html')

@lab5.route('/lab5/users')
def users():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base",
        user="maxim_knowledge_base",
        password="0811")
    cur = conn.cursor()
    cur.execute("SELECT username FROM users")
    result = cur.fetchall()
    conn.close()
    return render_template('users.html', users=result)

