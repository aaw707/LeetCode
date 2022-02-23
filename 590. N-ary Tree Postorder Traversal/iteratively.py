"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        results = []
        
        if not root:
            return results
        
        stack = [root]
        node = root
        prev = None
        
        while stack:
            
            node = stack[-1]
            
            if node.children and node.children[-1] != prev:  
                for i in range(len(node.children)):
                    index = -(i + 1)
                    stack.append(node.children[index])
                
            else:
                results.append(node.val)
                prev = stack.pop()            
            
                
        return results