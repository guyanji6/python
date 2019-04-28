import json
num = [1,2,3,4,5]
filename = '111.json'
with open(filename,'w') as f:
    json.dump(num,f)