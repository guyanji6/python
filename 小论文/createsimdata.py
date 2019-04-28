# 产生仿真数据
import numpy as np
import random
import pandas as pd
# num_simdata 是产生的仿真数据的个数
def SimDate(num_simdate ,mu1, mu2, sigma1 ,sigma2) :
    n1 = []
    n2 = []
    for i in range(num_simdate) :
        mu10 = random.randint(mu1 - 10, mu1 + 10)
        sigma10 = random.uniform(sigma1- 3 , sigma1 + 3)
        # mu10 = mu1 +20
        # sigma10 = sigma1 -3
        n1.append( random.gauss(mu10 , sigma10)) #产生符合高斯分布的X数据
    for i in range(num_simdate):
        mu20 = random.randint(mu2 - 10, mu2 + 10)
        sigma20 = random.uniform(sigma2 - 3, sigma2 + 3)
        # mu20 = mu2 +20
        # sigma20 = sigma2 -3
        n2.append(random.gauss(mu20 , sigma20 ))  # 产生符合高斯分布的Y数据

    obj = pd.DataFrame(n2,n1)
    obj = obj.reset_index()
    obj.columns = ['X','Y']

    # print(n1)
    # print(n2)

    return obj

