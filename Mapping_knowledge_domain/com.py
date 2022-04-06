import numpy as np
import pandas as pd

df = pd.read_csv(r'data.csv')
print(df.shape)

count = 0
for i in range(1120):
    for j in range(i+1 ,1120):
        if df['province'][i] == df['province'][j] and df['industry_1'][i] == df['industry_1'][j]:
            print(df['name'][i],df['name'][j])
            count += 1

print(count)