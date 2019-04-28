import json

filename = '111.json'
with open(filename) as f:
    num =json.load(f)
print(num)