list = [(2,4),(3,10),(5,3),(6,8),(8,2),(10,6),(13,5),(15,7),(8,0)]
# print(list)
list.sort()
def search(list):
    if len(list)==1:
        return list

    # print(list)
    mid = int( len(list)//2 )
    list_left = list[0:mid]
    list_right = list[mid:]

    list_left_get = search(list_left)
    list_right_get = search(list_right)

    max_y= max( [i[1] for i in list_left_get])

    list_left_get = [i for i in list_left_get if i[1]>max_y ]
    list_right_get.extend(list_left_get)
    return list_right_get



raise ValueError('x>0')
print(search(list))