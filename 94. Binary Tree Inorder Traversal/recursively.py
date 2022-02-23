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
        
        results = []
        
        if not root:
            return results
        
        if root.left:
            results += self.inorderTraversal(root.left)
        
        results += [root.val]
        
        if root.right:
            results += self.inorderTraversal(root.right)
            
        return results
        