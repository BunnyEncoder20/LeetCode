#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      def recursive(i, need):
        # base case
        if i == 0: 
          if need % coins[i] == 0:
            return need // coins[i]
          else:
            return float('inf')

        # check dp
        if dp[i][need] != -1: return dp[i][need]
        
        # calc dp table entry
        nottake = 0 + recursive(i-1, need)
        take = float('inf')
        if coins[i] <= need:
          take = 1 + recursive(i, need - coins[i])
        
        # update dp & return
        dp[i][need] = min(take, nottake)
        return dp[i][need]
      
      n = len(coins)
      # trivial case
      if n == 0 or amount == 0: return 0
      
      # DS
      dp = [[-1]*(amount+1) for _ in range(n)]
      res = recursive(n-1, amount)
      return res if res != float('inf') else -1
# @lc code=end

