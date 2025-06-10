#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#

# @lc code=start
from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        vis = [[0]*cols for _ in range(rows)]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        # find all boundry nodes and enque
        for i in range(rows):
            for j in range(cols):
                if (
                    i == 0 or i == rows-1 or
                    j == 0 or j == cols-1
                ):
                    if grid[i][j] == 1:
                        vis[i][j] = 1
                        q.append((i,j))
        
        # bfs the collected nodes
        while q:
            i,j = q.popleft()
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if (
                    0<=ni<rows and 
                    0<=nj<cols and 
                    grid[ni][nj] == 1 and 
                    not vis[ni][nj]
                ):
                    vis[ni][nj] = 1
                    q.append((ni,nj))
        
        # check the remaining land cells
        num_enclaves = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not vis[i][j]:
                    num_enclaves += 1
        
        return num_enclaves
                
# @lc code=end

