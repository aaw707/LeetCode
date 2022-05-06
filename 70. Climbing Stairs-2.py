class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # base case
        if n == 1:
            return 1

        # for n > 2, there are 2 possible starting points: n - 1 and n - 2
        
        # when starting at n - 1, we have ways = memo[n - 1] to reach n - 1 stairs 
        # and for each way we climb 1 more stair to reach the top
        
        
        # when starting at n - 2, we have ways = memo[n - 2] to reach n - 2 stairs
        # and for each way we climb 2 more stairs at once to reach the top
        
        # therefore, f(n) = f(n - 1) + f(n - 2), like Fibonacci number
        
        first = 1
        second = 2
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second

        # time: O(n)
        # space: O(1)