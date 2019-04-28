def findsmallest(arr):
    smallest  = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if smallest>arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newArr.append( arr.pop(smallest))
    return newArr

print( selection([4,7,1,2,4,5,4]))