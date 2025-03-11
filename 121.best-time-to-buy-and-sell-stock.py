#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mini = prices[0]
        maxProfit = 0
        
        for i in range(n):
          profit = prices[i] - mini
          maxProfit = max(maxProfit, profit)
          mini = min(prices[i], mini)
        
        return maxProfit
        
# @lc code=end

