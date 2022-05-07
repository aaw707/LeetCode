class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n1 = len(nums1)
        n2 = len(nums2)
        max_d = 0
        
        # go over each num in nums1
        for i in range(n1):
            L = i
            R = n2 - 1
            # binary search to find the furthest valid j
            while L <= R:
                j = (L + R) // 2
                if nums2[j] < nums1[i]:
                    R = j - 1
                else:
                    L = j + 1
            # update max_d
            max_d = max(max_d, L - 1 - i)
            
        return max_d
        
        

            