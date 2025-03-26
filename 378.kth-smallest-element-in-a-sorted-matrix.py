#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        
        # Insert first col elements into heap
        # pushing (val, row, col)
        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        
        # extract the smallest K elements
        val = None
        for _ in range(k):
            val, r, c = heapq.heappop(heap)
            if c+1 < n:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))

        return val
                
        
        
        
# @lc code=end

