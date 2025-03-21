#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for n in nums:
            if len(minHeap) == k:
                heapq.heappushpop(minHeap, n)
            else:
                heapq.heappush(minHeap, n)
        return minHeap[0]
                
        
        
# @lc code=end

