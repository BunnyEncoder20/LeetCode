#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
from functools import lru_cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(None)
        def recursive(i,j):
            # base case 
            if i == m-1 or j == n-1:
                return 1 
            
            # normally
            goRight = recursive(i, j+1)
            goDown = recursive(i+1, j)
            
            return goRight + goDown

        return recursive(0,0)
        
        
# @lc code=end

