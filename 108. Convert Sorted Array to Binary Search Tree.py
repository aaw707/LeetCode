# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if not nums:
            return None
        
        length = len(nums)
        
        if length == 1:
            return TreeNode(nums[0])
        else:
            # take the middle num to be the root
            root_idx = length // 2
            root = TreeNode(nums[root_idx])
            # left part to be the left child
            root.left = self.sortedArrayToBST(nums[:root_idx])
            # right part to be the right child
            root.right = self.sortedArrayToBST(nums[root_idx + 1:])
            
            return root