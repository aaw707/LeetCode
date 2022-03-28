# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        seq1 = self.findLeaves(root1)
        seq2 = self.findLeaves(root2)
        
        return seq1 == seq2
        
        
    def findLeaves(self, root):
        
        seq = []
        
        
        # root is null
        if not root:
            return seq
        
        # root is leaf
        elif not root.left and not root.right:
            seq.append(root.val)
        
        # root has left child
        elif not root.right:
            seq = self.findLeaves(root.left)
            
        # root has right child
        elif not root.left:
            seq = self.findLeaves(root.right)
            
        # root has 2 children
        else:
            seq  = self.findLeaves(root.left) + self.findLeaves(root.right)
            
        return seq