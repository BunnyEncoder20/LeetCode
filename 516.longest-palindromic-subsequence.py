#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubseq(self, s: str, t:str) -> int:
        def recursion(i, j):
            # base case
            if i<0 or j<0:
                return 0

            if s[i] == t[j]:
                return 1 + recursion(i-1, j-1)
            else:
                return max(recursion(i-1, j), recursion(i, j-1))

        l1, l2 = len(s), len(t)
        return recursion(l1-1, l2-1)

    def longestPalindromeSubseq(self, s: str) -> int:
        # Cause we looking for palindrome,
        # reversing the string and looking for
        # common subseq gives common palindromic strs
        return self.longestCommonSubseq(s, s[::-1])




# @lc code=end
