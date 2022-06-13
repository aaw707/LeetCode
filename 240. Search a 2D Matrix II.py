class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m = len(matrix)
        n = len(matrix[0])
         
        # base cases: out of range
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        # exclude the bottom rows where matrix[i][0] > target
        T = 0
        B = m - 1
        while T <= B:
            mid = (T + B) // 2
            if matrix[mid][0] < target:
                T = mid + 1
            elif matrix[mid][0] > target:
                B = mid - 1
            else:
                return True # found
        
        if matrix[B][0] < target:
            bottom_row = B
        else:
            bottom_row = B - 1
        # print("bottom_row", bottom_row)
                  
        # exclude the top rows where matrix[i][n - 1] < target
        T = 0
        B = bottom_row
        while T <= B:
            mid = (T + B) // 2
            if matrix[mid][-1] < target:
                T = mid + 1
            elif matrix[mid][-1] > target:
                B = mid - 1
            else:
                return True # found
        
        if matrix[T][-1] < target:
            top_row = T + 1
        else:
            top_row = T
        # print("top_row", top_row)
        
        # binary search each remaining row
        row = top_row
        L = 0
        R = n - 1
        while row <= bottom_row:
            while L <= R:
                mid = (L + R) // 2
                # print(L, R, mid, row, target, matrix[row][mid])
                if matrix[row][mid] < target:
                    L = mid + 1
                elif matrix[row][mid] > target:
                    R = mid - 1
                else:
                    return True # found
            # not found in this row
            # reset pointers
            L = 0
            # search range for the next row: 0 to R (R + 1), since matrix[row][j] > matrix[row + 1][j]
            if matrix[row][R] < target:
                R = R + 1
            else:
                R = R
            # continue for the next row
            row += 1
            
        # doesn't exist
        return False
            
            