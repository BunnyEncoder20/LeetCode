#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        curr_digit = nums.pop()
        subPermutations = self.permute(nums)

        res = []
        for p in subPermutations:
            for i in range(len(p)+1):
                new_permu = p[:i] + [curr_digit] + p[i:]
                res.append(new_permu)
        
        return res

        
        
# @lc code=end

