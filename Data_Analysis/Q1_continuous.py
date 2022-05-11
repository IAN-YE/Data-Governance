import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'heart_data.csv')
print(df.shape)

Y = df['HeartDisease']
X_BMI = df['BMI']
X_BMI_True = df[(df['HeartDisease'] == 'Yes')]['BMI']
X_BMI_False = df[(df['HeartDisease'] == 'No')]['BMI']

X_MentalHealth = df['MentalHealth']
X_MentalHealth_True = df[(df['HeartDisease'] == 'Yes')]['MentalHealth']
X_MentalHealth_False = df[(df['HeartDisease'] == 'No')]['MentalHealth']

X_PhysicalHealth = df['PhysicalHealth']
X_PhysicalHealth_True = df[(df['HeartDisease'] == 'Yes')]['PhysicalHealth']
X_PhysicalHealth_False = df[(df['HeartDisease'] == 'No')]['PhysicalHealth']

a = list(range(0,80,5))

plt.figure(figsize=(20,10))
plt.rcParams['font.family'] = 'SimHei'

plt.subplot(231)
plt.xlabel('BMI')
plt.ylabel('number of person')
plt.xticks(a)
plt.hist(X_BMI, bins=50, color='royalblue', edgecolor='black', rwidth=0.8)
plt.title('BMI分布图', fontproperties='SimHei', fontsize=15)

plt.subplot(232)
plt.rcParams['font.family'] = 'SimHei'
plt.xlabel('身体不健康天数')
plt.ylabel('number of person')
plt.hist(X_PhysicalHealth, bins=30, color='royalblue', edgecolor='black', rwidth=0.8)
plt.title('身体不健康天数分布', fontproperties='SimHei', fontsize=15)

plt.subplot(233)
plt.rcParams['font.family'] = 'SimHei'
plt.xlabel('心理不健康天数')
plt.ylabel('number of person')
plt.hist(X_MentalHealth, bins=30, color='royalblue', edgecolor='black', rwidth=0.8)
plt.title('心理不健康天数分布', fontproperties='SimHei', fontsize=15)

plt.subplot(234)
plt.rcParams['font.family'] = 'SimHei'
plt.xlabel('BMI')
X__BMI = [X_BMI_True,X_BMI_False]
colors = ['tomato', 'royalblue']
labels = ['患病者', '不患病者']
plt.ylabel('number of person')
plt.hist(X__BMI, bins=50, color=colors, rwidth=0.8, stacked=True, label=labels)
plt.title('BMI 对患有冠心病的影响', fontproperties='SimHei', fontsize=15)
plt.legend(loc='upper right')

plt.subplot(235)
plt.rcParams['font.family'] = 'SimHei'
plt.xlabel('身体不健康天数')
X__PhysicalHealth = [X_PhysicalHealth_True,X_PhysicalHealth_False]
colors = ['tomato', 'royalblue']
labels = ['患病者', '不患病者']
plt.ylabel('number of person')
plt.hist(X__PhysicalHealth, bins=30, color=colors, rwidth=0.8, stacked=True, label=labels)
plt.title('身体不健康天数对患有冠心病的影响', fontproperties='SimHei', fontsize=15)
plt.legend(loc='upper right')

plt.subplot(236)
plt.rcParams['font.family'] = 'SimHei'
plt.xlabel('心理不健康天数')
X__MentalHealth = [X_MentalHealth_True,X_MentalHealth_False]
colors = ['tomato', 'royalblue']
labels = ['患病者', '不患病者']
plt.ylabel('number of person')
plt.hist(X__MentalHealth, bins=30, color=colors, rwidth=0.8, stacked=True, label=labels)
plt.title('心理不健康天数对患有冠心病的影响', fontproperties='SimHei', fontsize=15)
plt.legend(loc='upper right')

plt.show()

