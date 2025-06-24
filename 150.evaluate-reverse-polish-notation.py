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
        operators = ('+','-','*','/')

        for ch in tokens:

            # if it's a operator
            if ch in operators:
                # check if there are 2 nums to pop in stk
                if len(stack)<2:
                    raise ValueError(f"Not enough operands before operator '{ch}'")

                n2, n1 = stack.pop(), stack.pop()
                if ch=="+":
                    stack.append(n1+n2)
                elif ch=="-":
                    stack.append(n1-n2)
                elif ch=="*":
                    stack.append(n1*n2)
                elif ch=="/":
                    # remember int for rounding towards 0
                    stack.append(int(n1/n2))
            
            # if it's a number
            else:
                # try to insert,
                try:
                    stack.append(int(ch))
                
                # unless not int
                except ValueError:
                    raise ValueError(f"Invalid token: '{ch}'")

        
        # check if stack
        return stack[0]
                
        
# @lc code=end

