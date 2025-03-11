#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
      def recursive(i,j):
        k = i+j
        # base case 
        if k == len(s3):
          return i == len(s1) and j == len(s2)
        
        # dp check
        if dp[i][j] != -1: return dp[i][j]
        
        # normally
        dp[i][j] = False
        # if ch of s1 mathcing s3
        if i < len(s1) and s1[i] == s3[k] and recursive(i+1, j):
          dp[i][j] = True
        
        # if ch of s2 mathcing s3
        if j < len(s2) and s2[j] == s3[k] and recursive(i, j+1):
          dp[i][j] = True
        
        # not matching (or above failed)
        return dp[i][j]
          
      # trivial case
      n,m = len(s1),len(s2)
      if n + m != len(s3): return False
      dp = [[-1] * (m+1) for _ in range(n+1)]
      return recursive(0,0)
        
        
# @lc code=end

