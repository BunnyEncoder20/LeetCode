#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1, max(piles)
        
        while low <= high:
            # rate of rating bananas
            rate = (low+high)//2
            
            # total time for this rate
            time = 0
            for p in piles:
                time += math.ceil(p / rate)
            
            if time > h:
                low = rate+1
            else:
                high = rate-1
        
        return low
            
        
# @lc code=end

