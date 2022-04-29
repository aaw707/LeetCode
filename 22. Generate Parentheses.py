class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        stack = []
        
        def backtracking(num_open, num_close):
            
            # n open and n close parenthesis have been added. end the branch and add it to res
            if num_open == num_close == n:
                res.append("".join(stack))
                return
            
            # case 1: add left parenthesis if possible 
            if num_open < n:
                stack.append("(")
                backtracking(num_open + 1, num_close)
                # the result through the above back tracking has been recorded
                # remove the left parenthesis we just added, to try the other case
                stack.pop()
                
            # case 2: add right parenthesis if possible
            if num_close < num_open:
                stack.append(")")
                backtracking(num_open, num_close + 1)
                # the result through the above back tracking has been recorded
                # remove the right parenthesis we just added, to clean up
                stack.pop()
                
        backtracking(0, 0)
        return res