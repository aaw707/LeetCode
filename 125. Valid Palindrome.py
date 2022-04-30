class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 2 pointers moving from sides to the center
        L = 0
        R = len(s) - 1
        
        while L < R:
            # skip the non-alphanumeric chars
            while (not s[L].isdigit() and not s[L].isalpha()) and L < R:
                L += 1
            while (not s[R].isdigit() and not s[R].isalpha()) and L < R:
                R -= 1
            print(s[L], s[R])
            # compare (case-insensitive)
            if s[L].lower() == s[R].lower():
                L += 1
                R -= 1
            else:
                return False
        
        # all checked
        return True
            

                