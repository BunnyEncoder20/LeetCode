#
# @lc app=leetcode id=3165 lang=python3
#
# [3165] Maximum Sum of Subsequence With Non-adjacent Elements
#

# @lc code=start
class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        ans = 0
        for pos,val in queries:
            nums[pos] = val
            ans += self.nonAdjacent(nums)
        return ans

    def nonAdjacent(self, nums):
        def recursive(i):
            # base case
            if i == 0: return nums[i]
            if i < 0: return 0
            if dp[i] != None: return dp[i]

            # pick the index (cannot take the adj i) 
            pick = nums[i] + recursive(i-2)

            # not picking index (can take the next i)
            notpick = 0 + recursive(i-1)
            
            dp[i] = max(pick, notpick)
            return dp[i]
        
        n = len(nums)
        dp = [None]*(n+1)
        return recursive(n-1)
        
        
# @lc code=end

