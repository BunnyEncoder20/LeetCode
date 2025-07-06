#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''a^a = 0 | a^0 = a'''
        xor = 0
        for n in nums:
            xor ^= n
        return xor
        
# @lc code=end

