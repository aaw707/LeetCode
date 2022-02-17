class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        size = len(nums)

        # walk towards both directions from start
        # to the left
        i = start
        # to the right
        j = start

        while True:
            # since It is guaranteed that target exists in nums
            # the while loop will end when target is found

            if i >= 0 and nums[i] == target:
                return start - i
                
            if j < size and nums[j] == target:
                return j - start

            i -= 1
            j += 1
    
# faster than 1.py