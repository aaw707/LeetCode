class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        # loop the digits backwards
        for i in range(len(digits) - 1, -1, -1):
            # need to carry 1 to the next digit
            if digits[i] + carry >= 10:
                digits[i] = digits[i] + carry - 10
                carry = 1
            # no need to carry. add 1 and end the function
            else:
                digits[i] += 1
                return digits
        
        # carry = 1
        return [1] + digits