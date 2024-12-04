from flask import Flask, render_template, abort
import os

CultInfo = Flask(__name__)

# Путь к папке с текстовыми файлами
BASE_DIR = os.path.join(os.getcwd(), "content")

# Категории и подкатегории
categories = {
    "Музыка": ["Людвиг ван Бетховен", "Иоганн Себастьян Бах", "Фредерик Шопен", "Антонин Дворжак", "Густав Малер", "Клод Дебюсси", "Вольфган Амадей Моцарт", "Петр Ильич Чайковский", "Сергей Прокофьев", "Дмитрий Шостакович", "Жан Себастьян Бах", "Ферруччо Бузони", "Георг Фридрих Гендель", "Игорь Стравинский", "Стив Райх", "Джон Кейдж", "Арнольд Шёнберг", "Камий Сен-Санс", "Аарон Копленд", "Анна Семенова", "Эдвард Григ"],
    "Живопись": ["Микеланджело Меризи да Караваджо", "Пабло Пикассо", "Леонардо да Винчи", "Жан-Батист-Симеон Шарден", "Эпоха Возрождения", "Жан Антуан Ватто", "Сальвадор Дали", "Йозеф Бойс", "Жорж Брак", "Клод Моне", "Микеланджело Буонарроти", "Рембрандт Харменс ван Рейн", "Винсент Ван Гог", "Эдвард Мунк", "Гюстав Курбе", "Кацусики Хокусай"],
    "Литература": ["Уильям Шекспир", "Джон Китс", "Лев Николаевич Толстой", "Федор Михайлович Достоевский", "Вирджиния Вулф", "Эрнест Хемингуэй", "Константин Симонов", "Филипп Сольер", "Блез Сен-Лорен", "Франц Кафка", "Андре Бретон", "Марк Твен", "Генрих Гейне", "Братья Гримм", "Джеймс Джойс", "Сильвия Плат", "Гомер", "Бернард Шоу", "Сэмюэл Джонсон", "Чарльз Диккенс", "Эмили Дикинсон", "Рэй Брэдберри", "Габриэль Гарсиа Маркес", "Герман Мелвил", "Виктор Гюго", "Людвиг Витгенштейн"]
}

@CultInfo.route("/")
def index():
    return render_template("index.html", categories=categories)

# Маршрут для отображения подкатегории
@CultInfo.route("/category/<category>/<subcategory>")
def subcategory_detail(category, subcategory):
    # Проверяем, что категория и подкатегория существуют
    if category in categories and subcategory in categories[category]:
        # Формируем путь к файлу
        file_path = os.path.join(BASE_DIR, category, f"{subcategory}.txt")
        # Проверяем существование файла и читаем содержимое
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                # Разделяем текст по маркеру абзацев ###
                paragraphs = content.split('###')
            return render_template("subcategory.html", category=category, subcategory=subcategory, paragraphs=paragraphs)
    abort(404)  # Возвращает 404 ошибку, если файл или категория не найдены


if __name__ == "__main__":
    CultInfo.run(debug=True)











