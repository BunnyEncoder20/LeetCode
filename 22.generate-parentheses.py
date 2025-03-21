#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursive(open, closed):
            # base case : open == closed == n
            if open == closed == n:
                res.append("".join(stack))
                return 
            
            # normally
            # can only add open if open < n
            if open < n:
                stack.append("(")
                recursive(open+1, closed)
                stack.pop()     # backtrack
            
            # can only add closed if closed < open
            if closed < open:
                stack.append(")")
                recursive(open, closed+1)
                stack.pop()
        
        stack = []
        res = []
        recursive(0,0)
        return res
        
# @lc code=end

