#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import bisect
import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap = []    # left heap
        self.minheap = []    # right heap

    def addNum(self, num: int) -> None:
        if len(self.minheap) == len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappushpop(self.minheap, num))
        else:
            heapq.heappush(self.minheap, -heapq.heappushpop(self.maxheap, -num))

    def findMedian(self) -> float:
        # edge case
        if not self.maxheap: return 0

        # odd case 
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        # even case
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2
            

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

