class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)

        # L[i]: the product of all nums on the left of nums[i]
        L = [0] * n
        # R[i]: the product of all nums on the right of nums[i]
        R = [0] * n
        # arr to be returned
        res = [0] * n
        
        # extremes
        L[0] = 1
        R[-1] = 1
        
        for i in range(1, n):
            L[i] = L[i - 1] * nums[i - 1]
        
        for j in range(n - 2, -1, -1):
            R[j] = R[j + 1] * nums[j + 1]
            
        for k in range(n):
            res[k] = L[k] * R[k]
        
        # print(L)
        # print(R)
        return res