#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(i) for i in range(1,n+1)]
        permus = list(permutations(digits))
        return "".join(permus[k-1])
        
# @lc code=end

