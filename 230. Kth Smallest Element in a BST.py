# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        arr = []
        
        def inorder(root):
            
            # base case
            if not root:
                return -1
            
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
            return -1
        
        inorder(root)
        return arr[k - 1]