# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        nodes_in_order = self.inorder_traversal(root)
        
        root = nodes_in_order.pop(0)
        node = root
        
        while nodes_in_order:
            node.left = None
            node.right = nodes_in_order.pop(0)
            node = node.right            
        
        return root
        
    def inorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List
        """
        
        results = []
        
        if not root:
            return []
        
        if root.left:
            results += self.inorder_traversal(root.left)
        
        node = TreeNode(val = root.val)
        results.append(node)
        
        if root.right:
            results += self.inorder_traversal(root.right)
            
        return results
            
            