class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        size = len(nums)
        min_distance = size
        
        for i in range(size):
            if nums[i] == target:
                if i >= start and min_distance == size:
                    return abs(i - start)
                else:
                    distance = abs(i - start)
                    if distance < min_distance:
                        min_distance = distance
        
        return min_distance
