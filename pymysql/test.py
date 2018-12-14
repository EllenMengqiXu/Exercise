
import pymysql
import pymysql.cursors

db = pymysql.connect(host='localhost', user='root', passwd='root', db='douban', port=8080, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

fr=open('DoubanTop250_^.csv', 'r')

count=0
for line in fr:
	count+=1
	print(count)
	if count == 1:
		continue
	line = line.strip().split('^')
	cursor.execute("insert into movie(title, rating, director, runtime, Released Date, Released Country, Genre, quote, url, counts) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10]])

fr.close()

cursor.close()
db.close()