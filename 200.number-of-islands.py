#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if ((0 <= r < rows) and (0 <= c < cols) and grid[r][c] == "1"):
                grid[r][c] = "0"
                for dr,dc in directions:
                    dfs(r+dr, c+dc)
        
        if not grid: return 0
        rows,cols = len(grid),len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count += 1
        return count
        
        
# @lc code=end

