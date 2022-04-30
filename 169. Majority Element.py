class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        t = {}
        for num in nums:
            if num in t:
                t[num] += 1
                if t[num] > len(nums) / 2:
                    return num                
            else:
                t[num] = 1