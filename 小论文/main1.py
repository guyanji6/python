import createsimdata
import createfielddata
from ChidTraingTest import PercetionChildTraingTest
import k_means
import KNN
import numpy as np
import ChidTraingTest
import bootstrap
import pandas as pd
import time
import sqlite3
# 仿真初始化
num_sim = 6 #仿真数量
mu1_sim = 10  #X均值
mu2_sim = 1   #Y均值
sigma1_sim = 1.25   #X方差
sigma2_sim = 3      #Y方差
# 现场试验初始化
num_filed = 4  #现场试验数量
mu1_field = 100
mu2_filed = 120
sigma1_field = 10
sigma2_field = 15

#1 制造服从正态分布的仿真数据 createsindata\data_sim是仿真数据
# data_sim = createsimdata.SimDate(num_sim,  mu1_field, mu2_filed, sigma1_field, sigma2_field)
# print(data_sim)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) )


# 现场数据

data_field1 = pd.DataFrame([108.239297,96.444860,85.395987,108.772511],
                           [115.740492,121.602448,127.057818  ,120.577064])
data_field1 = data_field1.reset_index()
data_field1.columns=['X','Y']

num_childtraingtest =4000  #子训练集个数
print('训练组数',num_childtraingtest)

# 3 结合6个仿真和4个现场 是10行数据，从10行数据中提取分布
childtest = ChidTraingTest.TraingTest(data_field1, num_childtraingtest)

# 4 bootstrap 采样
loops = 100
percetion_m_childTest = pd.DataFrame()
for i in range(0, num_childtraingtest * 10, 10) :
    data2 = childtest[i:i+10]
    # print( bootstrap.Bootstrap(data2) )
    percetion_m_childTest = percetion_m_childTest.append( bootstrap.Bootstrap(data2 , loops).ix[0] )

percetion_m_childTest = percetion_m_childTest.reset_index(drop= True)
percetion_m_childTest.columns = ['mux', 'muy', 'sigmax', 'sigmay']
# print(percetion_m_childTest)
percetion_m_childTest.to_excel('3.xlsx')

s3 = [np.mean(percetion_m_childTest['mux']), np.mean(percetion_m_childTest['muy']),
      np.mean(percetion_m_childTest['sigmax']), np.mean(percetion_m_childTest['sigmay'])]
print('所有的平均值，直接平均 :')
print(s3 )



# 4 聚类
s4 = k_means.k_means(percetion_m_childTest)
s4 = pd.DataFrame(s4)
print('k_means聚类后 ：')
print(s4)


# 5 KNN
# s5 = KNN.KNN(percetion_m_childTest)
# print('s5 ,KNN:',s5)

# 6误差平方和
aa = [100,120,10,15]
D =[]
for i in range(4):
    d = ( aa[i] - s3[i] ) *( aa[i] - s3[i] )
    D.append(d)
print('误差平方和')
print(D)
# 7 画图，决策
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) )