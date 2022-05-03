class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        
        # base case
        if numRows == 1:
            res.append([1])
            return res
        if numRows == 2:
            res += self.generate(numRows - 1)
            res.append([1, 1])
            return res
        
        # solve recursively
        res = self.generate(numRows - 1) 
        last_row = res[-1]
        
        # place holders for the row
        row = [1] * numRows
        # fill the middle of the row with the sum of nums in prev row
        for i in range(1, numRows - 1):
            row[i] = last_row[i - 1] + last_row[i]
        # add the new row to prev rows
        res.append(row)
        return res
        