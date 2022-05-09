class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        n = len(digits)
        # base case
        if n == 0:
            return []
        
        # hash table storing the chars
        t = {   
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        # put an empty string in the list to enable for loop
        prev_combinations = [""]
        
        # dp to construct the combinations
        for i in range(n):
            combinations = []
            for pc in prev_combinations:
                for c in t[digits[i]]:
                    combinations.append(pc + c)
            prev_combinations = combinations
            
        return prev_combinations