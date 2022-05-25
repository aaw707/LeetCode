# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        n = len(inorder)
        
        # base case
        if n == 0:
            return None
        
        root = TreeNode(preorder[0])
        
        # leaf
        if n == 1:
            return root
        
        # determine the inorder of left/right subtrees
        for i in range(n):
            if inorder[i] == root.val:
                inorder_left = inorder[:i]
                n_left = len(inorder_left)
                inorder_right = inorder[i + 1:]
                break
                
        # determine the preorder of left/right subtrees
        preorder_left = preorder[1:1 + n_left]
        preorder_right = preorder[1 + n_left:]
        
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root