import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

df = pd.read_csv(r'heart_data.csv')

Y = ['No', 'Yes']

X_AgeCategory_list = sorted(df['AgeCategory'].unique())
X_Smoking_list = sorted(df['Smoking'].unique())
X_AlcoholDrinking_list = sorted(df['AlcoholDrinking'].unique())

#AgeCategory
X_AgeCategory = df[['HeartDisease', 'AgeCategory']]
X_AgeCategory_plot = []
X_AgeCategory_yes = list(X_AgeCategory[X_AgeCategory['HeartDisease'] == 'Yes'].value_counts().sort_index())
X_AgeCategory_no = list(X_AgeCategory[X_AgeCategory['HeartDisease'] == 'No'].value_counts().sort_index())

X_AgeCategory_plot.append(X_AgeCategory_no)
X_AgeCategory_plot.append(X_AgeCategory_yes)

# print(X_AgeCategory_list)
# print(X_AgeCategory.value_counts().sort_index())
# print(list(X_AgeCategory[X_AgeCategory['HeartDisease'] == 'No'].value_counts().sort_index()))
#print(X_AgeCategory_plot,np.sum(X_AgeCategory_plot,axis=0))
X_AgeCategory_plot = np.divide(X_AgeCategory_plot,np.sum(X_AgeCategory_plot,axis=0))

#Smoking
X_Smoking = df[['HeartDisease', 'Smoking']]
X_Smoking_plot = []
X_Smoking_yes = list(X_Smoking[X_Smoking['HeartDisease'] == 'Yes'].value_counts().sort_index())
X_Smoking_no = list(X_Smoking[X_Smoking['HeartDisease'] == 'No'].value_counts().sort_index())

X_Smoking_plot.append(X_Smoking_no)
X_Smoking_plot.append(X_Smoking_yes)

X_Smoking_plot = np.divide(X_Smoking_plot,np.sum(X_Smoking_plot,axis=0))

#AlcoholDrinking
X_AlcoholDrinking = df[['HeartDisease', 'AlcoholDrinking']]
X_AlcoholDrinking_plot = []
X_AlcoholDrinking_yes = list(X_AlcoholDrinking[X_AlcoholDrinking['HeartDisease'] == 'Yes'].value_counts().sort_index())
X_AlcoholDrinking_no = list(X_AlcoholDrinking[X_AlcoholDrinking['HeartDisease'] == 'No'].value_counts().sort_index())

X_AlcoholDrinking_plot.append(X_AlcoholDrinking_no)
X_AlcoholDrinking_plot.append(X_AlcoholDrinking_yes)

X_AlcoholDrinking_plot = np.divide(X_AlcoholDrinking_plot,np.sum(X_AlcoholDrinking_plot,axis=0))


plt.figure(figsize=(20,10))
plt.rcParams['font.family'] = 'SimHei'


plt.subplot(231)
plt.xticks(ticks=[0,1,2,3,4,5,6,7,8,9,10,11,12],labels=X_AgeCategory_list,rotation=90)
plt.yticks(ticks=[0,1],labels=Y)
plt.imshow(X_AgeCategory_plot,cmap='pink', aspect='auto', alpha=0.8)
plt.colorbar()
plt.xlabel('不同年龄段')
plt.ylabel('是否患有冠心病')
plt.title('不同年龄段患有冠心病比例')

plt.subplot(232)
plt.xticks(ticks=[0,1],labels=X_Smoking_list)
plt.yticks(ticks=[0,1],labels=Y)
plt.imshow(X_Smoking_plot,cmap='magma', aspect='auto', alpha=0.8)
plt.colorbar()
plt.xlabel('是否抽烟')
plt.ylabel('是否患有冠心病')
plt.title('抽烟者患有冠心病比例')

plt.subplot(233)
plt.xticks(ticks=[0,1],labels=X_AlcoholDrinking_list)
plt.yticks(ticks=[0,1],labels=Y)
plt.imshow(X_AlcoholDrinking_plot, cmap='magma', aspect='auto', alpha=0.8)
plt.colorbar()
plt.xlabel('是否喝酒')
plt.ylabel('是否患有冠心病')
plt.title('喝酒者患有冠心病比例')

plt.subplot(234)
plt.xticks(rotation=90)
plt.bar(X_AgeCategory_list,X_AgeCategory_plot[1],width=0.2,label='患有冠心病',color='tomato')
plt.bar(X_AgeCategory_list,X_AgeCategory_plot[0],width=0.2,bottom=X_AgeCategory_plot[1],label='未患有冠心病',color='royalblue')

plt.xlabel('不同年龄段')
plt.ylabel('是否患有冠心病')
plt.title('不同年龄段患有冠心病比例')
plt.legend(loc='upper right')

plt.subplot(235)
# plt.xticks(ticks=[0,1],labels=X_AlcoholDrinking_list)
plt.bar(X_Smoking_list,X_Smoking_plot[1],width=0.2,label='患有冠心病',color='tomato')
plt.bar(X_Smoking_list,X_Smoking_plot[0],width=0.2,bottom=X_Smoking_plot[1],label='未患有冠心病',color='royalblue')

plt.xlabel('是否抽烟')
plt.ylabel('是否患有冠心病')
plt.title('抽烟者患有冠心病比例')
plt.legend(loc='upper right')

plt.subplot(236)
# plt.xticks(ticks=[0,1],labels=X_AlcoholDrinking_list)
plt.bar(X_AlcoholDrinking_list,X_AlcoholDrinking_plot[1],width=0.2,label='患有冠心病',color='tomato')
plt.bar(X_AlcoholDrinking_list,X_AlcoholDrinking_plot[0],width=0.2,bottom=X_AlcoholDrinking_plot[1],label='未患有冠心病',color='royalblue')

plt.xlabel('是否喝酒')
plt.ylabel('是否患有冠心病')
plt.title('喝酒者患有冠心病比例')
plt.legend(loc='upper right')

plt.show()
，