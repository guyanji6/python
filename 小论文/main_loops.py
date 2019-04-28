import createsimdata
import createfielddata
from ChidTraingTest import PercetionChildTraingTest
import k_means
import KNN
import matplotlib.pyplot as plt
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
D = []
H = []
num_childtraingtest = 2

for j in range(100,1000,25) :
    H.append(j)
    loops =j  #bootstrap采样循环次数,修改
    # print('训练组数',num_childtraingtest)
    # D =pd.DataFrame( index= num_childtraingtest)
    # 3 结合6个仿真和4个现场 是10行数据，从10行数据中提取分布
    childtest = ChidTraingTest.TraingTest(data_field1, num_childtraingtest)
    # 4 bootstrap 采样
    percetion_m_childTest = pd.DataFrame()
    for i in range(0, num_childtraingtest * 10, 10) :
        data2 = childtest[i:i+10]
        # print( bootstrap.Bootstrap(data2) )
        percetion_m_childTest = percetion_m_childTest.append( bootstrap.Bootstrap(data2,loops).ix[0] )
    percetion_m_childTest = percetion_m_childTest.reset_index(drop= True)
    percetion_m_childTest.columns = ['mux', 'muy', 'sigmax', 'sigmay']

    s3 = [np.mean(percetion_m_childTest['mux']), np.mean(percetion_m_childTest['muy']),
          np.mean(percetion_m_childTest['sigmax']), np.mean(percetion_m_childTest['sigmay'])]
    # print(s3)

    # 6误差平方和
    aa = [100,120,10,15]
    d1 = 0
    for i in range(4):
        d = 0
        d = ( aa[i] - s3[i] ) *( aa[i] - s3[i] )
        d1 += d
        d1 = d1/24725
    D.append(d1)
    print('D ,loops:',D)

# 结果显示
print('训练组数：',H)
print('误差平方和')
print(D)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) )

m1 = []
for i  in range(100,1000,25) :
    m1.append(i)
plt.xlabel('n')
plt.ylabel('P')
plt.plot(m1,D,marker = '*')