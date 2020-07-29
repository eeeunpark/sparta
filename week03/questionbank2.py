#2번 문제뱅크
import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

print(data.text)
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
#############################

baseballs = soup.select('#regularTeamRecordList_table > tr')
#regularTeamRecordList_table > tr:nth-child(1) > th > strong
#regularTeamRecordList_table > tr:nth-child(1) > td.tm > div
#regularTeamRecordList_table > tr:nth-child(1) > td.tm > div
for baseball in baseballs:
    rank = baseball.select_one('th > strong').text
    team = baseball.select_one('td.tm > div > span').text
    print(rank,team)

