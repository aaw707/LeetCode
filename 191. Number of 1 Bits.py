class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # convert input from decimal to binary and split it into a list of digits
        l = [int(x) for x in str(bin(n)[2:])]
        
        return sum(l)