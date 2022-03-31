# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def addValue(root):
            if root:
                values.add(root.val)
                addValue(root.left)
                addValue(root.right)
        
        values = set()
        addValue(root)
        values.remove(min(values))
        if len(values) > 0:
            return min(values)
        else:
            return -1