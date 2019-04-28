# 插入排序
def insertion_sort(data):
    for k in range(1, len(data)):
        cur = data[k]
        j = k
        while j>0 and data[j-1]>cur:
            data[j] = data[j-1]
            j-=1
            data[j] = cur
data = [2,4,1,6,3]
insertion_sort(data)
print(data)
