#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      @cache
      def recursive(i1, i2):
        # base case
        if i1 < 0 or i2 < 0:
          return 0
        
        # dp check
        if dp[i1][i2] != -1: return dp[i1][i2]
        
        # calc 
        if text1[i1] == text2[i2]:
          dp[i1][i2] = 1 + recursive(i1-1, i2-1)
          return dp[i1][i2]
        else:
          dp[i1][i2] = max(recursive(i1 - 1,i2), recursive(i1,i2 - 1))
          return dp[i1][i2]
      
      n,m = len(text1),len(text2)
      dp = [[-1] * m for _ in range(n)]
      return recursive(n-1, m-1)
        
# @lc code=end

