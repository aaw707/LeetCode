class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        
        n = len(nums)
        
        # 2 pointers
        L = 0
        R = n - 1
        
        # sum of all elements from idx 0 to L
        sum_ = 0
        # move L to the right until the sum of 0 to L - 1 >= x
        while L < n and sum_ < x:
            #print(L, nums[L], sum_)
            sum_ += nums[L]
            L += 1
        # removing all elements can't reduce x to 0
        if L > n:
            return -1
        
        min_steps = float('inf')
        
        # resize the array on both directions to try out min stels
        while L <= R + 1 and L >= 0:
            #print(L, R, sum_)
            
            # succeeded removal
            if sum_ == x:
                # update min steps
                min_steps = min(min_steps, L + n - R - 1)
                # keep checking other possibilities
                sum_ -= nums[L - 1]
                L -= 1
                
                
            elif sum_ > x:
                if L == 0:
                    break # no more num remaining on the left
                else:
                    sum_ -= nums[L - 1]
                    L -= 1 
            
            else: # sum < x
                R -= 1
                sum_ += nums[R + 1]
        
        # failed
        if min_steps == float('inf'):
            return -1
        # found
        else:
            return min_steps
                
            
            
            
            
            
            
            
            