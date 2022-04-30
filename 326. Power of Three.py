class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n == int(n) and n > 1:
            n = n / 3.0

        if n == 1:
            return True
        else:
            return False