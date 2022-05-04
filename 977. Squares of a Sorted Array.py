class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # base cases
        # all positive
        if nums[0] >= 0:
            return [num ** 2 for num in nums]
        # all negative
        if nums[-1] < 0:
            return [num ** 2 for num in reversed(nums)]
        
        # some positive, some negative
        # find the smallest abs val
        n = len(nums)
        for idx in range(n):
            if nums[idx] >= 0:
                i = idx
                break
        
        # 2 pointers
        j = i - 1
        
        res = []
        
        # append the smaller square to res. move i to the right / j to the left
        while j >= 0 and i < n:
            i2 = nums[i] ** 2
            j2 = nums[j] ** 2
            if i2 > j2:
                res.append(j2)
                j -= 1
            elif i2 < j2:
                res.append(i2)
                i += 1
            else:
                res.append(i2)
                i += 1
                res.append(j2)
                j -= 1
        
        # check for remaining subarray
        if j >= 0:
            for num in reversed(nums[:j + 1]):
                res.append(num ** 2)
        elif i < n:
            for num in nums[i:]:
                res.append(num ** 2)
                
        return res
            
        