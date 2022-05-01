class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # for a complete staircase with i rows
        # it contains (1 + i) * i / 2 coins
        
        # need to find i, so that i * (i + 1) / 2 <= n
        # i * (i + 1) <= 2n
        # i^2 + i <= 2n
        # i^2 + i + 1/4 <= 2n + 1/4
        # (i + 1/2)^2 <= 2n + 1/4
        # i + 1/2 <= sqrt(2n + 1/4)
        # i <= sqrt(2n + 1/4) - 1/2
        
        return int(sqrt(2* n + 0.25) - 0.5)