from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Галерея лис</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center mb-4">Галерея лис</h1>

        <div id="foxCarousel" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-indicators">
                <button type="button" data-bs-target="#foxCarousel" data-bs-slide-to="0" class="active"></button>
                <button type="button" data-bs-target="#foxCarousel" data-bs-slide-to="1"></button>
                <button type="button" data-bs-target="#foxCarousel" data-bs-slide-to="2"></button>
                <button type="button" data-bs-target="#foxCarousel" data-bs-slide-to="3"></button>
            </div>

            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="{{ url_for('static', filename='img/fox1.jpg') }}" class="d-block w-100" alt="Лиса 1">
                </div>
                <div class="carousel-item">
                    <img src="{{ url_for('static', filename='img/fox2.jpg') }}" class="d-block w-100" alt="Лиса 2">
                </div>
                <div class="carousel-item">
                    <img src="{{ url_for('static', filename='img/fox3.jpg') }}" class="d-block w-100" alt="Лиса 3">
                </div>
                <div class="carousel-item">
                    <img src="{{ url_for('static', filename='img/fox4.jpg') }}" class="d-block w-100" alt="Лиса 4">
                </div>
            </div>

            <button class="carousel-control-prev" type="button" data-bs-target="#foxCarousel" data-bs-slide="prev">
                <span class="carousel-control-prev-icon"></span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#foxCarousel" data-bs-slide="next">
                <span class="carousel-control-next-icon"></span>
            </button>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)


if __name__ == '__main__':
    app.run(debug=True)