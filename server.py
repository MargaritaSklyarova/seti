from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML-код вашей страницы
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Моя первая страница</title>
    <style>
        /* Устанавливаем фон с картинкой */
        body {
            background-image: url('https://avatars.mds.yandex.net/i?id=679720f2a94327342bb6a0e160ce7bb8_l-8497208-images-thumbs&n=13'); /* Замените на путь к вашей картинке */
            background-size: cover; /* Картинка растягивается на весь экран */
            background-position: center;
            font-family: Arial, sans-serif; /* Шрифт */
            color: white; /* Белый текст */
            margin: 0;
            padding: 0;
            height: 100vh; /* Чтобы фон занимал всю высоту экрана */
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        /* Стиль для заголовка */
        h1 {
            font-size: 3em;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7); /* Тень для заголовка */
        }

        /* Стиль для параграфа */
        p {
            font-size: 1.2em;
            line-height: 1.5;
        }

        /* Стиль для кнопки */
        .btn {
            padding: 10px 20px;
            font-size: 1.2em;
            background-color: #ff4500;
            border: none;
            color: white;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        .btn:hover {
            background-color: #ff6347; /* Цвет кнопки при наведении */
        }
    </style>
</head>
<body>
    <div>
        <h1>Добро пожаловать на страницу!</h1>
        <p>Рада всех видеть.</p>
        <button class="btn">Нажми на меня</button>
    </div>
</body>
</html>

"""

@app.route('/')
def home():
    # Рендерим HTML-страницу
    return render_template_string(html_content)

if __name__ == '__main__':
    # Указываем хост и порт
    port = int(os.environ.get('PORT', 5000))  # Используем порт из переменной окружения или 5000 по умолчанию
    app.run(host='0.0.0.0', port=port, debug=True)
