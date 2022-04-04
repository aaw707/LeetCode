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
        
        def getBinaryNums(root):
            """
            :type root: TreeNode
            :rtype: list of strings (binary nums)
            """

            # leaf
            if not root.left and not root.right:
                return [str(root.val)]

            # not leaf
            elif not root.left: # 1 child
                subtreeNums = getBinaryNums(root.right)
            elif not root.right: # 1 child
                subtreeNums = getBinaryNums(root.left)
            else: # 2 children
                subtreeNums = getBinaryNums(root.left) + getBinaryNums(root.right)
            
            # append root value to the end of list 
            newSubtreeNums = []
            for subtreeNum in subtreeNums:
                newSubtreeNums.append(str(root.val) + subtreeNum)
            return newSubtreeNums
        
        # list of strs 
        binaryNums = getBinaryNums(root)
        print("")
        print("binaryNums:", binaryNums)
        decimalNums = []
        for binaryNum in binaryNums:
            # convert to decimal nums
            decimalNums.append(int(binaryNum, 2))
        print("binaryNums after operation:", decimalNums)
            
        return sum(decimalNums)