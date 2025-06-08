#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq
import bisect
class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        '''TC: O(logN):lookup + O(N):insertion = O(n):overall'''
        bisect.insort(self.stream, num)

    def findMedian(self) -> float:
        '''TC: O(1)'''
        n = len(self.stream)
        if n%2==0:
            return (self.stream[n//2] + self.stream[(n//2)-1])/2
        else:
            return self.stream[n//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

