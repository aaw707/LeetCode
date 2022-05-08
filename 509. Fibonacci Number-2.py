class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base case
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # dp
        first = 0
        second = 1
        for i in range(2, n + 1):
            third = first + second
            first = second
            second = third
            
        return second