"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # base case
        if not root:
            return root
        
        queue = [root]
        
        # use queue to present each row of nodes
        while queue:
            n = len(queue)
            # set pointers for nodes in this level
            for i in range(n - 1):
                queue[i].next = queue[i + 1]
            # pop nodes in this level. add nodes in next level
            for i in range(n):
                node = queue.pop(0)
                # skip the loc with no child
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root