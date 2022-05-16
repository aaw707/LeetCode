class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # base case
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        locs = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1), 
            (0, 1),
            (1, -1),
            (1, 0), 
            (1, 1)
        ]
        
        # helper function: find the neighbours of a given cell
        def get_neighbours(i, j):
            for row_difference, col_difference in locs:
                row = i + row_difference
                col = j + col_difference
                
                # idx out of bound OR not valid path
                if not (0 <= row < n and 0 <= col < n) or grid[row][col] != 0:
                    continue
                
                # found valid neighbour
                yield (row, col)
                    
        # queue with starting point
        queue = [(0, 0)]
        # starting distance
        grid[0][0] = 1
        
        while queue:
            i, j = queue.pop(0)
            distance = grid[i][j]
            # reached end
            if i == j == n - 1:
                return distance
            for neighbour_row, neighbour_col in get_neighbours(i, j):
                grid[neighbour_row][neighbour_col] = distance + 1 # only the neighbours originally == 0
                queue.append((neighbour_row, neighbour_col))
            
        # not found
        return -1
                
        
        
            