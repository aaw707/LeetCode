# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        
        sum = 0
        
        # base case
        if not root:
            return sum
        
        if root.val < low:
            sum += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            sum += self.rangeSumBST(root.left, low, high)
        else: # root val in range
            sum += root.val
            sum += self.rangeSumBST(root.left, low, high)
            sum += self.rangeSumBST(root.right, low, high)
            
        return sum