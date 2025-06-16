#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
from typing import List
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        destination = (n-1, m-1)
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        maxDiff_mat = [[float('inf')]*m for _ in range(n)] 
        pq = []

        def isValid(i, j):
            return (0<=i<n and 0<=j<m)


        maxDiff_mat[0][0] = 0        
        heapq.heappush(pq, (0,0,0))  # (diff, i, j)

        while pq:
            diff, i, j = heapq.heappop(pq)

            # return if destination
            if (i, j) == destination:
                return diff
            
            for di, dj in directions:
                ni, nj = i+di, j+dj

                if isValid(ni, nj):
                    currDiff = abs(heights[ni][nj] - heights[i][j])
                    newEffort = max(diff, currDiff)

                    if newEffort < maxDiff_mat[ni][nj]:
                        maxDiff_mat[ni][nj] = newEffort
                        heapq.heappush(pq, (newEffort, ni, nj))

        return -1
# @lc code=end

