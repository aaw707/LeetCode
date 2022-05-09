# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # no child
        if not root.left and not root.right:
            return True
        # one child
        if not root.left or not root.right:
            return False
        
        # 2 children
        # check if the 2 children at symmetric positions are symmetric
        def checkChildren(child1, child2):
            if not child1 and not child2:
                return True
            if not child1 or not child2:
                return False
            if child1.val != child2.val:
                return False
            return checkChildren(child1.left, child2.right) and checkChildren(child1.right, child2.left)
        
        return checkChildren(root.left, root.right)