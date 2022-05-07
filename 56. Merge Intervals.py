class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res = []
        
        start = -1
        end = -1
        
        for interval in intervals:
            if interval[0] > end: # start a new interval
                res.append(interval)
                start = interval[0]
                end = interval[1]
                
            else: # overlap with the perv interval
                end = max(interval[-1], end)
                res[-1][1] = end
                
        return res
                