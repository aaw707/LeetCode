class Solution(object):
    # memorization of palindromes
    global p
    p = {
        "": True
    }
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        n = len(s)
        
        # base case
        if n == 0:
            return [[]]
        
        res = []
        
        # get the partitions with backtracking
        for i in range(n):
            
            if self.is_palindrome(s[:i + 1]):
                partitions = []
                backtracking = self.partition(s[i + 1:])
                if backtracking:
                    for part in backtracking:
                        partitions.append([s[:i + 1]] + part)
                    res += partitions
               
        return res
    
    # recursively decide if a string is a palindrome (with memorization)
    def is_palindrome(self, s):
        global p
        if s in p:
            return p[s]
        
        if s[0] != s[-1]:
            p[s] = False
        else:
            p[s] = self.is_palindrome(s[1:-1])
        
        return p[s]