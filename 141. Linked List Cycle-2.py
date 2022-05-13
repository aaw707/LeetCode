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
        # base cases
        if not head or not head.next:
            return False
        
        # use a set to record each visited node
        s = set()
        # if node.next of an unvisited node is in the set, there's a circle
        while head:
            if head in s:
                return True
            else:
                s.add(head)
                head = head.next
                
        # no circle
        return False
        
        