# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base case
        if isBadVersion(1):
            return 1
        
        # binary search to find the last good ver and the first bad ver
        L = 1
        R = n
        while L < R:
            print(L, R)
            if L + 1 == R:
                return R
            mid = (L + R) // 2
            if (isBadVersion(mid)):
                R = mid
            else:
                L = mid