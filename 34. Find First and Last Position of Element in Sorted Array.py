class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def find_starting_pos(l, r):
            # nums in the range of l to r can only be <= target
            while l <= r:
                if nums[l] == target:
                    return l
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] == target:
                    r = m
                else:
                    print("ERROR in find_starting_pos")
                    
        
        def find_ending_pos(l, r):
            # nums in the range of l to r can only be >= target
            while l <= r:
                if nums[r] == target:
                    return r
                m = (l + r) // 2 + 1
                if nums[m] > target:
                    r = m - 1
                elif nums[m] == target:
                    l = m
                else:
                    print("ERROR in find_ending_pos")
                    
            
        L = 0
        R = len(nums) - 1
        
        # binary search to find idx
        while L <= R:
            mid = (L + R) // 2
            
            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] < target:
                L = mid + 1
            else:
                # nums[mid] == target. find starting & ending idx separately
                starting_pos = find_starting_pos(L, mid)
                ending_pos = find_ending_pos(mid, R)
                return [starting_pos, ending_pos]
        # not found
        return [-1, -1]
            

                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                