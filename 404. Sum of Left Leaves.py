# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # root is null
        if not root:
            return 0
        
        # root has no left child
        if not root.left:
            return self.sumOfLeftLeaves(root.right)
        
        # root has left child
        else:
            left_child = root.left
            
            # left child is leaf
            if not left_child.left and not left_child.right:
                return left_child.val + self.sumOfLeftLeaves(root.right)
            
            # left child is not leaf
            else:
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
                
        
        