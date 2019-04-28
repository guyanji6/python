# 路程表
graph ={}
graph['start']={}
graph['start']['a']=6
graph['start']['b']=2
# print(graph['start'].keys())
graph['a']={}
graph['a']['fin']=1

graph['b']={}
graph['b']['fin']=5
graph['b']['a']=3

graph['fin']={}
# 代价表
costs={}
infinity = float('inf') #无穷大

costs['a']=6
costs['b']=2
costs['fin']=infinity

# 父节点
parents={}
parents['a']='start'
parents['b']='start'
parents['fin']='None'

# 处理过的节点
procesed=[]

#
def find_lowest_cost_node(costs):
    lowest_coat = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost<lowest_coat and node not in procesed:
            lowest_coat = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbores = graph[node]
    for n in neighbores.keys():
        new_cost = cost+neighbores[n]
        if costs[n]>new_cost:
            costs[n]=new_cost
            parents[n]=node
    procesed.append(node)
    node = find_lowest_cost_node(costs)
print(costs)