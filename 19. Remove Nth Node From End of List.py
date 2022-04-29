# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # base case
        if head.next == None:
            return None
        
        # 2 pointers
        node1 = head
        distance = n
        # keep a distance of 2
        while distance > 0:
            node1 = node1.next
            distance -= 1
        node2 = head
        
        # node 1 already at the end. remove the first node (last node counting backwards)
        if node1 == None:
            return head.next
        # go through the list until node1 reaches the end
        while node1.next != None:
            node1 = node1.next
            node2 = node2.next
        
        # remove nth node (backwards) at node2.next
        node2.next = node2.next.next
        return head
        