class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        d = set()
        
        for word in wordDict:
            d.add(word)
            
        # memorization
        t = {}
            
        def check(s):
            
            # base case
            if not s:
                return True
            # check hash table
            if s in t:
                return t[s]
            
            n = len(s)
            
            for i in range(n):
                if s[:i + 1] in d:
                    if check(s[i + 1:]):
                        t[s] = True
                        return t[s]
                    
            t[s] = False
            return t[s]
        
        return check(s)