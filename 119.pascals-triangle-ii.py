#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascalRow(n):
            ans = [0]*(n)
            ans[0] = 1
            
            for i in range(1, n):
                ans[i] = ans[i-1] * (n - i)
                ans[i] //= i
            
            return ans
        
        return pascalRow(rowIndex+1)
        
# @lc code=end

