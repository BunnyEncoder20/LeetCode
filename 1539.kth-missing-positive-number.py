#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low, high = 0, len(arr)-1

        while low<=high:
            mid = (low+high)//2
            missing = arr[mid] - (mid+1)

            if missing < k:
                low = mid+1
            else:
                high = mid-1
        
        # ans = arr[high] + (something more)
        # ans = arr[high] + k - (missing[high])
        # ans = arr[high] + k - (arr[high] - (high+1))
        # ans = arr[high] + k - arr[high] + high + 1
        # ans = k + (high + 1)
        # ans = k + (low)
        # return k + high + 1
        return k + low
        
# @lc code=end

