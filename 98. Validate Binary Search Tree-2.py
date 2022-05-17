# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # base case: only 1 node
        if not root.left and not root.right:
            return True
        
        # check valid bst with range (exclusive)
        def validBSTwithRange(root, lower, upper):
            
            # validate root
            if not lower < root.val < upper:
                return False
                
            # base case: 1 node only
            if not root.left and not root.right:
                return True
            
            # 1 child
            if not root.left:
                if root.val > root.right.val:
                    return False
                else:
                    return validBSTwithRange(root.right, root.val, upper)
            if not root.right:
                if root.val < root.left.val:
                    return False
                else:
                    return validBSTwithRange(root.left, lower, root.val)
             
            # 2 children
            if not root.left.val < root.val < root.right.val:
                return False
            else:
                return validBSTwithRange(root.right, root.val, upper) and validBSTwithRange(root.left, lower, root.val)
            
        return validBSTwithRange(root, float('-inf'), float('inf'))
                