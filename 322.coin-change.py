#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def MinimumCoins(self, coins, amount):
            # init
            n = len(coins)
            dp = [[0] * (amount+1) for _ in range(n)]

            # init oth row of table
            for T in range(amount+1):
                if T % coins[0] == 0: dp[0][T] = T // coins[0]
                else: dp[0][T] = float('inf')

            for i in range(1, n):
                for T in range(amount+1):
                    # init
                    take, nottake = float('inf'), float('inf') 

                    # not take
                    nottake = 0 + dp[i-1][T]
                    
                    # take
                    if coins[i] <= T:
                        take = 1 + dp[i][T - coins[i]]
                    
                    dp[i][T] = min(take, nottake)
            
            if dp[n-1][amount] >= int(1e9): return -1
            
            return dp[n-1][amount]
        
# @lc code=end

