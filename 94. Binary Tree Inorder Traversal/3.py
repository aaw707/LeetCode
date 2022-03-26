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
        
        # base case
        if not root:
            return []
        
        results = []
        
        results += self.inorderTraversal(root.left)
        results.append(root.val)
        results += self.inorderTraversal(root.right)
        
        return results