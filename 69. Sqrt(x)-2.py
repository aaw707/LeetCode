class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # base cases
        if x == 0 or x == 1:
            return x
        
        # binary search to find the sqrt
        low = 0
        high = x
        while low < high:
            mid = (low + high) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                high = mid
            else:
                low = mid + 1
        
        return low - 1
            
        # time: O(logn)
        # space: O(1)