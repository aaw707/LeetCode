class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum_ = 0
        # use a set to store the visited sum_
        s = set()
        while n != 1:
            # get the sum of squares of digits
            while n > 0:
                digit = n % 10
                sum_ += digit * digit
                n = n // 10
            
            # if sum_ is already visited, it's an infinite loop
            if sum_ in s:
                return False
            # else, record sum_ in the set
            else:
                s.add(sum_)
            
            # start the next loop
            n = sum_
            # clear sum_
            sum_ = 0
        
        # reached 1
        return True