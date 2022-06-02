# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # base case: no node or 1 node
        if not head or not head.next:
            return head
        
        # divide LL into 2 unsorted queues
        Q1 = ListNode(-1)
        Q2 = ListNode(-1)
        
        P1 = Q1
        P2 = Q2 
        
        node = head
        while node:
            P1.next = node
            P1 = P1.next 
            node = node.next 
            if node:
                P2.next = node
                P2 = P2.next
                node = node.next 
        
        P1.next = None
        P2.next = None
        
        Q1 = Q1.next 
        Q2 = Q2.next 
        
        # sort 2 queues separately
        Q1_sorted = self.sortList(Q1)
        Q2_sorted = self.sortList(Q2)
        
        # merge Q1 and Q2
        new_head = ListNode(-1)
        node = new_head
        
        while Q1_sorted and Q2_sorted:
            if Q1_sorted.val < Q2_sorted.val:
                node.next = Q1_sorted
                Q1_sorted = Q1_sorted.next 
                node = node.next 
            else: # Q1_sorted.val >= Q2_sorted.val
                node.next = Q2_sorted
                Q2_sorted = Q2_sorted.next 
                node = node.next 
                
        # check for remaining Q1/Q2
        if Q1_sorted:
            node.next = Q1_sorted
        if Q2_sorted:
            node.next = Q2_sorted
        
        return new_head.next
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            