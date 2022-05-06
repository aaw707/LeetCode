class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # smallest possible a
        a = 0
        # largest possible b
        b = int(sqrt(c))
        
        while a <= b:
            
            t = a ** 2 + b ** 2
            
            if t > c:
                b -= 1
            
            elif t < c:
                a += 1
            
            else: # t == c
                return True
            
        return False
    