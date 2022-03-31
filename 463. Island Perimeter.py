class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        peri = 0
        
        if len(grid) == 0 or len(grid[0]) == 0:
            return peri
        
        # loop over each cell
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                # if cell is land
                if grid[i][j] == 1:
                    peri += 4
                    
                    if i > 0 and grid[i - 1][j] == 1:
                        peri -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        peri -= 2
                    
        return peri
                    