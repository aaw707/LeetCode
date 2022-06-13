class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        
        i = 0
        j = 0
        
        s = set()
        score = 0
        max_score = 0
        
        while i < n:
            # keep moving i to the right until encounter a value already met
            if nums[i] not in s:
                s.add(nums[i])
                score += nums[i]
                
            else: # met a not unique value
                
                # update max score if needed
                max_score = max(max_score, score)
                
                # shrink j from left
                while j <= i:
                    if nums[j] != nums[i]:
                        s.remove(nums[j])
                        score -= nums[j]
                        j += 1
                    else:
                        j += 1
                        break
            
            i += 1
            
        max_score = max(max_score, score)            
        return max_score
                        
                        
                        
                    
            
            
        