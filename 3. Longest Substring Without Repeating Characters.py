class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # base case:
        if not s:
            return 0
        
        n = len(s)
        max_length = 1
        
        # 2 pointers
        i = 0
        j = 1
        
        while i <= j and j < n:
            
            if s[j] in set(s[i:j]):
                
                while s[i] != s[j]:
                    i += 1
                    # when while loop ends, s[i] == s[j]
                
                # move i one more to the left    
                i += 1
                
            # now substring only contains unique chars
            max_length = max(max_length, len(s[i:j + 1]))
            
            j += 1
                
        return max_length