#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
      n = len(arr)
      low,high = 0, n-1
      while low<=high:
        mid = (low+high)//2
        missing = arr[mid] - (mid+1)
        if missing < k:
          low = mid+1
        else:
          high = mid-1
      return high+1+k
        
# @lc code=end

