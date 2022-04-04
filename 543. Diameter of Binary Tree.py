# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def getDiameter(root):
            # null
            if not root:
                return 0
            # leaf
            elif not root.left and not root.right:
                return 0
            # have one child
            elif not root.left or not root.right:
                return getDepth(root) - 1
            # have both children
            else: 
                return getDepth(root.left) + getDepth(root.right) 
        
        def getDepth(root):
            if not root:
                return 0
            else:
                return 1 + max(getDepth(root.left), getDepth(root.right))
        
        if not root:
            return 0
        else:
            return max(getDiameter(root), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        