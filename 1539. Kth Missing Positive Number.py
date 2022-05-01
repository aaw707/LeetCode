class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        # missing num smaller than the first num
        if k < arr[0]:
            return k
        # missing num larger than the last num
        if k > arr[-1] - len(arr):
            return k - (arr[-1] - len(arr)) + arr[-1]
        
        # missing num in the range of nums

        L = 0
        R = len(arr) - 1

        # binary search for the smallest num larger then the target num
        while L < R:
            mid = (L + R) // 2
            print("L:", L, "R:", R, "mid:", mid)
            num_missing = arr[mid] - len(arr[:mid + 1])
            
            if k < num_missing:
                R = mid
            elif k > num_missing:
                L = mid + 1
                mid = L # when while loop ends, mid points to the first num larger than kth missing num
            else:
                break
                
        # mid points to the first num larger than kth missing num
        # find and return the last missing num
        num_missing = arr[mid] - len(arr[:mid + 1])
        n = num_missing - k + 1
        
        # count backwards for the target missing num
        while n > 0 and mid > 0:
            print("n_m:", num_missing, "n:", n, "mid:", mid)
            n = n - (arr[mid] - arr[mid - 1] - 1)
            mid -= 1
        return arr[mid] - n + 1