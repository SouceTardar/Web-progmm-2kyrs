from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Напишите имя!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле'

    sex = request.args.get('sex')
    return render_template('form1.html', user = user, age = age, sex = sex, errors = errors)

@lab3.route('/lab3/order')
def order():
    return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffe':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('pay.html', price = price)

@lab3.route('/lab3/success')
def success():
    return render_template('success.html')


@lab3.route('/lab3/bilet')
def bilet():
    errors2={}
    fio = request.args.get("fio")
    if fio == '':
        errors2['fio'] = 'Пожалуйста, заполните все поля!'
    type = request.args.get("type")
    if type == '':
        errors2['type'] = 'Пожалуйста, заполните все поля!'
    seat = request.args.get("seat")
    if seat == '':
        errors2['seat'] = 'Пожалуйста, заполните все поля!'
    luggage = request.args.get("luggage")
    if luggage == '':
        errors2['luggage'] = 'Пожалуйста, заполните все поля!'
    age = request.args.get("age")
    if age == '':
        errors2['age'] = 'Пожалуйста, заполните все поля!'
    departure = request.args.get("departure")
    if departure == '':
        errors2['departure'] = 'Пожалуйста, заполните все поля!'
    destination = request.args.get("destination")
    if destination == '':
        errors2['destination'] = 'Пожалуйста, заполните все поля!'
    date = request.args.get("date")
    if date == '':
        errors2['date'] = 'Пожалуйста, заполните все поля!'
    return render_template('bilet.html', fio=fio, type=type, seat=seat, luggage=luggage, age=age, departure=departure, destination=destination, date=date, errors2=errors2)


@lab3.route('/lab3/ticket')
def ticket():
    fio = request.args.get("fio")
    type = request.args.get("type")
    seat = request.args.get("seat")
    luggage = request.args.get("luggage")
    age = request.args.get("age")
    departure = request.args.get("departure")
    destination = request.args.get("destination")
    date = request.args.get("date")
    return render_template('ticket.html', fio=fio, type=type, seat=seat, luggage=luggage, age=age, departure=departure, destination=destination, date=date)
