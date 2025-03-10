#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1),len(s2)
        if n > m: return False
        
        s1fpp = Counter(s1)
        window_fpp = Counter(s2[:n])
        
        # check first window elements
        if s1fpp == window_fpp: return True
        
        for i in range(n,m):
            chfront = s2[i]
            chback = s2[i-n]
            
            window_fpp[chfront] += 1
            window_fpp[chback] -= 1
            
            # remove ch with counts = 0
            if window_fpp[chback] == 0:
                del window_fpp[chback]
            
            if s1fpp == window_fpp: return True
        
        return False
            
# @lc code=end

