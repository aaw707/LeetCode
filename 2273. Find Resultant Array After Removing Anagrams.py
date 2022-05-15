class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        stack = []
        
        # go over each word
        for word in words:
            # if stack is empty, put word in it
            if not stack:
                stack.append(word)
                
            # stack is not empty
            else:
                # compare this word with the top of stack
                top = "".join(sorted(stack[-1]))
                sorted_word = "".join(sorted(word))
                # if they are not anagrams, put this word on stack
                if top != sorted_word:
                    stack.append(word)
                    
        return stack
                