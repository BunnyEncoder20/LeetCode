class Solution:
    def countDistinctIslands(self, grid):
        def isValid(i, j):
            return (
                0<=i<rows and 
                0<=j<cols and 
                grid[i][j] == 1
            )

        def dfs(i, j, path, base_i, base_j):
            # mark visited & add to path
            grid[i][j] = 0
            path.append((i - base_i, j - base_j))

            for di, dj in directions:
                ni,nj = i+di, j+dj
                if isValid(ni, nj):
                    dfs(ni,nj,path,base_i, base_j)

        rows, cols = len(grid), len(grid[0])
        distinct_shapes = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # found new island

                    path = []
                    dfs(i,j,path,i,j)

                    # save shape of island 
                    # (sort to cancel our dfs travel path randomness)
                    distinct_shapes.add(tuple(sorted(path)))

        return len(distinct_shapes)


n = Solution().countDistinctIslands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1],[0, 0, 0, 1, 1]])
print(n)
# output 1