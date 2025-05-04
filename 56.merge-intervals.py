#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        
        for start,end in intervals:
            # if ans is empty, or 
            # starting of new interval
            if not ans or ans[-1][1] < start:
                ans.append([start, end])

            # overlapping: merge with last interval
            else:
                ans[-1][1] = max(ans[-1][1], end)
                
        return ans
            
            
        
# @lc code=end

