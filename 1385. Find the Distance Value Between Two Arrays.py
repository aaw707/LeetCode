class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        # sort arr2 for better processing
        arr2 = sorted(arr2)
        # num to return
        count = 0
        # for each num in arr1
        for m in arr1:
            count += 1
            # for each num in arr2
            for n in arr2:
                # if distance value > d, don't count it
                if abs(m - n) <= d:
                    count -= 1
                    break
        return count