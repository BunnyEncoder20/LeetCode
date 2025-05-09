#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # init 
        n = len(nums)
        dq = deque()
        ans = []
        
        for i in range(n):
            # maintain window 
            if dq and dq[0] < i-k+1:
                dq.popleft()
            
            # maintain monotonic stack
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            
            # add the new element
            dq.append(i)
            
            # if k elements, start
            # adding max to ans
            if i >= k-1:
                ans.append(nums[dq[0]])
        
        return ans
# @lc code=end

