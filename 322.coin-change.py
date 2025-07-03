#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from typing import List
from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache      # memo
        def recursion(i, target):
            # base case
            if i == 0:
                # if we can use the last coin to 
                # meet the target, return the no. 
                # of coins 
                if target % coins[0] == 0:
                    return target // coins[0]

                # else if not possible,
                # return very high val
                else:
                    return int(1e9)

            # do not take the coin, 
            # move to the next coin
            not_take = 0 + recursion(i-1, target)
            
            # case: we take that coin
            # casue we can take inf, we don't move pointer
            take = int(1e9)
            if coins[i] <= target:
                take = 1 + recursion(i, target-coins[i])

            # return back the minium of 
            # both situations
            return min(take, not_take)

        n = len(coins)
        res = recursion(n-1, amount)
        
        # check if target was possible
        if res == int(1e9):
            return -1
        else:
            return res
        
# @lc code=end

