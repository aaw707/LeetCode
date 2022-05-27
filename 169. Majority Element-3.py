class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore Voting Algorithm
        votes = 0
        
        for num in nums:
            
            if votes == 0:
                candidate = num
                
            if num == candidate:
                votes += 1
            else:
                votes -= 1
            
        return candidate