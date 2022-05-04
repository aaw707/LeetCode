class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # sort num into ABCD, non-descendingly
        nums = [int(x) for x in str(num)]
        nums.sort()
        
        # return AD + BC
        a = nums[0] * 10 + nums[3]
        b = nums[1] * 10 + nums[2]
        
        return a + b