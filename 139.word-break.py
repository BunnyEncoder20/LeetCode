#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        
        for i in range(n):
            for word in wordDict:
                # i not of length of wordDict word
                if i < len(word)-1: continue
                
                if i == len(word)-1 or dp[i-len(word)]:
                    if s[i - len(word)+1 : i+1] == word:
                        dp[i] = True
                        break
            
        return dp[n-1]
        
# @lc code=end

