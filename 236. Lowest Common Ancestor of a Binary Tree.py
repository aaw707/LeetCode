# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.res = None
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        def traverse(node):
            
            # base case
            if not node:
                return False
            
            left = traverse(node.left)
            right = traverse(node.right)
            mid = (node == p) or (node == q)
            
            if left + right + mid >= 2:
                self.res = node
            
            return mid or left or right
        
        traverse(root)
        return self.res
            