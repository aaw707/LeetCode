# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        
        def inorderTraversal(root):
            # base case
            if not root:
                return [root]
            
            # left, root, right
            if root.left != None:
                inorderTraversal(root.left)
            res.append(root)
            if root.right:
                inorderTraversal(root.right)
        
        # res should be sorted ascendingly by inorder traversal
        inorderTraversal(root)
        
        n = len(res)
        # check if res is sorted ascendingly
        for i in range(n - 1):
            if res[i].val >= res[i + 1].val:
                return False
        
        # all checked
        return True
            
        