class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        counts = [0] * 101 # range: 0-100
        
        # get counts for each num
        for num in nums:
            counts[num] += 1
        
        # update each idx to number of nums < num
        carry = counts[0]
        counts[0] = 0
        # for count in counts
        for i in range(1, 101):
            tmp = counts[i]
            counts[i] = carry
            carry = tmp + carry
        
        # for num in nums, get the number of nums < num from counts
        for j in range(n):
            nums[j] = counts[nums[j]]
            
        return nums
            
            