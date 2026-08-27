class Node:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache(object):

        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = {}
        #dummy nodes
            self.head = Node()
            self.tail = Node()
            self.head.next = self.tail
            self.tail.prev = self.head
    #remove nodes
        def remove(self,node):
            node.prev.next = node.next
            node.next.prev = node.prev
    #insert nodes
        def insert(self,node):
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node

        def get(self, key):
            if key not in self.cache:
                return -1
            node = self.cache[key]
        #move node to mru
            self.remove(node)
            self.insert(node)
            return node.value


        def put(self, key, value):
            if key in self.cache:
                self.remove(self.cache[key])
            node = Node(key,value)
            self.cache[key] =  node
            self.insert(node)
            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)