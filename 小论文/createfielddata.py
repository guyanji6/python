# 产生仿真数据
import numpy as np
import random
import pandas as pd
# num_simdata 是产生的仿真数据的个数
def FieldDate(num_simdate ,mu1, mu2, sigma1 ,sigma2) :
    n1 = []
    n2 = []

    for i in range(num_simdate) :
        n1.append( random.gauss(mu1, sigma1)) #产生符合高斯分布的X数据
    for i in range(num_simdate):
        n2.append(random.gauss(mu2, sigma2))  # 产生符合高斯分布的Y数据

    obj = pd.DataFrame(n2,n1)
    obj = obj.reset_index()
    obj.columns = ['X','Y']

    # print(n1)
    # print(n2)

    return obj


