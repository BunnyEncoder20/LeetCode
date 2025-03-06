#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x,y in points:
            heapq.heappush(minheap, ((x**2 + y**2), [x,y]))
        res = []
        while k:
            res.append(heapq.heappop(minheap)[1])
            k -= 1
        return res
            
        
# @lc code=end

