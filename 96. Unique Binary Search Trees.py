class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # array to record dp
        G = [0 for i in range(n + 2)]
        
        G[0] = 1
        G[1] = 1
        
        # self.numTrees(i)
        for i in range(2, n + 1): 
            # take each num in range(n) as the root
            for j in range(1, i + 1): 
                # left subtree = numTrees(j - 1)
                # right subtree = numTrees(range(j + 1,  i + 1)), equivalent to numTrees(i - j)
                # dp
                G[i] += G[j - 1] * G[i - j] 
                
        return G[n]
        