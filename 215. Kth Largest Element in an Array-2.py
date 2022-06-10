class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def mergeSort(nums):
            n = len(nums)
            
            # base case
            if n <= 1:
                return nums
            
            # divide and conquer
            mid = n // 2
            q1 = mergeSort(nums[:mid])
            q2 = mergeSort(nums[mid:])
            
            # merge
            q = []
            while q1 and q2:
                if q1[0] < q2[0]:
                    q.append(q1.pop(0))
                else:
                    q.append(q2.pop(0))
            
            # check for remaining
            if q1:
                q += q1
            if q2:
                q += q2
            
            return q
        
        nums = mergeSort(nums)
        return nums[-k]