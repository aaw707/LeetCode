# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        arr = []
        node = head
        
        # convert linkedlist to an array
        while node:
            arr.append(node.val)
            node = node.next
        
        # swap kth from front & back
        tmp = arr[k - 1]
        arr[k - 1] = arr[-k]
        arr[-k] = tmp
        
        # reconstruct linkedlist
        new_head = ListNode(arr[0])
        new_node = new_head
        for i in range(1, len(arr)):
            new_node.next = ListNode(arr[i])
            new_node = new_node.next
            
        return new_head
        