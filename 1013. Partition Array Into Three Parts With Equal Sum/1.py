class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        
        for i in range(0, n - 2):
            for j in range(i + 2, n):
                
                part_one = sum(arr[:i + 1])
                part_two = sum(arr[i + 1 : j])
                
                if part_one != part_two:
                    continue
                else:
                    part_three = sum(arr[j:])
                    if part_one != part_three:
                        continue
                    else:
                        return True
        return False

# too slow