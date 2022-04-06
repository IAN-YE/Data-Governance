import os
import json
import pandas as pd

path = "crawler_data"
files= os.listdir(path)

res = []

for file in files:
     if not os.path.isdir(file):
         with open(path + "/" + file, encoding='utf8') as fp:
             tmp = []
             data = json.load(fp)
             tmp.append(data["url"])
             tmp.append(data["title"])
             tmp.append(data["category"])
             tmp.append(data["content"])
             res.append(tmp)

df = pd.DataFrame(res)
df.columns = ['url', 'title', 'category', 'content']
df.to_csv('res.csv', index=False)