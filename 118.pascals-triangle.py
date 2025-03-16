#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def getRow(n):
            row = [0]*(n)
            row[0] = 1
            for i in range(1,n):
                row[i] = row[i-1] * (n - i)
                row[i] //= i
            return row
        
        ans = []
        for row in range(numRows):
            ans.append(getRow(row+1))
        return ans

            
        
# @lc code=end

