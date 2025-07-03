#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(opening, closing):
            # base case
            if opening == closing == n:
                res.append("".join(stack))
                return 
            
            # can insert opening bracket
            if opening < n:
                stack.append('(')
                backtracking(opening+1, closing)
                stack.pop()
            
            # can insert closing bracket
            if closing < opening:
                stack.append(')')
                backtracking(opening,closing+1)
                stack.pop()


        backtracking(0,0)
        return res
        
# @lc code=end

