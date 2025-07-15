from typing import List

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        def recursion(i, buy) -> int:
            # base case
            if i == len(prices):
                return 0

            profit = 0
            if buy:
                profit = max(
                    0 + recursion(i+1, buy),
                    -prices[i] + recursion(i+1, not buy)
                )
            else:
                profit = max(
                    0 + recursion(i+1, buy),
                    +prices[i] + recursion(i+1, not buy)
                )

            return profit

        return recursion(0, True)

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
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
                    +prices[i] + recursion(i+1, 1)
                )
            dp[i][buy] = profit
            return dp[i][buy]


        n = len(prices)
        dp = [[-1]*2 for _ in range(n+1)]
        dp[n][0] = dp[n][1] = 0
        return recursion(0, True)
