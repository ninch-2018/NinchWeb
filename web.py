import multiprocessing as mp

from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import os
import eval

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)
app.config['DEBUG'] = True


# 投稿画像の保存先
UPLOAD_FOLDER = './static/images/default'

# ルーティング。/にアクセス時


@app.route('/')
def index():
    result = eval.evaluation()
    print(result)
    return render_template('camera.html', result=result)


@app.route('/post', methods=['POST'])
def post():

    return render_template("index.html", result=result)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
