class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        strs = s.split()
        res = ["" for x in strs]
        for str_ in strs:
            position = int(str_[-1])
            res[position - 1] = str_[:-1]
        return " ".join(res)