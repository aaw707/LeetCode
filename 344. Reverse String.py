class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        L = 0
        R = len(s) - 1
        
        # using O(1) space
        while L < R:
            tmp = s[L]
            s[L] = s[R]
            s[R] = tmp
            
            L += 1
            R -= 1