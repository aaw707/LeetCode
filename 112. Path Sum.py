# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        # base case
        if not root:
            return False
        
        targetSum -= root.val
        if targetSum == 0 and not root.left and not root.right:
            return True
        else:
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
