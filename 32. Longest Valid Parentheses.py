class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        
        stack = [-1]
        max_length = 0
        
        # go over each char
        for i in range(n):
            c = s[i]
            
            if c == '(':
                # could be part of a valid parenthesis. add onto stack
                stack.append(i)
            
            else: # stack[-1] == '(', c == ')'
                stack.pop()
                
                if not stack: 
                    stack.append(i) # next count starts from this index
                    
                else: 
                    max_length = max(max_length, i - stack[-1]) # update max length
            
        return max_length