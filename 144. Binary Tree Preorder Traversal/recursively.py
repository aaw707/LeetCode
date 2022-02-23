# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
            
        results = [root.val]

        if root.left:
            results += self.preorderTraversal(root.left)
        
        if root.right:
            results += self.preorderTraversal(root.right)
            
        return results