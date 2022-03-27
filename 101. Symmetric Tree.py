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
        
        # base case
        if not root.left and not root.right:
            return True
        
        if self.left_level_order(root.left) == self.right_level_order(root.right):
            return True
        else:
            return False
        
        
        
        
    def left_level_order(self, root):
        
        results = []
        
        # base case
        if not root:
            return results
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node == None:
                results.append(None)
            else:
                results.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        print("left:", results)
        return results     
        
        
    def right_level_order(self, root):
        
        results = []
        
        # base case
        if not root:
            return results
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node == None:
                results.append(None)
            else:
                results.append(node.val)
                queue.append(node.right)
                queue.append(node.left)
        
        print("right:", results)
        return results
        
        