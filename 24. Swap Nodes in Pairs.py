# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # base case
        if head == None or head.next == None:
            return head
        
        # first 2 nodes to swap
        A = head
        B = head.next
        # recursively swap the remaining nodes
        A.next = self.swapPairs(B.next)
        B.next = A   
            
        # return new head
        return B