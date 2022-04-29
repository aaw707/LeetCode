class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 2 pointers
        L = 0
        R = 0
        # length of strings
        h = len(haystack)
        n = len(needle)
        
        for i in range(h):
            if haystack[i] == needle[0]:
                # idx exceed string length. not found
                if i + n > h:
                    return -1
                # check the rest of needle
                count = n - 1
                for j in range(1, n):
                    if haystack[i + j] == needle[j]:
                        count -= 1
                    else:
                        break
                # all letters checked. needle found
                if count == 0:
                    return i
                # not all letters match. keep looking
                else:
                    i = i + n
        
        # not found
        return -1