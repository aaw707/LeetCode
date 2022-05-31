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
        
        # recursively
        new_head = self.reverseList(head.next)
        # head still pointing at the second node in the original list, the last node in the newly returned list
        head.next.next = head # attach head at the end of new list
        # remove pointer to the second last node in the new list
        head.next = None
        return new_head
            
            
        
        
