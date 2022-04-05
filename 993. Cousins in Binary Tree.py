# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        # depth / parent of x, y
        global dx, dy, px, py
        dx, dy, px, py = 0, 0, 0, 0
        
        def findNums(root, depth, parent):
            global dx, dy, px, py
            
            if root:
                if root.val == x:
                    dx = depth
                    px = parent
                if root.val == y:
                    dy = depth
                    py = parent
                
                findNums(root.left, depth + 1, root.val)
                findNums(root.right, depth + 1, root.val)
                
        findNums(root, 0, None)
        if dx == dy and px != py:
            return True
        else:
            return False