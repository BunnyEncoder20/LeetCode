#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        ans = []
        
        for i in range(n):
            start,end = intervals[i]
            
            # if the interval lies within previous 
            # (current end < previous interval end)
            if len(ans)>0 and end <= ans[-1][1]: continue

            # Overlapping intervals
            for j in range(i+1, n):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
                else:
                    break
            ans.append([start, end])
        return ans
            
            
        
# @lc code=end

