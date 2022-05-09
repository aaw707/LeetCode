# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # no child
        if not root.left and not root.right:
            return True
        # one child
        if not root.left or not root.right:
            return False
        
        # 2 children

        def inorderTraversal_LR(root):
            res = []
            if not root:
                res.append("")
                return res
            res.append(root.val)
            res += inorderTraversal_LR(root.left)
            res += inorderTraversal_LR(root.right) 
            return res
            
        def inorderTraversal_RL(root):
            res = []
            if not root:
                res.append("")
                return res
            res.append(root.val)
            res += inorderTraversal_RL(root.right)
            res += inorderTraversal_RL(root.left)
            return res
        
        left_subtree = inorderTraversal_LR(root.left)
        right_subtree = inorderTraversal_RL(root.right)
        # print(left_subtree)
        # print(right_subtree)
        return left_subtree == right_subtree        