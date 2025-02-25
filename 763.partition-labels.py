#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mpp = {}
        res = []
        for i,ch in enumerate(s):
            mpp[ch] = i
        
        end = mpp[s[0]]
        start = 0
        for i in range(len(s)):
            end = max(end, mpp[s[i]])
            if i == end:
                res.append(end-start+1)
                if i+1 < len(s):
                    start = i+1 
                    end = mpp[s[start]]
        return res
                
            
# @lc code=end

