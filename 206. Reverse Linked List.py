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
        if not head or not head.next:
            return head
        
        # brutal force
        prev = head
        node = head.next
        while node.next:
            prev = prev.next 
            node = node.next
        # node is tail, prev is the node before tail
        prev.next = None
        node.next = self.reverseList(head)
        return node