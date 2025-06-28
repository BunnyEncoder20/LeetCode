#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals according to start times
        intervals.sort()
        ans = []

        for start, end in intervals:
            
            # non overlapping
            if not ans or ans[-1][1]<start:
                ans.append([start, end])
            
            # overlapping
            else:
                ans[-1][1] = max(end, ans[-1][1])
        
        return ans

        
            
            
        
# @lc code=end

