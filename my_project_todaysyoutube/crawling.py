import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 브이로그
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.youtube.com/results?search_query=%EB%B8%8C%EC%9D%B4%EB%A1%9C%EA%B7%B8',
                    headers=headers)

print(data.text)
soup = BeautifulSoup(data.text, 'html.parser')

video_list_info = soup.select('#contents > ytd-item-section-renderer')

# video-title > yt-formatted-string >
# video-title > yt-formatted-string
#contents > ytd-video-renderer:nth-child(1)

for video_info in video_list_info:
    img_url = video_info.select_one ('thumbnail' > 'yt-img-shadow' > 'img' > 'src')
    title = video_info.select_one('video-title' > 'yt-formatted-string' > 'title')
    video_url = video_info.select_one ('video-title' > 'yt-formatted-string' > 'href')

    print(image_url.src, title["title"], video_url.href)


