#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
from heapq import heappop, heappush, heappushpop
class MedianFinder:

    def __init__(self):
        self.left = []      # left (max)heap 
        self.right = []     # right (min)heap 

    def addNum(self, num: int) -> None:
        '''TC: O(logn)'''
        if len(self.left) == len(self.right):
            heappush(self.left, -(heappushpop(self.right, num)))
        else:
            heappush(self.right, -(heappushpop(self.left, -num)))

    def findMedian(self) -> float:
        '''TC: O(1)'''
        left_size = len(self.left)
        right_size = len(self.right)
        # empty 
        if left_size == 0: return 0

        # Odd numbers
        if left_size > right_size:
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2
            

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

