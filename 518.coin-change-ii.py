#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
from functools import lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @lru_cache(None)
        def recursive(i, need):
            # base case 
            if i == 0: 
                if need % coins[0] == 0:
                    return 1 
                else:
                    return 0
            
            # normally
            pick, notpick = 0, 0
            
            # notpick 
            notpick = recursive(i-1, need)
            
            # pick
            if coins[i] <= need:
                pick = recursive(i, need - coins[i])
            
            return pick + notpick

        n = len(coins)
        return recursive(n-1, amount)
            
        
# @lc code=end

