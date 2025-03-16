#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # O(n) space aprroach
        res = []
        for i in range(n):
            xi = nums[i]
            yi = nums[i+n]
            res.append(xi)
            res.append(yi)
        return res
        
# @lc code=end

