class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        n_floors = top - bottom + 1
        n_specials = len(special)
        
        # base case: all floors are special
        if n_floors <= n_specials:
            return 0
        
        # sort specials
        special.sort()
        
        # from bottom to first special
        start = bottom
        finish = special[0]
        max_floors = finish - start
        start = special[0]
        
        # check each intervel of special floors
        for i in range(1, n_specials):
            finish = special[i]
            floors = finish - start - 1
            max_floors = max(max_floors, floors)
            start = finish
            
        # from last special to top
        # after the for loop, start = finish = special[-1]
        finish = top
        floors = finish - start
        max_floors = max(max_floors, floors)
        
        # return 
        return max_floors
            
        
        