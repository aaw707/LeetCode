class Solution(object):
    # use a hash table to cache results
    global t
    t = {}
    
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        global t
        # base cases
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # if n in hash table, take the cached value
        if n in t:
            return t[n]
        else:
            # recursively calculate the value
            t[n] = self.fib(n - 1) + self.fib (n - 2)
            return t[n]