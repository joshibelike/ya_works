from flask import Flask, render_template_string, request, url_for
import os

# при тесте перейдите на http://127.0.0.1:5000/load_photo

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    photo_url = None

    if request.method == 'POST':
        if 'photo' in request.files:
            file = request.files['photo']
            if file.filename != '':
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)
                photo_url = url_for('static', filename=f'uploads/{file.filename}')

    return render_template_string(HTML_TEMPLATE, photo_url=photo_url)


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Отбор астронавтов</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container mt-4">
        <h1 class="text-center mb-4">Загрузка фотографии</h1>
        <h3 class="text-center mb-4">для участия в миссии</h3>

        <div class="card mx-auto" style="max-width: 600px; background-color: #ffe4c4;">
            <div class="card-body">
                <form method="POST" enctype="multipart/form-data">
                    <div class="mb-3">
                        <label for="photoInput" class="form-label">Приложите фотографию</label>
                        <input class="form-control" type="file" name="photo" id="photoInput">
                    </div>

                    {% if photo_url %}
                    <div class="text-center mb-3">
                        <img src="{{ photo_url }}" class="img-fluid" alt="Фото" style="max-height: 400px;">
                    </div>
                    {% else %}
                    <div class="text-center mb-3">
                        <img src="{{ url_for('static', filename='img/robot.jpg') }}" class="img-fluid" alt="Робот" style="max-height: 400px;">
                    </div>
                    {% endif %}

                    <button type="submit" class="btn btn-primary">Отправить</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
