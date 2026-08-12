class Node:
    def __init__(self, key = None, val=None):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key

class LRUCache:

    def insert_at_tail(self, key,val = None):
        node = self.kv[key]
        if val != None:
            node.val = val
        if node == self.tail:
            return
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
        node.next = None
        self.tail.next = node
        node.prev = self.tail
        self.tail = self.tail.next

    def __init__(self, capacity: int):
        self.kv = {}
        self.q = Node()
        self.length = 0
        self.capacity = capacity
        self.tail = self.q
        self.p = Node()
        self.q.next = self.p
        self.p.prev = self.q

    def get(self, key: int) -> int:
        if key in self.kv:
            self.insert_at_tail(key)
            return self.kv[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self.insert_at_tail(key, value)
        else:
            if self.length == self.capacity:
                temp = self.q.next.next
                self.q.next.next = None
                self.q.next.prev = None
                k = self.q.next.key
                self.q.next = temp
                if temp != None:
                    temp.prev = self.q
                del self.kv[k]
                self.length -= 1
            node = Node(key, value)
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next
            self.kv[key] = node
            self.length += 1