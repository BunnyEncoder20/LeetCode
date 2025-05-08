#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        time = 0
        freshOranges = 0
        q = deque()
        
        # count fresh oranges &
        # collect the rotten oranges into q
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                   q.append((0, i, j))
        
        # func to check for adj fresh orange
        def isValid(i,j):
            return (
                0 <= i < m and 
                0 <= j < n and 
                grid[i][j] == 1
            )

        # BFS
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            t, i, j = q.popleft()
            time = max(t, time)
            
            for di, dj in directions:
                newi, newj = i+di, j+dj
                if isValid(newi, newj):
                    grid[newi][newj] = 2
                    freshOranges -= 1
                    q.append((t+1, newi, newj))
        
        if freshOranges == 0:
            return time
        else:
            return -1
# @lc code=end

