#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def recursive(i):
            # base case
            if i == 0: return nums[0]
            if i < 0: return 0

            # check memo
            if dp[i] != -1:
                return dp[i]

            # pick
            pick = nums[i] + recursive(i-2)

            # not pick
            notpick = 0 + recursive(i-1)

            dp[i] = max(pick, notpick)
            return dp[i]

        n = len(nums)
        dp = [-1]*n
        return recursive(n-1)


# @lc code=end

# Test cases
if __name__ == '__main__':
    solver = Solution()
    tests = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([], 0),
        ([10], 10),
        ([2, 1], 2),
        ([1, 2], 2),
        ([0, 0, 0, 0], 0),
        ([2, 1, 1, 2], 4),
        ([5, 5, 5, 5, 5], 15),
        ([10, 1, 10, 1, 10], 30)
    ]

    for i, (nums, expected) in enumerate(tests):
        output = solver.rob(nums)
        status = "Passed" if output == expected else "Failed"
        print(f"testcase{i+1}: {nums} | {output} | {expected} | {status}")

