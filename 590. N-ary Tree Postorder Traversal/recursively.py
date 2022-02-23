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
        
        if root.children:
            for child in root.children:
                results += self.postorder(child)
                
        results.append(root.val)
            
        return results