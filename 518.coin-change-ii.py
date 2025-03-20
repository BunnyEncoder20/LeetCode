#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # init 
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n)]
        
        # init 0th row of dp table
        for T in range(amount+1):
            if T % coins[0] == 0: dp[0][T] = 1
        
        for i in range(1, n):
            for T in range(amount+1):
                pick, notpick = 0, 0
                notpick = dp[i-1][T]
                if coins[i] <= T:
                    pick = dp[i][T - coins[i]]
                dp[i][T] = pick + notpick
        
        return dp[n-1][amount]
    
            
        
# @lc code=end

