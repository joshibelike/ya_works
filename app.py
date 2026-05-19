from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    title = "Колонизация Марса"
    return render_template('base.html', title=title)


@app.route('/table/<gender>/<int:age>')
def table(gender, age):
    if gender == 'male':
        if age < 21:
            wall_color = "#87CEEB"
        else:
            wall_color = "#4682B4"
    else:  # female
        if age < 21:
            wall_color = "#FFB6C1"
        else:
            wall_color = "#CD5C5C"

    if age < 21:
        alien_image = "child.jpg"
        alien_status = "марсианин-ребенок"
    else:
        alien_image = "adult.jpg"
        alien_status = "взрослый марсианин"

    return render_template('table.html',
                           gender=gender,
                           age=age,
                           wall_color=wall_color,
                           alien_image=alien_image,
                           alien_status=alien_status)


if __name__ == '__main__':
    app.run(debug=True)