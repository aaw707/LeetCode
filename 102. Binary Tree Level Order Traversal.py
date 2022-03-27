# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        results = []
        
        # base case
        if not root:
            return results
        
        queue = [root]
        num = 1
        next_level_num = 0
        
        while queue:
            level = []
            while num > 0:
                node = queue.pop(0)
                num -= 1
                
                if node.left:
                    queue.append(node.left)                    
                    next_level_num += 1
                if node.right:
                    queue.append(node.right)                  
                    next_level_num += 1
                
                level.append(node.val)
                
            results.append(level)
            num = next_level_num
            next_level_num = 0
            
        return results
            
                    
        