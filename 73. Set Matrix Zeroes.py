class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        # in the first col
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break       
                
        # in the first row
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # go over each cell (excluding the first col/row)
        for i in range(1, m):
            for j in range(1, n):
                # if this cell == 0
                if matrix[i][j] == 0:
                    # flag the beginning of the row/col
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # check the flags on each row
        for i in range(1, m):
            # if the row is flagged as 0
            if matrix[i][0] == 0:
                # set each cell to zero
                for j in range(1, n):
                    matrix[i][j] = 0
              
        # check the flags on each col
        for j in range(1, n):
            # if the col is flagged as 0
            if matrix[0][j] == 0:
                # set each cell to 0
                for i in range(1, m):
                    matrix[i][j] = 0
                    
        # set the first col
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
        # set the first row
        if first_row_zero:
            for j in range(n):
                 matrix[0][j] = 0
                    