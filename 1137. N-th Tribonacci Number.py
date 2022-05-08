class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base case
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        first = 0
        second = 1
        third = 1
        
        # dp
        for i in range(3, n + 1):
            fourth = first + second + third
            first = second
            second = third
            third = fourth
            
        return third