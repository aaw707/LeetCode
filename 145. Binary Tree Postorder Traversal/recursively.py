# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        results = []
        
        if root.left:
            results += self.postorderTraversal(root.left)
            
        if root.right:
            results += self.postorderTraversal(root.right)
        
        results += [root.val]
        
        return results