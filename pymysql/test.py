import pymysql
import pymysql.cursors
import pandas as pd
import codecs

#establish connection
#add 'use_unicode=True' to read Chinese
db = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='douban', port=3306, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, use_unicode=True)


cursor = db.cursor()


'''
#create
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
'''

'''
#update
cursor.execute("update movie set title=%s, rating=%s where rank=1", ['肖申克的救赎', 9.6])
'''

'''
#read
cursor.execute("select * from movie")
#movies = cursor.fetchone()
movies = cursor.fetchall()
print(len(movies))
'''


'''
#insert
cursor.execute("insert into movie(rank, title, rating, director) values(%s, %s, %s, %s)", [250, "MyStory", 10, "EllenXu"])
'''

'''
#delete
cursor.execute("delete from movie where rank = %s", [250])
'''

#output
#if the output csv file still no Chinese, go to notepad++ convert to 'UTF-8 without BOM'.
query = "select * from movie"
result = pd.read_sql_query(query,db)
result.to_csv("output.csv", index=False)

cursor.close()
db.close()
