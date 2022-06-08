class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ### check for palindrome
        # key: string
        # val: is palindrome or not
        p = {}
        
        # ### check for remove
        # # key: string
        # # val: min steps to remove until empty
        # r = {}
        
        def isPalindrome(s):
            '''
            check if a string is palindrome
            '''
            # base case: empty string
            if not s:
                return True
            
            # recursively check
            if s not in p:
                if s[0] == s[-1]:
                    p[s] = isPalindrome(s[1:-1])
                else:
                    p[s] = False
            return p[s]


        if isPalindrome(s):
            return 1
        else:
            return 2
        
        
            