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
        # recursively, time O(n), space O(1)
        # 2 pointers
        
        self.front_pointer = head
        
        def recursive_check(node):
            
            # if the back pointer hasn't reached the end
            if node is not None:
                
                # recursively push the back pointer one more step to the end
                if not recursive_check(node.next):
                    # if the remaining check returns false, return false
                    return False
                
                # check the front & end pointers
                if self.front_pointer.val != node.val:
                    # not palindrome
                    return False
                
                # checked. move front pointer one step forward
                self.front_pointer = self.front_pointer.next 
                
            # has reached the end of list OR has passed palindrome check for the front & back pointers
            return True
            
        return recursive_check(head)