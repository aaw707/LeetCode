class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # since after taking nums[i], we remove all nums[i] + 1 and nums[i] - 1
        # the remaining nums[i] will not be deleted in the future
        # so everytime we take one nums[i], we can take all the rest nums with the same value
        
        # use a hashtable to store nums, grouping the duplicates
        # key: num, val: sum of nums with the same value
        t = {}
        for num in nums:
            if num in t:
                t[num] += num
            else:
                t[num] = num
        # print("t:", t)
        
        # base cases
        n = len(t)
        if n == 0:
            return 0
        if n == 1:
            return t[nums[0]]
                
        max_ = max(nums)
        min_ = min(nums)
        
        # key: consider num in nums with values in range 0-n
        # val: the maximum sum we can get from it
        cache = {}
        cache[0] = 0 # when only considering 0s in nums, no matter how many 0s we take, the sum is 0
        cache[min_] = t[min_] # when only considering 1s and 0s, take 1s for a larger sum
        
        def maxPoint(n):
            # consider num in nums between 0 and n (inclusive)
            if n < 0:
                return 0
            if n in cache:
                return cache[n]
            if n not in t:
                return maxPoint(n - 1)
            
            # take the last num
            gain = t[n]
            g1 = gain + maxPoint(n - 2)

            # not take the last num 
            g2 = maxPoint(n - 1)
            
            return max(g1, g2)

        for i in range(2, max_ + 1):
            cache[i] = maxPoint(i)
        # print("cache:", cache)
        
        return cache[max_]
    