class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        
        # key: (i, j) starting (inclusive) & ending (inclusive) idx of nums
        # val: product
        t = {
            (0, 0): nums[0],
            (n - 1, n - 1): nums[-1]
            }
    
        # calculate products of subarrays
        for j in range(1, n - 1):
            t[(0, j)] = t[(0, j - 1)] * nums[j]
        
        for i in range(n - 2, 0, -1):
            t[(i, n - 1)] = t[(i + 1, n - 1)] * nums[i]
            
        # return arr to be filled
        arr = [0 for i in range(n)]
        
        # construct the return arr
        for i in range(n):
            # multiply left subarray and right subarray
            if i == 0:
                left = 1
            else:
                left = t[(0, i - 1)]
            if i == n - 1:
                right = 1
            else:
                right = t[(i + 1, n - 1)]
            
            arr[i] = left * right
         
        return arr
            