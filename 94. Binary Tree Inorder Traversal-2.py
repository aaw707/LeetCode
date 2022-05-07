# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        node = root
        
        while stack or node:
            if node:
                stack.append(node)
                node = node.left 
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        
        return res
        
        