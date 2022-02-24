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

        stack = []
        current = root

        result = TreeNode()
        pointer = result

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                pointer.right = TreeNode(val = current.val)
                pointer = pointer.right
                current = current.right
        
        return result.right

# faster than 1.py