from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
   return redirect("/menu", code = 302)

@app.route("/menu")
def menu():
   return """
      <!DOCTYPE html>
      <html>
      <link rel="stylesheet" href="static/lab1.css">
         <head>
            <title>Козицкий Владислав и Штагауэр Максим. Лабораторные работы</title>
         </head>

         <body style="margin-left: 5%; padding: 50px;">
            <header>
               <h1>НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных</h1> web-сервер на flask
            </header>
            <h2><a href="/lab1">Лабораторная 1</a></h2>

            <footer>
                  &copy; Козицкий Владислав и Штагауэр Максим, ФБИ-12, 3 курс 2023
            </footer>
         </body>
      </html>
"""

@app.route("/lab1")
def lab1():
   return """
      <!DOCTYPE html>
      <html>
      <link rel="stylesheet" href="static/lab1.css">
         <head>
            <title>Козицкий Владислав и Штагауэр Максим. Лабораторная работа 1</title>
         </head>

         <body style="margin-left: 5%; padding: 50px;">
            <header>
                  НГТУ, ФБ, Лабораторная работа 1
            </header>
            <a href="/menu">Меню</a>
            <div style="margin-left: 2%; padding: 15px;">
                  Flask — фреймворк для создания веб-приложений на языке
                  программирования Python, использующий набор инструментов
                  Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                  называемых микрофреймворков — минималистичных каркасов
                  веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
                  Проверьте: обрабаты
            </div>
            <div style="margin-left: 5%; padding: 20px;">
               <div style="margin-left: -20px; padding: -10px;">
                  <b>Работа:</b>
               </div>
               <p>
                  <a href="/lab1/oak">/lab1/oak - Дуб</a>
               </p>
               <p>
                  <a href="/lab1/student">/lab1/student - Студент</a>
               </p>
               <p>
                  <a href="/lab1/python">/lab1/python - Питон</a>
               </p>
            </div>
            <footer>
                  &copy; Козицкий Владислав и Штагауэр Максим, ФБИ-12, 3 курс 2023
            </footer>
         </body>
      </html>
"""

@app.route('/lab1/oak')
def oak():
   return '''
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="static/lab1.css">
   <head>
      <title>Козицкий Владислав и Штагауэр Максим. Лабораторные работы</title>
   </head>
   <a href="/lab1">Назад</a>
   <p></p>
   <a href="/menu">Меню</a>
   <body style="margin-left: 5%; padding: 50px;">
      <h1>Мудрый Дуб</h1>
      <img src="''' + url_for('static', filename='oak.jpg') + '''">
   </body>
</html>
   '''

@app.route('/lab1/student') 
def student():
   return '''
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="static/lab1.css">
   <head>
      <title>Козицкий Владислав и Штагауэр Максим. Лабораторные работы</title>
   </head>
   <a href="/lab1">Назад</a>
   <p></p>
   <a href="/menu">Меню</a>
   
   <body style="margin-left: 5%; padding: 50px;">
      <h1>Козицкий Владислав Сергеевич</h1>
      <h1>Штангауэр Максим Максимович</h1>
      <img style="height: 250px; width: 250px;" src="''' + url_for('static', filename='NSTU.jpeg') + '''">
   </body>
</html>
   '''

@app.route('/lab1/python') 
def python():
   return '''
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="static/lab1.css">
   <head>
      <title>Козицкий Владислав и Штагауэр Максим. Лабораторные работы</title>
   </head>
   <a href="/lab1">Назад</a>
   <p></p>
   <a href="/menu">Меню</a>
   
   <body style="margin-left: 5%; padding: 50px;">
      <h1>Python - это   </h1>
      <h3>Высокоуровневый язык программирования общего назначения с динамической строгой типизацией 
      и автоматическим управлением памятью, ориентированный на повышение производительности 
      разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных
      на нём программ.</h3>
      <img style="height: 250px; width: 250px;" src="''' + url_for('static', filename='PYTHON.png') + '''">
   </body>
</html>
   '''