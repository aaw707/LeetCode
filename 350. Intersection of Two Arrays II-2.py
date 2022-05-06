class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1= len(nums1)
        n2 = len(nums2)
        
        if n1 > n2:
            return self.intersect(nums2, nums1)
        
        # nums1 is shorter than or equal length to nums2        
        nums1.sort()
        nums2.sort()
        
        res = []
        i = 0
        j = 0
        
        # 2 pointers to find the intesections
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
            
        return res
            