# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root.left and not root.right:
            return True
        elif not root.left:
            if root.val == root.right.val:
                return self.isUnivalTree(root.right)
            else:
                return False
        elif not root.right:
            if root.val == root.left.val:
                return self.isUnivalTree(root.left)
            else:
                return False
        else:
            if root.val == root.left.val == root.right.val:
                return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            else:
                return False