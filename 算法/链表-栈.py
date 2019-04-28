# 创建node类，节点
class _Node:
    __slots__ = '_element','_next'

    def __init__(self, element, _next):
        self._element = element
        self._next = _next

# 单向链表，栈
class LinkedStack():
    # 创建node类，节点
    class _Node():
        __slots__ = '_element','_next'

        def __init__(self, element, _next):
            self._element = element
            self._next = _next
    def __init__(self):
        self._head = None
        self._size = 0
    
    def len(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self,e):
        self._head = self._Node(e, self._head)
        self._size +=1
    
    def top(self):
        if self.is_empty:
            return None
        else:
            return self._head._element
    def pop(self):
        if self.is_empty:
            return None
        answer  =self._head._element
        self._head = self._head._next
        self._size -=1
        return answer