class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if length of 2 strings are not the same, they are not anagrams
        if len(s) != len(t):
            return False
        
        # use a hash table 
        h = {}
        # store each char & frequency of s into hash table
        for c in s:
            if c not in h:
                h[c] = 1
            else:
                h[c] += 1
        
        # check each char & frequency of t against hash table
        for c in t:
            if c not in h:
                return False
            else:
                h[c] -= 1
                # if all frequency has been found, pop the key
                if h[c] == 0:
                    h.pop(c)
        # if s and t are anagrams, the hash table should be empty
        return not h