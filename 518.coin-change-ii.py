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
        prev = [0] * (amount+1)
        curr = [0] * (amount+1)
        
        # init 0th row of dp table
        for T in range(amount+1):
            if T % coins[0] == 0: prev[T] = 1
        
        for i in range(1, n):
            for T in range(amount+1):
                pick, notpick = 0, 0
                notpick = prev[T]
                if coins[i] <= T:
                    pick = curr[T - coins[i]]
                curr[T] = pick + notpick
            prev[:] = curr
        
        return prev[amount]
    
            
        
# @lc code=end

