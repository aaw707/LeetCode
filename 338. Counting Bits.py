class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0] * (n + 1)
        
        # for res[i] count num of 1 in binary representation
        for i in range(n + 1):
            res[i] = bin(i)[2:].count("1")
            
        return res