class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # group duplicate nums into t
        t = {}
        for num in nums:
            if num in t:
                t[num] += num
            else:
                t[num] = num
                
        # base cases
        n = len(t)
        if n == 1:
            return t[nums[0]]
        
        # list of keys (sorted)
        keys = sorted(t)
        
        # min and max in nums
        min_ = keys[0]
        max_ = keys[-1]
        
        # only consider num in nums with val between 0 to n
        first = 0 # 0 to 0
        second = t[min_] # 0 to min_
        
        for i in range(1, n): # for each key in t, excluding the smallest one
            
            # take current num
            gain = t[keys[i]]
            
            # best decision
            # if current num == prev num + 1, skip the prev num while taking the current num
            if keys[i] - 1 == keys[i - 1]:
                third = max(first + gain, second) # take, not take
            else:
                third = gain + second
                
            # move over
            first = second
            second = third
        
        return second
