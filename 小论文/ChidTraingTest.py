# 1 PercetionChildTraingTest()
# 2 得到是4列的数，是每个子训练集的2个平均数，2个方差。一共是num_childtraingtest行

import createsimdata
import createfielddata
import pandas as pd
import numpy as np
import tensorflow as tf
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
#
# num_childtraingtest =4000  #子训练集个数

# 返回data1 是把6个仿真和4个现场数据结合起来 ，10行数，2列：X，Y
def TraingTest(data_field1, num_childtraingtest) :
    data1 = pd.DataFrame(columns=['X', 'Y'])
    # # 现场数据
    # data_field1 = createfielddata.FieldDate(num_filed, mu1_field, mu2_filed, sigma1_field, sigma2_field)
    # print('现场数据')
    # print(data_field1)
    # result = [np.mean(data_field1['X']), np.mean(data_field1['Y']), np.std(data_field1['X']), np.std(data_field1['Y'])]
    # print('现场数据分布 :' , result)
    # 仿真数据
    for i in range(num_childtraingtest) :
        data_sim = createsimdata.SimDate(num_sim, mu1_field, mu2_filed, sigma1_field, sigma2_field)
        data = data_field1.append(data_sim)
        data = data.reset_index(drop=True)
        data1 = data1.append(data)
        # print(data1)
    # 10行数据是一组，一个很多组数据
    data1 = data1.reset_index( drop=True )
    # print(data1)
    return data1

# 返回percesion， 是4列的数，是每个子训练集的2个平均数，2个方差。一共是num_childtraingtest行
def Percesion(data) :
    percesion = pd.DataFrame(columns=['mux', 'muy', 'sigmax', 'sigmay'])
    print(type(percesion))
    for i in range(0, num_childtraingtest * 10 ,10 ):
        data2 = data[i: i+10]
        percesion1 = [ np.mean(data2['X']), np.mean(data2['Y']), np.std(data2['X']), np.std(data2['Y']) ]
        percesion1 = pd.DataFrame(percesion1)
        percesion1 = percesion1.T
        percesion1.columns = ['mux', 'muy', 'sigmax', 'sigmay']
        percesion =percesion.append(percesion1)
    percesion = percesion.reset_index(drop= True)
    # print(percesion)
    return percesion


def PercetionChildTraingTest(data_field1) :
    data1= TraingTest(data_field1)
    percetion = Percesion(data1)
    return percetion

