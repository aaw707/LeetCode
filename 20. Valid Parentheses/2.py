class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # quick check by the string length
        if len(s) % 2 != 0:
            return False
        
        stack = []
        
        matches = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        for char in s:
            
            if char in matches:
                
                # char is a righty
                # check if char matches the item on top of the stack
                if stack and stack[-1] == matches[char]:
                    # matches. pop off the top item from the stack
                    stack.pop()
                else:
                    # not a match. string is invalid
                    # or stack is empty. no more item to match with char. string is invalid
                    return False  
                
            else:                
                # char is a lefty
                stack.append(char)
                
        # stack is empty i.e. everything matched        
        if stack == []:
            return True
        
        else:
            # there are items left in stack
            # string in invalid
            return False