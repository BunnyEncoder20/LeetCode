#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # trivial case
        n = len(nums)
        if n == 0 or k > n: return -1
        
        heap = []
        
        # first k element pushed into heap
        for num in nums[:k]:
            heapq.heappush(heap, num)
        
        print(heap)
        
        # remaing elements
        for num in nums[k:]:
            heapq.heappushpop(heap, num)
        
        print(heap)
        
        # check for same nums 
        if k == 1:
            return heap[0] if len(heap) == 1 else -1
        
        return heap[0]
        
        
        
        
               
                
        
        
# @lc code=end


