class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        pz = 0 # pointer for zeros
        pn = 0 # pointer for non-zeros
        
        while True:
            
            # proceed pz until pointing a zero
            while pz < n and nums[pz] != 0:
                pz += 1
                
            # proceed pn until pointing a non-zero
            while pn < n and nums[pn] == 0:
                pn += 1
                
            # if still in range
            if pz < n and pn < n:
                # make sure moving zeros to the end
                if pz < pn:
                    # swap the two nums
                    nums[pn], nums[pz] = nums[pz], nums[pn]
                else:
                    # looking for other non-zeros further toward the end
                    pn += 1
            # reached the end of nums
            else:
                break