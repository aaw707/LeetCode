class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        def getComs(k, n, start):
            res = []
            
            # only 1 num needed
            if k == 1:
                # valid num found
                if start <= n <= 9:
                    res.append([n])
                # no valid num
                return res
            
            # out of bound
            if start > n or start > 9:
                return res
                
            # recursively find the combinations
            for i in range(start, 10):
                prev_coms = getComs(k - 1, n - i, i + 1)
                for com in prev_coms:
                    com.append(i)
                    res.append(com)                    
            return res
            
        return getComs(k, n, 1)