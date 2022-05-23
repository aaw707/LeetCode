class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        
        def counting(s):
            c = [0, 0]
            n = len(s)
            # count the num of zeroes and ones in s
            for i in range(n):
                c[int(s[i])] += 1
            return c
            
        
        for s in strs:
            counts = counting(s)
            # fill the dp matrix backwards
            for zeros in range(m, counts[0] - 1, -1):
                for ones in range(n, counts[1] - 1, -1):
                    dp[zeros][ones] = max(1 + dp[zeros - counts[0]][ones - counts[1]], dp[zeros][ones])
            
        return dp[m][n]
            
            