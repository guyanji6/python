# 是否存在路径，路径最近,使用队列实现queue
from collections import deque
graph={}
graph['you'] = ['alice','bob','claire']
graph['bob']=['anuj','peggy']
graph['alice']=['peggy']
graph['claire']=['thom','jonny']
graph['anuj']=[]
graph['peggy']=[]
graph['thom']=[]
graph['jonny']=[]
# 创建图
# search_queue = deque()
# search_queue += graph['you']

def person_is_seller(person):
    return person[-1] == 'm'

# while search_queue:
#     # 取出第一个人,在队列中删除
#     person = search_queue.popleft()
#     if person_is_seller(person):
#         print(person + ' is a seller')
#     else:
#         # 添加其他的到图
#         search_queue += graph[person]
#         print(search_queue)

def search(name):
    search_queue =deque()
    search_queue+=graph[name]
    searched=[]
    while search_queue:
        # 取出第一个人,在队列中删除
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a seller')
            else:
                # 添加其他的到图
                search_queue += graph[person]
                searched.append(person)
                # print(search_queue)
search('thom')