class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.cache = {} # key-[value, node] pair
        # use a doubly linked list to store the last used item
        self.head = None # LRU
        self.tail = None # most recently used

    def get(self, key):
        #print("get:", key)
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            value, node = self.cache[key]
            self.move(node)  
            return value
        else:
            return -1

    def put(self, key, value):
        #print("put:", key, value)
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # existing key. update value
        if key in self.cache:
            self.cache[key][0] = value
            # move node to the end of DDL
            node = self.cache[key][1]
            self.move(node)
            
        # non-existing key
        else:
            if self.size == self.capacity: # will exceed capacity after adding this k-v pair
                # evict the least recently used key
                LRU = self.head 
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                # update tail if needed
                else:
                    self.tail = None
                # remove k-v from cache
                #print(LRU.val) 
                self.cache.pop(LRU.val)
                # update size
                self.size -= 1
                    
            # add k-[v, node] pair
            node = Node(key)
            self.add(node)
            self.cache[key] = [value, node]  
            # update size
            self.size += 1
        
    def move(self, node):
        #print("move:", node.val)
        '''
        :type node: Node
        :rtype: None
        move the node to the end of doubly-linked-list
        '''
        # if node is not already tail, move node to the end of DDL
        if node.next:
        
            # node is head
            if not node.prev:
                self.head = node.next
                self.head.prev = None

            # node is not head nor tail
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            
            # attach node at tail
            node.next = None
            self.tail.next = node
            node.prev = self.tail
            self.tail = node         
        
    def add(self, node):
        #print("add:", node.val)
        '''
        :type node: Node
        :rtype: None
        add the node to the end of doubly-linked-list
        '''
        # empty DDL
        if not self.head:
            self.head = node
            self.tail = node 
        # DDL not empty
        else:
            self.tail.next = node
            node.prev = self.tail 
            self.tail = node
        

class Node():
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)