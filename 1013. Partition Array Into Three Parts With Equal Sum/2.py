class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        average = sum(arr) / 3

        # quick check: if the average is int
        if average != int(average):
            return False
        
        n = len(arr)
        for i in range(0, n - 2):
            part_one = sum(arr[:i + 1])
            if part_one == average:
            
                for j in range(i + 2, n):
                    part_two = sum(arr[i + 1 : j])
                    
                    if part_two == average:
                        return True
                
        return False


# faster than 1.py