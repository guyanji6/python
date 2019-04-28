import  pandas as pd
import  numpy as np



# print('loops' ,loops)
num_bootstrapa = 10 #不修改，来自一个样本10个数
# data是10*2的矩阵
def Bootstrap(data,loops) :
    data = data.reset_index(drop= True) #重设索引，不然迭代时在产生训练集报错
    percetion_origin = pd.DataFrame( [np.mean(data['X']), np.mean(data['Y']), np.std(data['X']), np.std(data['Y']) ]).T
    # print('percetion_origin',percetion_origin)
    # print(data)
    error = pd.DataFrame()
    for i in range(loops) :

        # 训练集 data_train
        data1 = pd.DataFrame(columns=['X', 'Y'])
        # 产生10个随机数
        x = []
        for i in range(num_bootstrapa):
            x.append(np.random.randint(0, 10))
        # print(x)
        for i in x :
            # print(data.ix[i] )
            s = pd.DataFrame(data.ix[i])
            s = s.T
            data1 = data1.append(s)
        # print(data1)
        data1 =data1.reset_index(drop= True)
        data_train = data1
        # print(data_train)

        # 测试集 data_test
        # xx = []
        #         # for i in range(10) :
        #         #     if i in x:
        #         #         continue
        #         #     else:xx.append(i)
        #         # # print(xx)
        #         # data_test = pd.DataFrame( )
        #         # for i in xx :
        #         #     data_test = data_test.append(data.ix[i])
        #         # # print(data_test)

        # 计算偏差 error
        percetion_train = pd.DataFrame( [ np.mean(data_train['X']), np.mean(data_train['Y']), np.std(data_train['X']), np.std(data_train['Y'])] ).T
        # percetion_test = pd.DataFrame([ np.mean(data_test['X']), np.mean(data_test['X']), np.std(data_test['Y']), np.std(data_test['Y']) ]).T
        # print('percetion_test',percetion_test)
        # print('percetion_train',percetion_train)
        R = percetion_train - percetion_origin
        # print('r',R)
        error = error.append(R)
        # print('error' , error)
    # print('error', error)
    error.columns = ['mux', 'muy', 'sigmax', 'sigmay']
    error1 = pd.DataFrame( [ np.mean(error['mux']), np.mean(error['muy']), np.mean(error['sigmax']), np.mean(error['sigmay']) ] ).T
    # error1.columns = ['mux', 'muy', 'sigmax', 'sigmay']
    # print(error1)

    #     修改均值，方差
    percetion_back = percetion_origin - error1
    # print('percetion_back')
    # print( percetion_back)

    return percetion_back

