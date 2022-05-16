class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        t = {}
        n = len(keyboard)
        # put keyboard into a hash table
        for i in range(n):
            t[keyboard[i]] = i
            
        # ref word to the hash table
        res = 0
        start = 0
        for char in word:
            res += abs(t[char] - start)
            start = t[char]
        return res
            