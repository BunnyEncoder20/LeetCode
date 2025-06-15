from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])

        # trivial case: src or destination node blocked
        if grid[0][0] == 1 and grid[n-1][m-1] == 1: return -1

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        dist = [[float('inf')]*m for _ in range(n)]
        q = deque()
        
        def isValid(i, j):
            '''func to check if cell valid path cell'''
            return (
                0<=i<n and 
                0<=j<m and 
                grid[i][j] == 0
            )
        
        # enque src ndoe
        dist[0][0] = 1
        q.append((1,0,0))

        # BFS grid
        while q:
            distance, i, j = q.popleft()
            
            # check if reached destination
            if i == n-1 and j == m-1:
                return distance

            for di, dj in directions:
                ni, nj = i+di, j+dj 
                if isValid(ni, nj) and distance + 1 < dist[ni][nj]:
                    dist[ni][nj] = distance + 1
                    q.append((distance+1, ni, nj))
        
        # path not found
        return -1

print(Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))