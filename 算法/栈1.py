# 用列表实现栈
class ArrayStack():
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def push(self):
        pass
    def pop(self):
        pass
n =5
for i in range(n,0,-1):
    print(i)