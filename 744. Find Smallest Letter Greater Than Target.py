class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # base cases
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        
        # 2 pointer
        L = 0
        R = len(letters) - 1
        
        while L <= R:
            mid = int((L + R) / 2)
            print("L:", L, "R:", R, "mid:", mid)
            if letters[mid] < target:
                L = mid + 1
            elif letters[mid] > target:
                if L == R:
                    return letters[mid]
                else:
                    R = mid
            
            else: 
                # letters[mid] == target               
                while mid < len(letters) - 1 and letters[mid] == letters[mid + 1]:
                    print("mid:", mid)
                    mid += 1
                        
                # return the next larger item       
                if mid != len(letters) - 1:
                    return letters[mid + 1]
                # letters[mid] is the last item. return the first item instead   
                else:   
                    return letters[-1]
                    