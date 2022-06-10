# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # key: node
        # val: depth
        depth_cache = {}
        
        def getDiameter(root):
            """
            :type root: TreeNode
            :rtype: int, diameter of tree
            """
            # base case: leaf
            if not root.left and not root.right:
                return 0
            
            # 1 child
            if not root.left or not root.right:
                
                # start from root
                d1 = getDepth(root)
                
                # not pass root
                if not root.left:
                    d2 = getDiameter(root.right)
                    
                else: # not root.right
                    d2 = getDiameter(root.left)
                    
                return max(d1, d2)
            
            # 2 children
            # path pass root
            d1 = getDepth(root.left) + 1 + 1 + getDepth(root.right)
            # longest path at left
            d2 = getDiameter(root.left)
            # longest path at right
            d3 = getDiameter(root.right)
            
            # return longest
            #print("get diameter:", "root", root.val, "d", d1, d2, d3)
            return max(d1, d2, d3)
            
            
        def getDepth(root):
            """
            :type root: TreeNode
            :rtype: int, length of longest path from root to leaf
            """
            
            # base case: leaf
            if not root.left and not root.right:
                return 0
            
            # check cache
            if root in depth_cache:
                return depth_cache[root]
            
            # 1 child
            if not root.left:
                res = 1 + getDepth(root.right)
            elif not root.right:
                res = 1 + getDepth(root.left)
            
            # 2 children
            else:
                res = 1 + max(getDepth(root.left), getDepth(root.right))
                
            # save in cache
            depth_cache[root] = res
            return res

        # main function        
        return getDiameter(root)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                