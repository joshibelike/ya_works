from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    title = "Колонизация Марса"
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    prof_lower = prof.lower()
    if 'инженер' in prof_lower or 'строитель' in prof_lower:
        title = "Инженерные тренажеры"
        image = "engineering.webp"
    else:
        title = "Научные симуляторы"
        image = "scientific.jpg"

    return render_template('training.html', title=title, prof=prof, image=image)


if __name__ == '__main__':
    app.run(debug=True)