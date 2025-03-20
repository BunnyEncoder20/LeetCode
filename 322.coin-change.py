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
            prev = [0] * (amount+1)
            curr = [0] * (amount+1)

            # init oth row of table
            for T in range(amount+1):
                if T % coins[0] == 0: prev[T] = T // coins[0]
                else: prev[T] = float('inf')

            for i in range(1, n):
                for T in range(amount+1):
                    # init
                    take, nottake = float('inf'), None

                    # not take
                    nottake = 0 + prev[T]
                    
                    # take
                    if coins[i] <= T:
                        take = 1 + curr[T - coins[i]]
                    
                    curr[T] = min(take, nottake)
            
            ans = prev[amount]
            if ans >= int(1e9): return -1
            
            return ans
        
# @lc code=end

