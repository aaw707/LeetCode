class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # convert to binary and count the occurrence of 1
        return bin(n).count('1')