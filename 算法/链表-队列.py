class LinkedQuene():

    class _Node():
        __slots__ = '_element','_next'

        def __init__(self, element, _next):
            self._element = element
            self._next = _next

    def __init__(self):
        self._head =None
        self._tail =None
        self._size =0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size ==0
    def first(self):
        if self.is_empty():
            return False
        return self._head._element
    # 出队，头部
    def dequeue(self):
        if self.is_empty():
            return False
        ansewer = self._head._element
        self._head = self._head._next
        self._size -=1
        if self.is_empty():
            return False
        self._tail._next = None
        return ansewer
    
    def enqueue(self):
        newest = self._Node(e,None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest #更新尾节点指针
        self._size+=1
        
        


        