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

@lab4.route('/lab4/zerno')
def zerno():
    return render_template('order_grain.html')

@lab4.route('/process_order', methods=['POST'])
def process_order():
    grain_type = request.form['grainType']
    weight = float(request.form['weight'])

    number = 0

    if not weight:
        return "Ошибка: не введён вес. <a href='/'>Вернуться к заказу</a>"

    if weight <= 0:
        return "Ошибка: неверное значение веса. <a href='/'>Вернуться к заказу</a>"

    price_per_ton = 0
    if grain_type == 'ячмень':
        price_per_ton = 12000
    elif grain_type == 'овёс':
        price_per_ton = 8500
    elif grain_type == 'пшеница':
        price_per_ton = 8700
    elif grain_type == 'рожь':
        price_per_ton = 14000

    if weight > 500:
        return "Ошибка: такого объёма сейчас нет в наличии. <a href='/lab4/zerno'>Вернуться к заказу</a>"
    elif weight > 50:
        total_price = weight * price_per_ton * 0.9
        message = f"Заказ успешно сформирован. Вы заказали зерно: {grain_type}. Вес: {weight} т. Сумма к оплате: {total_price} руб. (Применена скидка за большой объём)"
    else:
        total_price = weight * price_per_ton
        message = f"Заказ успешно сформирован. Вы заказали зерно: {grain_type}. Вес: {weight} т. Сумма к оплате: {total_price} руб."

    return f"<h3>{message}</h3><br><a href='/lab4/zerno'>Вернуться к заказу</a>"

@lab4.route('/lab4/cookies', methods = ['GET', 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html' )
    
    color = request.form.get('color')
    bgcolor = request.form.get('bgcolor')
    fontsize = request.form.get('fontsize')
    headers = {
        'Set-Cookies': 'color=' + color + '; path=/',
        'Set-Cookies': 'bgcolor=' + bgcolor + '; path=/',
        'Set-Cookies': 'fontsize=' + fontsize + '; path=/',
        'Location': '/lab4/cookies'
    }
    return '', 303, headers