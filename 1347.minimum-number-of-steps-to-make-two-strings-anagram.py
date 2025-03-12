#
# @lc app=leetcode id=1347 lang=python3
#
# [1347] Minimum Number of Steps to Make Two Strings Anagram
#

# @lc code=start
from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        f1 = Counter(s)
        f2 = Counter(t)
        changes = 0
        for c in f1:
            if f1[c] > f2[c]:
                changes += f1[c] - f2[c]
        return changes
            
        
# @lc code=end

