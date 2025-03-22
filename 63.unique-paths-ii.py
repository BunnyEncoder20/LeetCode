#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, mat: List[List[int]]) -> int:
        n,m = len(mat), len(mat[0])
        prev = [0] * m
        
        for i in range(n):
            curr = [0] * m
            for j in range(m):
                # base case: dead cells
                if mat[i][j] == 1:
                    prev[j] = 0
                    continue
                
                # base case: start pos
                if i == 0 and j == 0:
                    if mat[i][j] == 0:
                        curr[j] = 1
                    else:
                        curr[j] = 0
                    continue
                
                # normally
                up, left = 0, 0
                if i > 0: up = prev[j]
                if j > 0: left = curr[j-1]
                curr[j] = up + left
            
            # update the prev row
            prev[:] = curr
        
        return prev[m-1]
        
# @lc code=end

