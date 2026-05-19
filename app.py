from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    title = "Колонизация Марса"
    return render_template('base.html', title=title)


@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    # Список профессий для миссии на Марсе
    professions = [
        "Инженер-конструктор",
        "Биолог",
        "Геолог",
        "Программист",
        "Врач",
        "Психолог",
        "Строитель",
        "Астроном"
    ]

    return render_template('list_prof.html',
                           list_type=list_type,
                           professions=professions)


if __name__ == '__main__':
    app.run(debug=True)