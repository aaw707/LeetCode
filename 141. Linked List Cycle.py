# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # base case
        if not head or not head.next:
            return False
        
        hashtable = {}
        while head:
            key = head
            value = head.next
            if value in hashtable: # as a key
                return True
            else:
                hashtable[key] = value        
                head = head.next
     
        # head == null, not a cycle
        return False
