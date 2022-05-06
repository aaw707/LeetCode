class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # base case
        if n <= 1:
            return matrix
        
        start = 0
        end = n - 1
        
        # rotate layer by layer, from outer to inner
        while end > start:
            # for each element on one outer side 
            # (operate on 1 side to change 4 sides together)
            for x in range(0, end - start):
                matrix[start][start + x], matrix[start + x][end], matrix[end][end - x], matrix[end - x][start] = matrix[end - x][start], matrix[start][start + x], matrix[start + x][end], matrix[end][end - x]

            # rotate the inner cells iteratively
            start += 1
            end -= 1
        