#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
from typing import List
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = [nums[0]]

        for n in nums[1:]:
            # case: simple insert
            if n > temp[-1]:
                temp.append(n)

            # case: find insertion index & replace
            else:
                i = bisect.bisect_left(temp, n)
                temp[i] = n     
        
        return len(temp)
# @lc code=end

