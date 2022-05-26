class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        nums_set = set(nums)
        
        for num in nums_set:
            
            # num is the smallest num in the streak contains it
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1
                
                # find the rest of nums in this streak consecutively
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1
                    
                # update the longest streak
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
        