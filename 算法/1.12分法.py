def binnary_search(list, item):
    low = 0
    high = len(list) -1

    while low<=high:
        mid = (high + low)
        guess = list[mid]
        if guess == item:
            return mid
        if guess >item:
            high = mid -1
        else:low = mid+1
    return None

list = [1,3,5,7,9,11,51,69]
print( binnary_search(list,5)+1)
print( binnary_search(list,51)+1)
