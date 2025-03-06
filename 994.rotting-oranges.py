#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isValid(i,j):
            '''helper func'''
            return (
                0 <= i < rows and 
                0 <= j < cols and
                grid[i][j] == 1
            )
            
        # init
        fresh = 0
        q = deque([])
        rows,cols = len(grid),len(grid[0])
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        total_time = 0
        # count fresh | collect rotten
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((0,i,j))
        
        # BFS 
        while q:
            time,x,y = q.popleft()
            total_time = max(total_time, time)
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if isValid(nx,ny):
                    grid[nx][ny] = 2
                    fresh -= 1
                    q.append((time+1, nx, ny))
        
        return -1 if fresh>0 else total_time

        
        
        
# @lc code=end

