from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
            return render_template('index.html', filename=file_path)
    else:
        return render_template('index.html')

@app.route('/image')
def image_show_page():
    return render_template('show-img.html')

if __name__ == '__main__':
    app.run(debug=True)
