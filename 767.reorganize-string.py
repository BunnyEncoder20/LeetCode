#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        # get the freq and construct maxHeap
        fpp = Counter(s)
        heap = [(-freq, char) for char, freq in fpp.items()]
        heapq.heapify(heap) # O(n) operation
        
        # loop through heap
        prev = None
        ans = ""
        while heap or prev:
            # if heap empty, prev char is only available
            if prev and not heap:
                return ""
            
            # get the max freq val and add to ans
            # we know it's not gonna be equal to prev
            # casue prev is not add
            freq, char = heapq.heappop(heap)
            ans += char
            freq += 1           # we adding cause the freq are actually negative

            # add the prev into the heap
            # cause it was excluded previously
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            
            # update prev if it's freq is not 0
            if freq != 0:
                prev = (freq, char)
        
        return ans
        
# @lc code=end

