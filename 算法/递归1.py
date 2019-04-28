def fac(n):
    if n==0:
        return 1
    while n>0:
        return n*fac(n-1)
# print(fac(3))

# 二分查找,递归
data = [2,4,5,7,8,9,12,14,17,19,50]

def binary_search(data, target,low ,high):
    mid = (low+high)//2
    if data[mid] == target:
        return mid
    elif target < data[mid]:
        return binary_search(data,target,low,mid-1)
    else:
        return binary_search(data,target,mid+1,high)

# a= binary_search(data,7,0,len(data)-1)
# print(a)

# 文件大小
import os
def disk_usagee(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total += disk_usagee(childpath)
    return total

# 斐波那契数 f(n)=f(n-1)+f(n-2)
def fibonacci(n):
    if n<=1:
        return (n,1)
    else:
        (a,b) = fibonacci(n-1)
        return (a+b,a)
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
# print(fibonacci(7))

# 递归逆置序列
def reverse(s,start,stop):
    if start <stop-1: #最少2个数
        s[start] ,s[stop] = s[stop],s[start]
        reverse(s,start+1,stop-1)
# print(data)
# reverse(data, 0, len(data)-1 ) 
# print(data)

# 两路递归 求和
def binary_sum(s,start,stop):
    if start>=stop:
        return 0
    elif start == stop-1:
        return s[start]
    else:
        mid = (start+stop)//2
        return binary_sum(s,start,mid) + binary_sum(s,mid,stop)
print(binary_sum(data,0,4))

