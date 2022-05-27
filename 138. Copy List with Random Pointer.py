"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # base case
        if not head:
            return None
        
        new_head = Node(head.val)
        
        OLD = head
        NEW = new_head
        
        # hash table for memorization
        # key: random index
        # val: node
        t = {}
        t[head] = new_head
        
        # copy the node val and next pointer
        while OLD.next:
            OLD = OLD.next            
            NEW.next = Node(OLD.val)
            NEW = NEW.next
            # add node idx into hash table
            t[OLD] = NEW
        
        # copy the random pointer
        OLD = head
        NEW = new_head
        while NEW:
            if OLD.random:
                NEW.random = t[OLD.random]
            OLD = OLD.next
            NEW = NEW.next
        
        return new_head