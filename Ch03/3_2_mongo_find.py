"""
날짜 : 2021/01/04
이름 : 김하린
내용 : 파이썬 Mongodb 프로그래밍
"""

from pymongo import MongoClient as mongo
from _datetime import datetime

# 1단계 - mongodb 접속
conn = mongo('mongodb://khl:1234@192.168.56.104:27017')

# 2단계 - DB 선택
db = conn.get_database('khl')

# 3단계 - collection(table) 선택
collection = db.get_collection('member')

# 4단계 - 쿼리 실행
rs1 = collection.find()

for row in rs1:
    print('---------------------------------------')
    print('%s, %s, %s' % (row['uid'], row['name'], row['hp']))

# select * from `member` where uid='a101'
rs2 = collection.find({'uid':'a101'})

for row in rs2:
    print('---------------------------------------')
    print('%s, %s, %s, %s' % (row['name'], row['pos'], row['dep'], row['rdate']))
