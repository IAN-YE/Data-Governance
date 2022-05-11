import pandas as pd
import numpy as np

data = pd.read_csv(r'Exp 6_problem3.csv')

df = data[['泡面','沙琪玛','泡腾片','橙子','苹果','梨','酒精棉']]
df = df.copy()
df[df > 0] = 1

df = pd.concat([data['用户ID'], df], axis=1)
# print(df)

df.to_csv('P3_res.csv', index=None)