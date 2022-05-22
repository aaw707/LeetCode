class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # memorization
        t = {
            "": True
        }
        
        def isPalindrome(s):
            # check hash table
            if s in t:
                return t[s]
            
            # recursively determine if s is a palindrome
            if s[0] == s[-1]:
                res = isPalindrome(s[1:-1])
                t[s] = res
            else:
                t[s] = False
            
            return t[s]
        
        n = len(s)
        res = 0
        
        # all possible substrings
        for i in range(n):
            for j in range(i + 1, n + 1):
                if isPalindrome(s[i:j]):
                    res += 1
                    
        return res