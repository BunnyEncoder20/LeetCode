from typing import List

class Solution1:
    def maxProfit(self, arr: List[int]) -> int:
            def recursion(i, canBuy, cap):
                # base case
                if cap == 0 or i == n:
                    return 0

                profit = 0
                if canBuy:
                    profit = max(
                        -arr[i] + recursion(i+1, False, cap),
                        0 + recursion(i+1, True, cap)
                    )
                else:
                    profit = max(
                        +arr[i] + recursion(i+1, True, cap-1),
                        0 + recursion(i+1, False, cap)
                    )
                return profit

            n = len(arr)
            return recursion(0, True, 2)


class Solution2:
    def stockBuySell(self, arr, n):
        def recursion(i, canBuy, cap):
            # base case
            if cap == 0 or i == n:
                return 0

            # check dp
            if dp[i][canBuy][cap] != -1:
                return dp[i][canBuy][cap]


            if canBuy:
                dp[i][canBuy][cap] = max(
                    -arr[i] + recursion(i+1, False, cap),
                    0 + recursion(i+1, True, cap)
                )
            else:
                dp[i][canBuy][cap] = max(
                    +arr[i] + recursion(i+1, True, cap-1),
                    0 + recursion(i+1, False, cap)
                )

            return dp[i][canBuy][cap]

        n = len(arr)
        if n == 0: return 0
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        return recursion(0, True, 2)
