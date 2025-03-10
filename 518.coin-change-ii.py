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
        
        # normally
        nottake = recursive(i-1, need)
        take = 0
        if coins[i] <= need:
          take = recursive(i, need - coins[i])
        
        return nottake + take
      
      N = len(coins)
      return recursive(N-1, amount)
        
# @lc code=end

