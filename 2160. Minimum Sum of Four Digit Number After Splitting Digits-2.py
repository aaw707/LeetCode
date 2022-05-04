class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # sort num into ABCD, non-descendingly
        nums = list(str(num))
        nums.sort()
        
        # return AD + BC
        a = int(nums[0] + nums[3])
        b = int(nums[1] + nums[2])
        
        return a + b