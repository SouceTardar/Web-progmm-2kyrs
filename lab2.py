from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route('/lab2/') 
def lab():
   return render_template('lab2.html')


@lab2.route('/lab2/example') 
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


@lab2.route('/lab2/info') 
def info():
   return render_template('lab2INFO.html')