class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        res = ""
        
        for char in s:
            if char not in vowels:
                res += char
                
        return res