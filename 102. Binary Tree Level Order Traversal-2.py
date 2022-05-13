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
        # base case
        if not root:
            return root
        
        queue = [root]
        res = [[root.val]] # first level
        
        while queue:
            
            # num of nodes in queue
            n = len(queue)
            
            # pop nodes in this level. add nodes from the next level
            for i in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # vals of nodes in queue
            level = []
            for node in queue:
                level.append(node.val)
            
            # add level's vals to res
            if level:
                res.append(level)
            
        return res
                    