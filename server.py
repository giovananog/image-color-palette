from flask import Flask, render_template, request, redirect
import os
from functions import get_colors

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
path = 'None'

@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'POST':
        if 'file' not in request.files:
                return 'Nenhum arquivo enviado!'
        file = request.files['file']
        if file.filename == '':
                return 'Nenhum arquivo selecionado!'
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            global path
            path = file_path
            return render_template('index.html', filename=file_path)
    else:
        return render_template('index.html')

@app.route('/image', methods=['POST'])
def image_show_page():
    global path

    rgb_list = get_colors(path, request.form['count'])
    return render_template('show-img.html', list=rgb_list, filename=path)

if __name__ == '__main__':
    app.run(debug=True)
