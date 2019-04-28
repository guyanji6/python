from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
from itertools import groupby

def KNN( percection ) :
    # s = KNeighborsClassifier()
    # s.fit(percection)
    row = percection.shape[0]
    # print(row)
    k = 3
    knn =  int(row/2)

    # a = []
    # # 产生K个随机数，在Percetion的行数之间
    # for i  in range(k) :
    #     s  = np.random.randint(0, row)
    #     a.append(s)
    #     # print(s)
    # a.sort()
    # print(a)
    # # 从percetion选取产生的随机行数a,得到first_choice
    # first_choice = pd.DataFrame()
    # for i in a:
    #     first_choice = first_choice.append( percection.ix[i])
    # first_choice = first_choice.reset_index(drop=True)
    # print(first_choice)

#     计算first_choice的每一行和其他行的距离平方和
#     print( percection.ix[0])
#     print(first_choice.ix[0])
#     d = (percection.ix[0] - first_choice.ix[0])
#     d = d*d
#     dd = d[0] +d[1] + d[2] +d[3]
#     print(d)
#     print(dd)

#     计算平方和
    s_matrix = pd.DataFrame()
    for i in range(row) :
        s = []
        for j in range(row) :
            s1=[]
            s2 =[]
            s3 =[]
            s1 = percection.ix[i] - percection.ix[j]
            s2 = s1 * s1
            s3 = s2[0] + s2[1] + s2[2] +s2[3]
            s.append(s3)
        s = pd.DataFrame(s).T
        s_matrix = s_matrix.append(s)
    # 矩阵行是:每一行和其他行之间的距离平方和,肯定是对称矩阵啊
    s_matrix = s_matrix.reset_index(drop=True)
    # print(s_matrix.index)
    # print(type(s_matrix))
    # print(s_matrix)
    # cc = s_matrix.sort_values(axis=0,ascending=True)
    # print(cc)
    # 找到最小的M数，排序, 每列
    second_choice = pd.DataFrame()
    b=[]
    for i in range(row) :
        a = []
        s = []
        s = s_matrix.ix[i]
        s = s.sort_values()
        s = s[0:knn] #取前KNN个数
        # print(s)
        a = s.index #取索引，放入A,每行的索引
        for i in a :
            b.append(i)
        # print(a[0])
        # print(type(a))
        # print(s.idx())
    b.sort()
    # print(b)
    c = [len(list(group)) for key, group in groupby(b)]
    # print(c)
    d = []
    for i in range(row) :
        if c[i] > knn:
           d.append(i)
    # print(d)
    #  d 是待选取的索引行
    second_choice = second_choice.append(percection.ix[d])
    #
    # 均值，sigma
    s5 = [np.mean(second_choice['mux']), np.mean(second_choice['muy']),
          np.mean(second_choice['sigmax']), np.mean(second_choice['sigmay'])]

    return s5