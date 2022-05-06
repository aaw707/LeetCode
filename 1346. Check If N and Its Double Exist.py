class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        s = set()
        
        for i in range(n):
            num = arr[i]
            if num in s:
                return True
            else:
                s.add(num * 2)
                s.add(num / 2.0)
        
        return False