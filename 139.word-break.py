#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def recursive(i):
            # base case 
            if i < 0: return True
            
            # check all words
            for word in wordDict:
                if s[i-len(word)+1 : i+1] == word and recursive(i - len(word)):
                    return True
            
            # none matched
            return False

        n = len(s)
        return recursive(n-1)
        
# @lc code=end

