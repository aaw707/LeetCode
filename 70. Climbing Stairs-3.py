class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # f(n) = f(n - 1) + f(n - 2)
        first = 1
        second = 2
        
        # dp
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
            
        return second