class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # base cases
        if target == nums[0]:
            return 0
        elif len(nums) == 1:
            return -1
        
        # find the pivot first
        L = 0
        R = len(nums) - 1
        if nums[R] > nums[L]: # not pivoted
            L = R
        else:
            while L < R:
                mid = (L + R) // 2
                print(L, R, mid)

                if nums[mid] < nums[R]:
                    R = mid
                elif nums[mid] > nums[L]:
                    L = mid
                else:
                    break # nums[mid] == nums[R] or nums[L]
        
            # after while loop, L: idx of largest num
            # return -1 if target is larger than the largest val or smaller than the smallest val
            if target > nums[L] or target < nums[L + 1]:
                return -1
                    
        # set the range of search
        if target < nums[0]:
            L = L + 1
            R = len(nums) - 1
        elif target > nums[0]:
            R = L
            L = 1
        else:
            return 0
        
        # binary search to find the idx of target
        while L <= R:
            mid = (L + R) // 2
            print(L, R, mid)
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                return mid
        
        # not found
        return -1
            
            
            