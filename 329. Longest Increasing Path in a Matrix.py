class Solution(object):
    
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        
        record = {}
        
        def get_targets(i, j):
            # get the adjacent cells with increasing val
            targets = []
            locs = [
                (i - 1, j),
                (i, j - 1),
                (i, j + 1),
                (i + 1, j)
            ]
            for x, y in locs:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    targets.append((x, y))
            return targets
        
        def dfs(i, j):
            #print("i:", i, "j:", j)
            # this pos is already included in prev path
            if (i, j) in record:
                return
            # this pos has not been detected yet
            # get pos next to this pos with increasing val
            targets = get_targets(i, j)
            #print("targets:", targets)
            # no next available pos to go. path ends
            if not targets:
                # add path length to record
                record[(i, j)] = 1
                #print("record(" + str(i) + ", " + str(j) + ") = (" + str(matrix[i][j]) + ", 1)")
                return 
            # find the longest increasing path from this pos
            max_path = 0
            for x, y in targets:
                # next pos not included in prev path yet
                if (x, y) not in record:
                    # find the longest increasing path from the next pos
                    dfs(x, y)
                path = record[(x, y)]
                max_path = max(max_path, path)
                             
            # longest increasing path from this pos
            record[(i, j)] = 1 + max_path
            #print("record(" + str(i) + ", " + str(j) + ") = (" + str(matrix[i][j]) + " + " + str(max_length) + ", 1 + " + str(max_path) + ")")
        
        for i in range(m):
            for j in range(n):
                dfs(i, j)
        #print("record:")
        #for rec in record:
            #print(rec, ":", record[rec])
        max_path = 0
        for path in record.values():
            # if length >= max_length:
            #     max_length = length
            max_path = max(max_path, path)
        return max_path