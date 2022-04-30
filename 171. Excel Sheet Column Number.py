class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        res = 0
        
        # go over each char
        while columnTitle:
            res *= 26
            c = columnTitle[0]
            columnTitle = columnTitle[1:]
            res += ord(c) - 64
        return res