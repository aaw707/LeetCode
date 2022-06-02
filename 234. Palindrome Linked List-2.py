# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # time: O(n), space O(n)
        
        vals = []
        
        while head:
            vals.append(head.val)
            head = head.next
        
        return vals == vals[::-1]