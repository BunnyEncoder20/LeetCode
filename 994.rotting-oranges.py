#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
      n,m = len(grid), len(grid[0])
      directions = [(0,1), (1,0), (-1,0), (0,-1)]
      fresh = 0
      time = 0

      # DS req
      q = deque()

      # traverse and collect all rotten oranges
      for i in range(n):
          for j in range(m):
              # count fresh oranges
              if grid[i][j] == 1:
                  fresh += 1

              # if rotten, push into rotten queue
              if grid[i][j] == 2:
                  q.append((0,i,j))
      
      # chk of valid cell
      def isValid(i,j):
          return 0 <= i < n and 0 <= j < m and grid[i][j] == 1

      # BFS loop
      while(q):
          t, row, col = q.popleft()
          time = max(time, t)
          
          # checkout all neighbours
          for dr, dc in directions:
              nrow, ncol = row+dr, col+dc

              # if fresh orange found
              if isValid(nrow, ncol):
                  grid[nrow][ncol] = 2    # mark
                  fresh -= 1              # reduce
                  q.append((t+1, nrow, ncol))
      
      # return time if no more fresh oranges left 
      return -1 if fresh>0 else time
      
      # fresh_count = 0, all oranges converted
      return time if fresh_count == 0 else -1 

        
        
        
# @lc code=end

