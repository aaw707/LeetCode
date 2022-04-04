# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        s = ""
        decimalNums = []
        
        def dfs(root, s):
            """
            root: TreeNode
            s: string, binary number of ancestors on the path down
            return: no return values as the function opeartes on global variables
            """
            # ancestor path + root value
            s = s + str(root.val)
            # conver to decimal num if leaf
            if not root.left and not root.right:
                num = int(s, 2)
                # append to list
                decimalNums.append(num)
            
            if root.left:
                dfs(root.left, s)
            if root.right:
                dfs(root.right, s)
                
        dfs(root, s)
        return sum(decimalNums)

        # faster