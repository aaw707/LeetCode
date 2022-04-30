class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # bit operation
        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res