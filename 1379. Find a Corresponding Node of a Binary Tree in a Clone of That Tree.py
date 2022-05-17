# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        # base case. root is the target
        if target == original:
            return cloned
        
        # reached end of tree
        if not original:
            return None
        
        # search left subtree
        left_res = self.getTargetCopy(original.left, cloned.left, target)
        # if found, return left subtree
        if left_res:
            return left_res
        
        # if not found in left subtree, search right subtree
        right_res = self.getTargetCopy(original.right, cloned.right, target)
        return right_res 