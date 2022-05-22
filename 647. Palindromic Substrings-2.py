class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        global n
        n = len(s)
        
        def checkPalindromes(i, j):
            # i, j are idx of center character(s)
            global n            
            res = 0
            while i >= 0 and j < n and s[i] == s[j]:
                res += 1
                i -= 1
                j += 1
            return res                
                
        res = 0
        
        # each char as the center, expand towards both sides
        for i in range(n):
            # odd palindromes
            res += checkPalindromes(i, i)
            # even palindromes
            res += checkPalindromes(i, i + 1)
            
        return res