class Solution(object):
    # hash table for ref
    t = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # base cases
        if not s:
            return 0
        if len(s) == 1:
            return self.t[s]
        
        # special cases: 2 letters to 1 number
        if s[-2] == "I":
            if s[-1] == "V":
                last_digit = 4
                return self.romanToInt(s[:-2]) + last_digit
            elif s[-1] == "X":
                last_digit = 9
                return self.romanToInt(s[:-2]) + last_digit
        elif s[-2] == "X":
            if s[-1] == "L":
                last_digit = 40
                return self.romanToInt(s[:-2]) + last_digit
            elif s[-1] == "C":
                last_digit = 90
                return self.romanToInt(s[:-2]) + last_digit
        elif s[-2] == "C":
            if s[-1] == "D":
                last_digit = 400
                return self.romanToInt(s[:-2]) + last_digit
            elif s[-1] == "M":
                last_digit = 900
                return self.romanToInt(s[:-2]) + last_digit
        
        # 1 letter to 1 number 
        return self.romanToInt(s[:-1]) + self.t[s[-1]]
        
        