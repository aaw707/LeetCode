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
        # first run: find the max depth
        def find_max_depth(root):
            # no child: leaf
            if not root.left and not root.right:
                return 1
            # 1 child
            if not root.left:
                return 1 + find_max_depth(root.right)
            if not root.right:
                return 1 + find_max_depth(root.left)
            # 2 children
            return 1 + max(find_max_depth(root.left), find_max_depth(root.right))
        
        max_depth = find_max_depth(root)
        
        
        # second run: find the sum of nodes at max depth
        sum_ = 0
        def addup_deepest_nodes(root, remaining_depth):           
            
            if not root:
                return 0
            
            # reached leaf
            if remaining_depth == 1:
                return root.val

            return addup_deepest_nodes(root.right, remaining_depth - 1) + addup_deepest_nodes(root.left, remaining_depth - 1)
            
        sum_ = addup_deepest_nodes(root, max_depth)
        return sum_
                
                