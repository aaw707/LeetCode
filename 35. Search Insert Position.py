class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 2 pointers
        L = 0
        R = len(nums) - 1

        # binary search to find the num / pos to insert
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                return mid
        
        return L