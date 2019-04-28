import createsimdata
import createfielddata
from ChidTraingTest import PercetionChildTraingTest
import numpy as np
import pandas as pd
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
sigma1_field = 6
sigma2_field = 5
#1 制造服从正态分布的仿真数据 createsindata\data_sim是仿真数据
# data_sim = createsimdata.SimDate(num_sim,  mu1_field, mu2_filed, sigma1_field, sigma2_field)
# print(data_sim)
# print(np.mean(data_sim['X']))
# print(np.mean(data_sim['Y']))
# print(np.std(data_sim['X']))
# print(np.std(data_sim['Y']))

# 2 制造现场数据，有两种情况：仿真和现场试验数据同分布和不同分布
# 2.1 仿真和现场试验数据同分布data_field
# data_field0 = createsimdata.SimDate(num_filed, mu1_field, mu2_filed, sigma1_field, sigma2_field)
# print(data_field0)
# 2.2 仿真和现场试验数据不同分布data_field1
# data_field1 = createfielddata.FieldDate(num_filed, mu1_field, mu2_filed, sigma1_field, sigma2_field)
# print(data_field1)

# 3 结合8个仿真和4个现场 是12行数据，从12行数据中提取分布
percetion = PercetionChildTraingTest()
# print(percetion)
print(np.mean(percetion['mux']), np.mean(percetion['muy']), np.mean(percetion['sigmax']), np.mean(percetion['sigmay']))
# 4 bagging 集成学习 随机森林


# 4 贝叶斯决策

# 5 基模型

# 6 最大熵

# 7 画图，决策
