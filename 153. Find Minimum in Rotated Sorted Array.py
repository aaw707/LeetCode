class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # base case: rotated n times OR only 1 num in nums
        if nums[0] <= nums[-1]:
            return nums[0]
        
        L = 0
        R = n - 1
        
        # binary search to find the largest idx
        while L < R:
            if L + 1 == R:
                break
            mid = (L + R) // 2
            if nums[mid] > nums[0]:
                L = mid
            else:
                R = mid
                
        return nums[R]