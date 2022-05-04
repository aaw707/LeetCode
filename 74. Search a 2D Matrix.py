class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        rows = len(matrix) 
        cols = len(matrix[0])
        
        def idx_to_pos(i):
            m = i // cols
            n = i - m * cols
            return m, n
        
        L = 0
        R = rows * cols - 1
        
        while L <= R:
            mid = (L + R) // 2
            m, n = idx_to_pos(mid)
            if matrix[m][n] < target:
                L = mid + 1
            elif matrix[m][n] > target:
                R = mid - 1
            else:
                return True
            
        return False
        
        