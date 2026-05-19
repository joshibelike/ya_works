from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mars_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/img'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/')
@app.route('/index')
def index():
    title = "Марсианская галерея"
    return render_template('base.html', title=title)


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    img_folder = os.path.join(app.root_path, 'static', 'img')
    images = []

    if os.path.exists(img_folder):
        for file in os.listdir(img_folder):
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                images.append(file)

    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)
                return render_template('gallery.html',
                                       title="Галерея марсианских пейзажей",
                                       images=images)

    return render_template('gallery.html',
                           title="Галерея марсианских пейзажей",
                           images=images)


if __name__ == '__main__':
    app.run(debug=True)