#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start
from functools import cache
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))

        def bsearch(i):
            endTime = jobs[i][1]
            low,high = 0, len(jobs)-1
            while low <= high:
                mid = (low+high)//2
                if jobs[mid][0] < endTime:
                    low = mid+1
                else:
                    high = mid-1
            return low

        @cache
        def dfs(i):
            if i == len(jobs):
                return 0

            # not pick
            pick = dfs(i+1)
            
            # pick
            # finding the next non overlapping job
            j = bsearch(i)
            
            # add the profits and recursive to next job
            notpick = jobs[i][2] + dfs(j)

            return max(pick, notpick)
        
        return dfs(0)
        
# @lc code=end

