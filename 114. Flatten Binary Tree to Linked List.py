# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def helper(root):
            # base case
            if not root:
                return None
            
            # take out subtrees
            left_subtree = root.left
            right_subtree = root.right
            
            root.left = None
            # add flattened left subtree to the right
            root.right = helper(left_subtree)
            # traverse to the end of new tree
            node = root
            while node.right:
                node = node.right
            # add flattened right subtree to the right
            node.right = helper(right_subtree)
            
            # flattened
            return root
        
        # flatten in-place
        helper(root)