# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # base case
        if not root:
            return 0
        
        max_depth = 1
        
        if not root.left and not root.right:
            return max_depth
        
        max_depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + max_depth
        return max_depth