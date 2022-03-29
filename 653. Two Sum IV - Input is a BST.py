# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        hashtable = {}
        
        queue = [root]
        
        # go through all nodes in tree
        while queue:
            node = queue.pop(0)
            
            # refer to the hash map to find sums
            if node.val in hashtable:
                return True
            else:
                remaining = k - node.val
                hashtable[remaining] = node.val
            
                # enqueue the children of node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        # no match found
        return False