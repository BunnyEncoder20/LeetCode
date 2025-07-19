'''
Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
1 <= s.length <= 3 * 10^5
'+', '-', '*', '/'

Example 1:
Input: s = "3+2*2" = [3,"+",2,"*",2]
Output: 7
'''

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'

        for i, char in enumerate(s):
            # Build the current number
            if char.isdigit():
                num = num * 10 + int(char)

            # Process when we hit an operator or reach the end
            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    # Handle division with truncation toward zero
                    prev = stack.pop()
                    if prev < 0:
                        stack.append(-(-prev // num))
                    else:
                        stack.append(prev // num)

                # Update sign for next iteration
                sign = char
                num = 0

        return sum(stack)

# Test cases
sol = Solution()
print(sol.calculate("3+2*2"))  # Expected: 7
print(sol.calculate(" 3/2 "))  # Expected: 1
print(sol.calculate(" 3+5 / 2 "))  # Expected: 5
print(sol.calculate("14-3*2"))  # Expected: 8
print(sol.calculate("-3*2+1"))  # Expected: -5
