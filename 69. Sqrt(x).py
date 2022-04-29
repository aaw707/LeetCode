class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # base cases
        if x == 0 or x == 1:
            return x
        
        factor = 2
        while True:
            res = x / factor
            if res == factor:
                return factor
            elif res < factor:
                return factor - 1
            else:
                factor += 1
            