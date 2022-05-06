class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        
        # sort mat, which at the same time sorts row_nums, from weakest to strongest
        def merge_sort(mat, row_nums):
            """
            :type mat: List[List[int]]
            :type row_nums: List[int]
            :rtype: List[List[int]]         
            """
            n = len(mat)
            # base case
            if n <= 1:
                return mat, row_nums
            
            # merge sort the rows with row numbers
            left_mat, left_rownums = merge_sort(mat[:n // 2], row_nums[:n // 2])
            right_mat, right_rownums = merge_sort(mat[n // 2:], row_nums[n // 2:])
            
            return merge(left_mat, right_mat, left_rownums, right_rownums)
        
        # merge the sub mats
        def merge(left_mat, right_mat, left_rownums, right_rownums):
            """
            :type left: List[List[int]]
            :type right: List[List[int]]
            :type left_rownums: List[int]
            :type right_rownums: List[int]
            :rtype: List[List[int]]         
            """
            res_mat = []
            res_rownums = []
            
            # merge the smaller one at the beginning of two lists to res
            while len(left_mat) != 0 and len(right_mat) != 0:
                
                if left_mat[0] < right_mat[0]:
                    # left is weaker"
                    res_mat.append(left_mat[0])
                    left_mat.pop(0)
                    res_rownums.append(left_rownums[0])
                    left_rownums.pop(0)
                    
                elif left_mat[0] > right_mat[0]:
                    # right is weaker
                    res_mat.append(right_mat[0])
                    right_mat.pop(0)
                    res_rownums.append(right_rownums[0])
                    right_rownums.pop(0)
                    
                else: # left_mat[0] == right_mat[0]
                    if left_rownums[0] < right_rownums: # left is weaker
                        res_mat.append(left_mat[0])
                        left_mat.pop(0)
                        res_rownums.append(left_rownums[0])
                        left_rownums.pop(0)
                        
                    else: # right is weaker
                        res_mat.append(right_mat[0])
                        right_mat.pop(0)
                        res_rownums.append(right_rownums[0])
                        right_rownums.pop(0)
                
            # append the remaining sublist
            if len(left_mat) == 0:
                res_mat+= right_mat
                res_rownums += right_rownums 
            if len(right_mat) == 0:
                res_mat+= left_mat
                res_rownums += left_rownums 
            
            return res_mat, res_rownums
        
        # sort mat and row nums
        row_nums = list(range(len(mat)))
        sorted_mat, sorted_rownums = merge_sort(mat, row_nums)
        
        # return the first k nums in row_nums
        return sorted_rownums[:k]