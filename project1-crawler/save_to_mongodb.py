import os
import json
import pymongo

# connect to DB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["crawler_data"]['crawler_data']

path = "crawler_data"
files = os.listdir(path)
for file in files:
     if not os.path.isdir(file):
         with open(path + "/" + file, encoding='utf8') as fp:
             data = json.load(fp)
             db.insert_one(data)