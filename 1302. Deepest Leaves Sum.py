# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        global sum_ 
        sum_ = 0
        
        def findDepth(root):
            # leaf
            if not root.left and not root.right:
                return 0
            # 1 child
            elif not root.left:
                return 1 + findDepth(root.right)
            elif not root.right:
                return 1 + findDepth(root.left)
            # 2 children
            else:
                return 1 + max(findDepth(root.left), findDepth(root.right))
            
        # find the deepest depth of tree
        depth = findDepth(root)
        
        def dfs(root, depth):
            global sum_
            
            if depth == 0: 
                sum_ += root.val
            else:
                if root.left:
                    dfs(root.left, depth - 1)
                if root.right:
                    dfs(root.right, depth - 1)
        
        # sum up the deepest leaves
        dfs(root, depth)
        return sum_