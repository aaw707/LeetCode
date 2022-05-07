class Solution(object):
    global t
    t = {}
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # for each pos on the top row: 1 way to reach (move to right only)
        if m == 1: # only 1 row
            return 1
        
        # for each pos on the left most column: 1 way to reach (move down only)
        if n == 1: # only 1 col
            return 1     
        
        # check cached res
        global t
        key = str(m) + "," + str(n)
        if key in t:
            return t[key]
                
        # for every other pos: can be reached from the top pos down, or from left pos to the right
        # ways = ways to reach the pos above + ways to reach the pos on the left
        res = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        t[key] = res
        return res
        