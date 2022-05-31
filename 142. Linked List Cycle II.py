# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # base case
        if not head:
            return None
        
        s = set()
        
        # use set to check if the next node is already seen
        while head:
            if head.next in s:
                return head.next 
            s.add(head)
            head = head.next 
        
        return None