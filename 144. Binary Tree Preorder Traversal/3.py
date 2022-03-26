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
        # base case
        if not root:
            return []
                
        results = []
        
        results.append(root.val)
        print(results)
        results += self.preorderTraversal(root.left)
        results += self.preorderTraversal(root.right)
            
        return results
            