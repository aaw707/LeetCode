# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack = []
        results = []
        node = root
        prev = None
        
        while stack or node:
            
            if node:
                stack.append(node)
                node = node.left
            
            # return to the last node that has unprocessed right child
            elif stack[-1].right and stack[-1].right != prev:
                node = stack[-1].right
                
            # either right child has been processed or no right chil
            else:
                prev = stack.pop()
                results.append(prev.val)
        
        return results
            