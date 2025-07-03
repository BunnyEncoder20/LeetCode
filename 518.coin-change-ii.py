#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
from functools import cache, lru_cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def recursion(i, target):
            # base case 
            if i == 0:
                if target % coins[0] == 0:
                    return 1
                else:
                    return 0
            
            # init
            pick, not_pick = 0, 0

            # case we do not pick coin
            not_pick = recursion(i-1, target)

            # case we pick coin
            if coins[i] <= target:
                pick = recursion(i, target-coins[i])
            
            # return sum of total ways
            return pick + not_pick

        n = len(coins)
        res = recursion(n-1, amount)
        if res != int(1e9):
            return res
        else:
            return 0
    
            
        
# @lc code=end

