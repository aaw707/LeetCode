class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        n = len(numbers)
        
        def find_match(i, target_):
            '''
            :type i: int
            :type target_: int
            :rtype: None or int
            '''
            # binary search to find the match
            L = i + 1
            R = n - 1
            
            while L <= R:
                mid = (L + R) // 2
                #print(L, R, mid)
                if numbers[mid] < target_:
                    L = mid + 1
                elif numbers[mid] > target_:
                    R = mid - 1
                else:
                    # found
                    return mid
            
            # not found
            return None
                
            
        # for each num try to find a match
        for i in range(n):
            j = find_match(i, target - numbers[i])
            #print(i, j)
            # return the match if found it
            if j != None:
                return [i + 1, j + 1]
        