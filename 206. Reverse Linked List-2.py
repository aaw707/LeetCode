# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # base case
        if not head:
            return head
        
        # key: idx
        # val: node
        t = {}
        idx = 0
        
        # iteratively reverse
        
        # put all nodes into a hash table
        while head:
            idx += 1
            t[idx] = head
            head = head.next 
        
        # reverse by referring to the hash table
        new_head = t[idx]
        node = new_head
        while idx > 1:
            idx -= 1
            node.next = t[idx]
            node = node.next 
            
        node.next = None
        return new_head
            
        
        
