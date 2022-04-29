# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # base cases
        # both lists are null
        if not list1 and not list2:
            return None
        # one list is null
        if not list1:
            return list2
        if not list2:
            return list1
        
        # both list1 and list2 are not null
        # put the smaller head val at the beginning, and recursively construct the rest of the list
        if list1.val > list2.val:
            root = ListNode(list2.val)
            root.next = self.mergeTwoLists(list1, list2.next)
        elif list1.val < list2.val:
            root = ListNode(list1.val)
            root.next = self.mergeTwoLists(list1.next, list2)
        else:
            root = ListNode(list1.val)
            root.next = ListNode(list2.val)
            root.next.next = self.mergeTwoLists(list1.next, list2.next)
        
        return root