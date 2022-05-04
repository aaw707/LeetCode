class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def find_start_idx(l, r, n):
            # nums[l] <= n
            # nums[r] == n
            while l < r:
                mid = (l + r) // 2
                print("find start idx")
                print(l, r, mid, n)
                if nums[mid] < n:
                    l = mid + 1
                else: # nums[mid] == n
                    r = mid
            return l
        
        
        # sort nums
        nums = sorted(nums)
        
        for n in range(len(nums) + 1):
            if n < nums[0]:
                count = len(nums)
            elif n > nums[-1]:
                count = 0
            else:
                # binary search: find the idx of num >= n
                L = 0
                R = len(nums) - 1
                while L <= R:
                    mid = (L + R) // 2
                    print(L, R, mid, n)
                    if nums[mid] > n:
                        R = mid - 1
                    elif nums[mid] < n:
                        L = mid + 1
                    else: # nums[mid] == n
                        # find the left most num = n
                        L = find_start_idx(L, mid, n)
                        print("L:", L)
                        break
                        
                # L: the idx of num >= n
                count = len(nums) - L

            # check if the number of remaining nums = n
            if count == n:
                return n
        
        # not found
        return -1