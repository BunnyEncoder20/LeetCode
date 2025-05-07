#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        
        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            else:
                if not stack or stack.pop() != brackets[bracket]:
                    return False
        
        # only if stack empty, it's complete
        return len(stack) == 0
# @lc code=end

