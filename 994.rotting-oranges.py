#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        fresh_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((0, i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        def isValid(i, j):
            return (
                0<=i<rows and 
                0<=j<cols and 
                grid[i][j] == 1
            )
        
        global_time = 0
        while q:
            t, i, j = q.popleft()
            global_time = max(global_time, t)

            for di, dj in directions:
                ni, nj = i+di, j+dj

                if isValid(ni, nj):
                    grid[ni][nj] = 2
                    fresh_count -= 1
                    q.append((t+1, ni, nj))
        
        return global_time if fresh_count==0 else -1


# @lc code=end

