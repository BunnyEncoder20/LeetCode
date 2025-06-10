#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        vis = [[0]*cols for _ in range(rows)]
        dist = [[0]*cols for _ in range(rows)]
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()

        # find the zero cells and enque
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j,0))   # (x,y,steps)
                    vis[i][j] = 1       # mark
        
        # bfs 
        while q:
            row,col,steps = q.popleft()
            dist[row][col] = steps      # save distance

            # checkk neighbouring cells
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if (
                    0<=nr<rows and 
                    0<=nc<cols and 
                    not vis[nr][nc]
                ):
                    vis[nr][nc] = 1
                    q.append((nr, nc, steps+1))
        
        return dist
            

        
# @lc code=end

