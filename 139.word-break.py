#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        
        # if we at end of s, it's true
        dp[n] = True

        # iterate from back of s
        for i in range(n,-1,-1):
            # check if word matching s[i:word]

            for word in wordDict:
                # check s[i:word] has enough chars for word
                if (
                    i+len(word) <= len(s) and 
                    s[i:i+len(word)] == word
                ):
                    dp[i] = dp[i + len(word)]

                # if we found a word break, 
                # we can move on to next idx,
                if dp[i]:
                    break
        
        # if we were able to word break entire s,
        # dp[0] would be True
        return dp[0]
        
# @lc code=end

