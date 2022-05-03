class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # at least: 0 value >= x
        # at most: n values >= x
        
        for n in range(len(nums) + 1):
            count = 0
            for num in nums:
                if num >= n:
                    count += 1
            if count == n:
                return n
        
        # not found
        return -1
    
        # time: O(n^2)
        # space: O(1)