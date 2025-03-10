#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def getPermu(s):
            if s == "":
                return [""]
            curr = s[0]
            nextPermus = getPermu(s[1:])
            currPermus = set()
            for p in nextPermus:
                for i in range(len(p)+1):
                    currPermus.add(p[:i] + curr + p[i:])
                    
            return nextPermus + [p for p in currPermus]
            
        permutations = getPermu(s1)
        for p in permutations:
            if p in s2: return True
        return False
# @lc code=end

