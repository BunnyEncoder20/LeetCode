#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
      def recursive(i, need):
        # base case
        if i == 0:
          if need % coins[i] == 0:
            return 1
          else:
            return 0
        # dp check
        if dp[i][need] != -1: return dp[i][need]

        # calc dp entry
        nottake = recursive(i-1, need)
        take = 0
        if coins[i] <= need:
          take = recursive(i, need - coins[i])
        
        dp[i][need] = nottake + take
        return dp[i][need]
      
      N = len(coins)
      dp = [[-1]*(amount+1) for _ in range(N)]
      return recursive(N-1, amount)
        
# @lc code=end

