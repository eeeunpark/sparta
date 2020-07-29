from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

wall_e = db.movies.find_one({'title' : '월-E'})

same_point_movies = list(db.movies.find (
    {'point':wall_e['point']}
))

for movie in same_point_movies:
    print (movie['title'])