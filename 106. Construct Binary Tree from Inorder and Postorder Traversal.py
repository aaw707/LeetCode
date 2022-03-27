# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        # null spot
        if not postorder:
            return None
        
        root = TreeNode(postorder.pop())
        
        # order list is empty after popping the root
        if not postorder:
            return root
        
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                root.left = self.buildTree(inorder[:i], postorder[:i])
                root.right = self.buildTree(inorder[i + 1:], postorder[i:])
                break
        return root