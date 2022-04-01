# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def bst(root):
            
            if root:
                values.add(root.val)
                bst(root.left)
                bst(root.right)
                
        values = set()
        # add all values to root
        bst(root)
        # sort values
        sorted_values = sorted(values)
        
        # find min difference
        min_diff = sorted_values[-1] - sorted_values[0]
        for i in range(len(values) - 1):
            diff = sorted_values[i + 1] - sorted_values[i]
            min_diff = min(min_diff, diff)
        return min_diff
        
            