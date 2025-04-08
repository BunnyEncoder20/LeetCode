#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.cap = k  
        for n in nums:
            if len(self.heap) != self.cap:
                heapq.heappush(self.heap, n)
            else:
                heapq.heappushpop(self.heap, n)

    def add(self, val: int) -> int:
        if len(self.heap) < self.cap:
            heapq.heappush(self.heap, val)
            if len(self.heap) == self.cap: return self.heap[0]
            else: return None
        else:
            heapq.heappushpop(self.heap, val)
            return self.heap[0]
            
       


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

