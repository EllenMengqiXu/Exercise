
import pymysql
import pymysql.cursors
import pandas as pd
import codecs

db = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='douban', port=3306, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

fr=open('testdouban.csv', 'r', encoding = 'utf8')

count = 0
for line in fr:
	count += 1
	print(count)
	if count == 1:
		continue
	line = line.strip().split('^')
	cursor.execute("insert into movie(rank, title, rating, director) values(%s, %s, %s, %s)", [line[0], line[1], line[2], line[3]])

fr.close()

cursor.close()
db.close()
