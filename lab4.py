from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    errors={}
    username = request.form.get('username')
    if username == '':
        errors['username'] = 'не введен логин'

    password = request.form.get('password')
    if password == '':
        errors['password'] = 'не введен пароль'

    if username == 'alex' and password == '123':
        return render_template('successlogin.html', username = username)

    error = 'Неверный логин и/или пароль'
    return render_template('login.html', error = error, username=username, password=password, errors=errors)

@lab4.route('/lab4/fridge', methods = ['GET', 'POST'])
def fridge():


    return render_template('fridge.html')

@lab4.route("/set_temperature", methods=["POST"])
def set_temperature():
    temperature = request.form.get("temperature")
    error = ""
    success = False
    flakes = 0

    if not temperature:
        error = "Ошибка: не задана температура"
    elif int(temperature) < -12:
        error = "Не удалось установить температуру — слишком низкое значение"
    elif int(temperature) > -1:
        error = "Не удалось установить температуру — слишком высокое значение"
    elif -12 <= int(temperature) <= -9:
        success = True
        flakes = 3
    elif -8 <= int(temperature) <= -5:
        success = True
        flakes = 2
    elif -4 <= int(temperature) <= -1:
        success = True
        flakes = 1

    return render_template("fridge.html", error=error, success=success, temperature=temperature, flakes=flakes)

