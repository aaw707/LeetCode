class Solution(object):
    
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def backtracking(n, last_char): # last_char: the num representing the last vowel char in the sorted string (0-4)
            res = 0
            if n == 1:
                res += 5 - last_char
            else: # n > 1
                for i in range(last_char, 5):
                    res += backtracking(n - 1, i)
            return res
        
        return backtracking(n, 0)