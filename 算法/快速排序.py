def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]  #基准值
        print(pivot)
        less = [i for i in arr[1:] if i <=pivot] #小于基准值的数组
        greater = [i for i in arr[1:] if i > pivot]  #大于基准值的数组
        print( less+[pivot]+greater )
        return quicksort(less) + [pivot] + quicksort(greater)  #迭代

print( quicksort([4,5,1,2,3,15]))