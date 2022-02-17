class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        # loop over each character in string
        for char in s:
            
            # if char is a lefty
            if char in ("(", "{", "["):
                # add it on top of the stack
                stack.append(char)
            
            # if char is a righty
            else:
                
                # check if it matches with the top item on the stack
                try:
                    top_item = stack.pop()
                    
                except IndexError as e:
                    # no more item left in the stack to match with char
                    # string is invalid
                    return False
                
                if (top_item == "(" and char == ")") or (top_item == "[" and char == "]") or (top_item == "{" and char == "}"):
                    # top item matches with char
                    # proceeds to the next char in string
                    continue
                
                else:
                    # top item doesn't match with char
                    # string is invalid
                    return False
            
        # no more char left in string
        if stack == []:
            # all parentheses match
            return True
        else:
            # there are lefties left in the stack
            # string is invalid
            return False