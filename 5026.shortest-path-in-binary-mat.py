from collections import deque
class Solution:
    def shortestPath(self, grid, source, destination):
        # trivial case
        if source == destination: return 0
        
        def isValid(i, j):
            '''helper func'''
            return (
                0<=i<rows and 
                0<=j<cols and 
                grid[i][j] == 1
            )


        # init config
        rows,cols = len(grid), len(grid[0])
        q = deque()     # pq not needed for unit/same wts, automatically sorted dist in q
        dist = [[float('inf')]*cols for _ in range(rows)]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]    # directions 

        # insert the src node
        si,sj = source
        dist[si][sj] = 0
        q.append((0,si,sj))
        
        # BFS
        while q:
            distance, i, j = q.popleft()

            # check all 4 directions
            for di, dj in directions:
                ni, nj = i+di, j+dj

                # if valid and distance less than previous, 
                # enque node into pq for processing
                if isValid(ni, nj) and distance+1 < dist[ni][nj]:

                    # if detination reached, return distance
                    if (ni, nj) == destination:
                        return distance+1
                    
                    # else record new distance
                    dist[ni][nj] = distance+1
                    q.append((distance+1, ni, nj))
        
        # no path found from src to destination node
        return -1
