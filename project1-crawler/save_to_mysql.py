import pymysql
import json
import os

client = pymysql.connect(
            host="121.5.218.161",
            port=3306,
            user="root",
            passwd="zcy723",
            db="crawler_data",
            charset="utf8mb4"
        )

cursor = client.cursor()

insert_order_sql = \
    'INSERT INTO crawler_data (URL, TITLE, CATEGORY, CONTENT) VALUES (%s, %s, %s, %s)'

path = "crawler_data"
files = os.listdir(path)

for file in files:
     if not os.path.isdir(file):
         with open(path + "/" + file, encoding='utf8') as fp:
             data = json.load(fp)
             cursor.execute(insert_order_sql, [data["url"],data["title"],data["category"],data["content"]])

client.commit()
client.close()
cursor.close()