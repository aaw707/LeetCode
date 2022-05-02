class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # counting backwards, if on the right of idx i exists the smallest num with idx j
        # so that nums[j] > nums[i], swap the vals of nums[i] and nums[j]
        # sort the right part of idx i ascendingly
        
        # base case
        if len(nums) == 1:
            return 
        
        min_j_val = 101 # larger than given range
        # counting backwards for each num at idx i
        for i in range(len(nums) - 1, -1, -1):
            # look for the smallest num larger than nums[i] on the right of nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    # update max_j with the idx of the current smallest nums[j]
                    if nums[j] < min_j_val:
                        min_j = j
                        min_j_val = nums[j]
            # if j found
            if min_j_val < 101:
                # swap nums at idx i and min_j
                nums[i], nums[min_j] = nums[min_j], nums[i]
                # sort everything on the right of i, ascendingly
                nums[i + 1:] = sorted(nums[i + 1:])
                # end for loop & function
                break
        # if j never found, there's no larger arrangement. return the smallest
        if min_j_val == 101:
            return nums.reverse()