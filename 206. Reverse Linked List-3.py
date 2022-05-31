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
        
        # iteratively. time O(n), space O(1)
        
        prev = None
        node = head
        
        while node:
            next_ = node.next 
            node.next = prev
            prev = node
            node = next_
            
        return prev
            
            
        
        
