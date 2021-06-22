import time,os

from flask import Flask, request, render_template


app = Flask(__name__, template_folder="html")

@app.route('/')
def index():
    return render_template('img_index.html')

@app.route('/uploads', methods=['POST'])
def load():
    # 获取图片
    file =  request.files.get('pic')
    if not file:
        return render_template('img_index.html')

    file_name = time.strftime('%Y-%m-%d-%H-%M-%S')+file.filename
    file_url = f'/static/{file_name}'
    file.save(os.path.join(
        app.root_path,
        app.static_folder,
        file_name
    ))

    return file_url


if __name__ == '__main__':
    app.run(debug=True)