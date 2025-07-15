from typing import List

class Solution2:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def recursion(i, buy) -> int:
            # base case
            if i == n:
                return 0

            if dp[i][buy] != -1: return dp[i][buy]

            profit = 0
            if buy:
                profit = max(
                    0 + recursion(i+1, 1),
                    -prices[i] + recursion(i+1, 0)
                )
            else:
                profit = max(
                    0 + recursion(i+1, 0),
                    +prices[i] - fee + recursion(i+1, 1)    # only things that changed from buy-sell-stock-II
                )
            dp[i][buy] = profit
            return dp[i][buy]


        n = len(prices)
        dp = [[-1]*2 for _ in range(n+1)]
        dp[n][0] = dp[n][1] = 0
        return recursion(0, True)
