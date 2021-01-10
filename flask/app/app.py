## ライブラリインポート
from flask import Flask, render_template
from models import *

## インスタンス生成
app = Flask(__name__, static_folder='static')

IMAGE_PATH = 'https://static.kiichi.work/'

## index
@app.route('/', methods=['GET'])
def index():

    ## レスポンス内容を初期化
    response = {}
    ## タイトル
    response['title'] = 'p4pアルバム'
    
    items = []
    ## S3からファイル名を取得
    filename_list = get_filename_from_s3()
    for filename in filename_list:
        item = {}
        ## HTMLでリンクされるURLへ整形(CloudFront)
        item['image_path'] = IMAGE_PATH + filename
        ## S3からファイル名に紐づくタグを取得
        item['tags'] = get_tags_from_s3(filename)
        items.append(item)
    response['items'] = items

    return render_template('index.html', response=response)


## favicon
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


if __name__ == '__main__':
    app.run()