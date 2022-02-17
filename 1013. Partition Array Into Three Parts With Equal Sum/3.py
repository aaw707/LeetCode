class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        if sum(arr) % 3 != 0:
            print("not divisible by 3")
            return False
        
        average = sum(arr) / 3        
        n = len(arr)

        first_part_sum = 0
        second_part_sum = 0

        for i in range(0, n - 2):
            first_part_sum += arr[i]
            if first_part_sum == average:
           
                for j in range(i + 1, n - 1):
                    second_part_sum += arr[j]
                    
                    if second_part_sum == average:
                        return True
                
        return False

# faster than 2.py