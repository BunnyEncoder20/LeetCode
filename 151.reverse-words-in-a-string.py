#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s_arr = s.strip().split()
        return " ".join(s_arr[::-1])
        
# @lc code=end

