"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        results = []
        
        if not root:
            return results
        
        stack = [root]
        
        while stack:
            
            node = stack.pop()
            
            if node:
                results.append(node.val)
                
                for i in range(len(node.children)):
                    index = -(i + 1)
                    stack.append(node.children[index])
                    
        return results
                    
                    
                    