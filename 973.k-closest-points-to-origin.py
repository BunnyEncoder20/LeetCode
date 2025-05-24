#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda pt: (pt[0]**2 + pt[1]**2))
        return points[:k]
        
# @lc code=end

