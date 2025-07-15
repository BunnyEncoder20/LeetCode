from typing import List

class Solution:
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
