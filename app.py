
from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
   return """
   <!DOCTYPE html>
<html>
    <head>
        <title>Козицкий Владислав и Штагауэр Максим. Лабораторная 1</title>
    </head>

    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>web-сервер на flask</h1>

        <footer>
            &copy; Козицкий Владислав и Штагауэр Максим, ФБИ-12, 3 курс 2023
        </footer>
    </body>
</html>
"""



