import pandas as pd
import numpy as np
import random
import xlwt
data_field1 = pd.DataFrame([108.239297,96.444860,85.395987 ,108.772511 ],
                           [115.740492,121.602448,127.057818,120.577064])

# data_field1 = data_field1.reset_index()
# data_field1.columns=['X','Y']
# print(data_field1)
# result = [np.mean(data_field1['X']), np.mean(data_field1['Y']), np.std(data_field1['X']), np.std(data_field1['Y'])]
# print('现场数据分布 :', result)
#
# data_field1.to_excel('11.xlsx')
# result = pd.DataFrame(result).T
# # print(result)
# print(type(result))
# result.to_excel('11.xlsx')

m = random.randint(90,90)
print(m)
m1 = random.uniform(3,3)
print(m1)
print('---')
aa = [100,120,10,15]
s =[108.35310611995372, 112.00753914084623, 14.85721333082463, 17.995327396443596]
sa=[]
m1= 0

for i in range(4) :
    d = (aa[i] -s[i])
    d = d*d
    m1 +=d
sa.append(m1)
print(sa)