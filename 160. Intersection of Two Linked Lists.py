# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        s = set()
        
        # put each node of A into a set
        A = headA
        while A:
            s.add(A)
            A = A.next
            
        # if a node in B is in set, return it as the intersection
        B = headB
        while B:
            if B in s:
                return B
            B = B.next
    
        # no intersection
        return None