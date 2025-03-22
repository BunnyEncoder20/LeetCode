#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * n
        
        for i in range(m):
            curr = [0] * n
            for j in range(n):
                if i == 0 and j == 0: 
                    curr[j] = 1
                    continue
                
                up,left = 0,0
                if i > 0: up = prev[j]
                if j > 0: left = curr[j-1]
                curr[j] = up + left
            prev[:] = curr
        
        return prev[n-1]

       
        # Combination Method (choosing down moves (m-1) from total ways (m-1 + n-1))
        # return math.comb(m+n-2, m-1)
        
        
# @lc code=end

