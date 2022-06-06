class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m = len(grid)
        n = len(grid[0])
        
        # use array to represent disjointed sets
        # None: not initiated yet.
        # non-negative number: idx of root
        # negative number (< -1): number of items in the set (e.g. -3: 3 items)
        arr = [None] * (m * n)
        
        def pos_to_idx(x, y):
            return x * n + y
        
        def idx_to_pos(i):
            x = i // m
            y = i - x * m
            return x, y
        
        def union(i, j):
            # union disjointed set i with disjointed set j, with i and j as idx in representing array
            
            # find root of i
            rooti = find(i)
                
            # find root of j
            rootj = find(j)
            
            # print("rooti", rooti, "rootj", rootj)
            # print(arr)
            if arr[rooti] <= arr[rootj]: # rooti has larger tree
                # add size of rootj to rooti                
                arr[rooti] += arr[rootj]
                # make rootj point to rooti
                arr[rootj] = rooti
            
            else: # rootj has larger tree
                # add size of rooti to rootj
                arr[rootj] += arr[rooti]
                # make rooti point to rootj
                arr[rooti] = rootj
                
        def find(i):
            # find the root idx of set i, with i as idx in the representing array
            if arr[i] < 0:
                return i
            else:
                return find(arr[i])
            
               
        # num of lands
        res = 0
        
        for x in range(m):
            for y in range(n):
                
                # this is land
                if grid[x][y] == "1":
                    
                    top_i = None
                    left_i = None
                    # initiate a new disjointed set
                    i = pos_to_idx(x, y)
                    arr[i] = -1
                    
                    ### check if it belongs to detected land on top and left
                    # belongs to the land on top
                    if x - 1 >= 0 and grid[x - 1][y] == "1":
                        # idx of left land
                        top_i = pos_to_idx(x - 1, y)
                    
                    # belongs to the land on left
                    if y - 1 >= 0 and grid[x][y - 1] == "1":
                        left_i = pos_to_idx(x, y - 1)
                        
                    # print(x, y, top_i, left_i, i)
                        
                    ### connect lands 
                    # this land is not connected to detected land
                    if top_i == None and left_i == None:
                        # print("case 1")
                        arr[i] = -1 # an isolated land with area of 1
                        res += 1
                        
                    # this land is connected to the left land
                    elif top_i == None:
                        # print("case 2")
                        union(left_i, i) 
                        
                    # this land is connected to the top land
                    elif left_i == None:
                        # print("case 3")
                        union(top_i, i)  
                        
                    # this land is connected to both top and left land
                    else:
                        union(i, top_i)
                        # this land connects top and left land
                        if find(i) != find(left_i):
                            # print("case 4")
                            union(i, left_i)
                            res -= 1
                        # top and left land are already connected
                        else:
                            pass
                            # print("case 5")
                            
        
                #print(arr)
        return res