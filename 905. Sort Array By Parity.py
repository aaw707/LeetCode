class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums) 
        if n == 1:
            return nums
        
        # 2 pointers
        for i in range(n - 1):
            for j in range(i + 1, n):
                
                # find nums[j] == even
                if nums[j] % 2 == 0:
                    break
                    
            # find nums[i] == odd
            if nums[i] % 2 == 1:
                
                # swap nums[i], nums[j]
                nums[i], nums[j] = nums[j], nums[i]
                continue
                
        return nums