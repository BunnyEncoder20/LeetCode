#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxlength = 0

        for num in hashset:
            if num-1 in hashset:
                continue
            
            l = 1
            lastnum = num
            while lastnum+1 in hashset:
                l += 1
                lastnum += 1
            maxlength = max(maxlength, l)
        
        return maxlength


        
# @lc code=end

