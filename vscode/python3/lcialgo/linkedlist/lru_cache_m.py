class Node:
    def __init__(self, key, value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dicti=dict()
        self.head,self.tail=Node(0,0),Node(0,0)
        self.head.right=self.tail
        self.tail.left=self.head

    def put(self, key:int, value:int) -> None:
        if key in self.dicti:
            self._remove(node)
        node=Node(key,value)
        self.dicti[key]=node        
        self._add(node)
        if len(self.dicti)>self.capacity:
            node=self.head.right
            self._remove(node)
            del self.dicti[node.key]

    def get(self, key:int) -> int:
        if key in self.dicti:
            node=self.dicti[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def _add(self, node):
        prev=self.tail.left
        self.tail.left=node
        node.right=self.tail
        prev.right=node
        node.left=prev

    def _remove(self, node):
        next=node.right
        prev=node.left
        prev.right=next
        next.left=prev


# Test case
def test_LRUCache():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

test_LRUCache()