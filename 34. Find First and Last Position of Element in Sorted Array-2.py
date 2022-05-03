class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        
        def find_starting_idx(l, r):
            print("finding starting")
            while l < r:
                mid = (l + r) // 2
                print(l, r, mid)
                if nums[mid] < target:
                    l = mid + 1
                else: # nums[mid] == target
                    r = mid
            return r            
            
        def find_ending_idx(l, r):
            print("finding ending")
            while l < r:
                mid = -1 * (-(l + r) // 2)
                print(l, r, mid)
                if nums[mid] > target:
                    r = mid - 1
                else: # nums[mid] == target
                    l = mid
            return l        
        
        # base case
        if len(nums) == 0:
            return [-1, -1]
        
        # 2 pointers
        L = 0
        R = len(nums) - 1
        
        # binary search for the target
        while L <= R:
            mid = (L + R) // 2
            print(L, R, mid)
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                # get the starting & ending idx from helper functions
                start = find_starting_idx(L, mid)
                if start == -1:
                    # not found
                    return [-1, -1]
                else:
                    end = find_ending_idx(mid, R)
                    return [start, end]
        # not found
        return [-1, -1]
                
            
        

                    
                    
                    
                    
                    
                
                