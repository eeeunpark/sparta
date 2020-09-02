from flask import Flask, render_template, jsonify, request
from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests
from selenium import webdriver
import time

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/videolist/<name>', methods=['GET'])
def show_videolist(name):
    # 타겟 URL을 읽어서 HTML를 받아오고,
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
    path = "/Users/lopun/Downloads/chromedriver"
    driver = webdriver.Chrome(path, options=options)

    # chrome창에서 youtube url open
    driver.get('https://www.youtube.com/results?search_query=' + name)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
    # 이제 코딩을 통해 필요한 부분을 추출하면 된다.
    video_list = list(soup.select('#contents > ytd-video-renderer'))
    print(video_list)

    video_list_to_return = []

    for video in video_list:
        try:
            img_tag = video.select_one("div:nth-child(1) > ytd-thumbnail > a > yt-img-shadow > img")
            title_tag = video.select_one(
                "div:nth-child(1) > div > div:nth-child(1) > div > h3 > a > yt-formatted-string")
            if img_tag != None and title_tag != None:
                video_list_to_return.append({
                    "img_src": img_tag["src"],
                    "title": title_tag.text
                })
        except:
            print("에러남")

    # 1. 첫번째 카테고리와 두번째 카테고리의 조건을 만족시키는 영상 리스트를 뽑는다.
    # 2. 성공하면 영상 리스트 중 상위 10개를 클라이언트에 전달.
    # 여기 함수를 못짜겠어요 ㅠㅠ
    return jsonify({'result': "success", "video_list": video_list_to_return})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
