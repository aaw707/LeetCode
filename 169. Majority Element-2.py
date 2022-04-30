class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Boyer-Moore Voting Algorithm
        # time: O(n)
        # space: O(1)
        
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate
            
