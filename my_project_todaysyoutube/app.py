from flask import Flask, render_template, jsonify, request
from bs4 import BeautifulSoup
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/videolist', methods=['GET'])
def show_videolist():
    # 1. 첫번째 카테고리와 두번째 카테고리의 조건을 만족시키는 영상 리스트를 뽑는다.
    # 2. 성공하면 영상 리스트 중 상위 10개를 클라이언트에 전달.
    #여기 함수를 못짜겠어요 ㅠㅠ
    return jsonify({'result':... })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)