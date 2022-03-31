# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        if self.nodeBalanced(root):
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
        
    def getDepth(self, root):
        
        if not root:
            return 0
        else:
            return 1 + max(self.getDepth(root.left), self.getDepth(root.right))
    
    def nodeBalanced(self, root):
        return abs(self.getDepth(root.left) - self.getDepth(root.right)) <= 1