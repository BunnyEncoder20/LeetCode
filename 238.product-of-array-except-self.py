#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        prefix, suffix = 1,1

        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        for i in reversed(range(n)):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
        
# @lc code=end

