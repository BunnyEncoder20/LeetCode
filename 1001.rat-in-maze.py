class Solution:
    def findPath(self, grid):
        def valid(x,y):
            if (
                not (0 <= x < n) or
                not (0 <= y < n) or
                grid[x][y] == 0
            ): return False
            return True
        
        def dfs(x,y,path):
            if x == n-1 and y == n-1:
                paths.append(path)
                return 
            if not valid(x,y):
                return
            
            # if valid pos
            # mark the cell
            grid[x][y] = 0
            for dx,dy,step in directions:
                dfs(x+dx, y+dy, path+step)

            # backtracking unmark the cell
            grid[x][y] = 1
        
        # trivial cases
        n = len(grid)
        paths = []
        if not n or grid[0][0] == 0 or grid[n-1][n-1] == 0:
            return paths

        directions = [(0,1,'R'),(0,-1,'L'),(1,0,'D'),(-1,0,'U')]
        dfs(0,0,"")
        return sorted(paths)


Solution().findPath([ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ])