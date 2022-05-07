class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        
        # base case: 
        if target == nums[0]:
            return 0
        elif n == 1:
            return -1
        
        # 2 pointers
        L = 0
        R = n - 1
        
        # find the pivot
        # case 1: not pivoted
        # [0, 1, 2, 3, 4]
        if nums[0] < nums[-1]:
            pass
        # case 2: pivoted
        # [2, 3, 4, 5, 6, 0, 1]
        else:
            # find the pivot
            while L <= R:
                if L + 1 == R:
                    largest = L
                    break
                mid = (L + R) // 2
                if nums[mid] > nums[0]:
                    L = mid
                else:
                    R = mid 
        
            # set the range of search
            if target < nums[0]:
                L = largest + 1
                R = n - 1
            else:
                L = 0
                R = largest
            
        # binary search for target
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                return mid
        
        return -1
        