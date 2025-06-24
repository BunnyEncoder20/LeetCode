#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for ch in tokens:
            if ch == '+':
                n2, n1 = stack.pop(), stack.pop()
                stack.append(n1+n2)
            elif ch == '-':
                n2, n1 = stack.pop(), stack.pop()
                stack.append(n1-n2)
            elif ch == '*':
                n2, n1 = stack.pop(), stack.pop()
                stack.append(n1*n2)
            elif ch == '/':
                n2, n1 = stack.pop(), stack.pop()

                # use int() to make use to round
                # the result towards 0
                stack.append(int(n1/n2))    

            # case: it's a number
            else:
                stack.append(int(ch))
        
        return stack[0]
                
        
# @lc code=end

