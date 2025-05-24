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
            distance = x**2 + y**2
            heapq.heappush(minheap, (distance, x, y))
        ans = []
        while k:
            distance, x, y = heapq.heappop(minheap)
            ans.append([x,y])
            k -= 1
        return ans
# @lc code=end

