class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        
        ### consider the matrix as an array with increasing elements
        
        # helper function 
        def idx_to_val(idx):
            i = idx // n
            j = idx - i * n
            return matrix[i][j]
        
        # 2 pointers binary search
        L = 0
        R = m * n - 1
        while L <= R:
            mid = (L + R) // 2
            val = idx_to_val(mid)
            if val < target:
                L = mid + 1
            elif val > target:
                R = mid - 1
            else:
                return True
        
        return False