from flask import Flask, redirect, url_for, render_template
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
            <h2><a href="/lab2/example">Лабораторная 2</a></h2>
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

@app.route('/lab2/example') 
def example():
   name = 'Козицкий Владислав и Штагауэр Максим'
   nomerLab = '2'
   grupa = 'ФБИ-12'
   kyrs = '3 курс'
   fruits = [
      {'name': 'яблоки', 'price': 100},
      {'name': 'груши', 'price': 115},
      {'name': 'апельсины', 'price': 95},
      {'name': 'мандарины', 'price': 80},
      {'name': 'манго', 'price': 310},
   ]
   books = [
      {'name': 'Человек-бензопила.', 'autor': 'Тацуки Фудзимото','page': 384, 'Genre': 'Трагедия, Сёнэн, Боевик, Триллер, Комедия, Демоны и Драма', 'price': 613},

      {'name': 'Восхождение Героя Щита.', 'autor': 'Кю Айя и Юсаги Анэко','page': 166, 'Genre': 'Приключения, Романтика, Фэнтези, Исекай, Драма, Сэйнэн и Боевик', 'price': 505},

      {'name': 'Нелюдь.', 'autor': 'Гамон Сакураи и Цуйна Миура','page': 230, 'Genre': 'Приключения, Ужасы, Сэйнэн, Боевик, Драма, Мистика, Трагедия и Научная фантастика', 'price': 500},

      {'name': 'Тетрадь Смерти.', 'autor': 'Цугуми Ооба и Такэси Обата','page': 392, 'Genre': 'Мистика, Приключения, Фэнтези и Ужасы', 'price': 1035},

      {'name': 'Стальной Алхимик.', 'autor': 'Хирому Аракава','page': 280, 'Genre': 'Боевик, Драма, Приключения, Сёнэн и Фэнтези', 'price': 1095},

      {'name': 'Староста-горничная.', 'autor': 'Хиро Фудзивара','page': 192, 'Genre': 'Комедия, Романтика и Интрига', 'price': 350},

      {'name': 'One-Punch Man.', 'autor': 'ONE и Юскэ Мурата','page': 400, 'Genre': 'Боевик, Боевые искусства, Комедия, Сэйнэн, Сверхъестественное и Пародия', 'price': 840},

      {'name': 'Торадора!.', 'autor': 'Дзэккё, Ясу (Takemiya Yuyuko и Zekkyo)','page': 184, 'Genre': 'Драма, Комедия, Повседневность и Романтика', 'price': 350},

      {'name': 'Моя история.', 'autor': 'Кадзунэ Кавахара','page': 180, 'Genre': 'Комедия, Романтика, Сёдзе', 'price': 380},

      {'name': 'Я - Сакамото, а что?.', 'autor': 'Нами Сано','page': 178, 'Genre': 'Комедия, Школа и Сэйнэн', 'price': 505},
   ]
   return render_template('example.html', 
                          name=name, nomerLab=nomerLab, grupa=grupa, kyrs=kyrs,
                          fruits=fruits, books=books)