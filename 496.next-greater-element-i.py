#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        m = len(nums1)
        nge_mpp = {k:-1 for k in nums2}
        stack = []
        
        for i in range(n-1,-1,-1):
            element = nums2[i]
            while stack and stack[-1] <= element:
                stack.pop()
            if stack:
                nge_mpp[element] = stack[-1]
            stack.append(element)
        
        ans = []
        for k in nums1:
            ans.append(nge_mpp[k])
        return ans
        
# @lc code=end

