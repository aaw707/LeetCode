class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def bSearch(L, num):
            R = len(numbers) - 1
            while L <= R:
                mid = (L + R) // 2
                if numbers[mid] < num:
                    L = mid + 1
                elif numbers[mid] > num:
                    R = mid - 1
                # if found:
                else:
                    # return idx
                    return mid            

            # if not found:
            return -1
        
        n = len(numbers)
        
        # go over every num in numbers
        for i in range(n):
            
            # find target - numbers[i] in numbers via binary search
            res = bSearch(i + 1, target - numbers[i])
            
            # if found
            if res != -1:
                # return
                return [i + 1, res + 1]
            
            # if not found
            else:
                # continue
                continue
                
                
                
            