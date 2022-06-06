class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        # if rotate n times, give the original array
        k = k % n
        
        # helper array in rotating
        tmp = [None for i in range(n)]
        
        # rotate each num
        for i in range(n):
            
            # target pos for rotating this num
            target = (i + k) % n  
            
            # these pos will be overwritten - save them in tmp
            if i < n - k:
                # save the original value in the pos to be over-written
                tmp[target] = nums[target]
            
            # this pos has not been over-written
            if tmp[i] == None:
                # rotate this num to the target pos
                nums[target] = nums[i]
            
            # this pos has been overwritten
            else:
                # take original value from tmp and put into target pos
                nums[target] = tmp[i]
                

                