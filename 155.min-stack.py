#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        # Case 1: stack is empty, simply push val
        if not self.stack:
            self.mini = val
            self.stack.append(val)
        
        # Case 2: stack has elements
        else:

            # sub case 2.1: the val is greater
            # means mini will not get modified
            if val > self.mini:
                self.stack.append(val)
            
            # sub case 2.2: the val < mini
            # encode the val and push into stack
            else:
                prev_min = self.mini
                encoded_val = (2*val - prev_min)    # use this formula later
                self.mini = val                     # val which came became min
                self.stack.append(encoded_val)      # encoded pushed into stack


    def pop(self) -> None:
        # case 1: stack is empty 
        if not self.stack:
            return None
        
        # case 2: the element > mini 
        # It's normal val ∴ mini unchanged
        top_element = self.stack.pop()

        # Case 3: if the top was smaller than mini, 
        # its encoded val ∴ mini will change
        if top_element < self.mini:
            val = self.mini                 # that original val was made mini
            encoded_val = top_element       # encode val was pushed into stack
            prev_min = 2*val - encoded_val  # from formula

            # restore prev min
            self.mini = prev_min
        
        return

        

    def top(self) -> int:
        # case 1: stk empty
        if not self.stack:
            return None
        
        top_element = self.stack[-1]

        # case 2: it's a normal val
        if self.mini <= top_element:
            return top_element
        
        # case 3: it's a encoded val
        else:
            return self.mini
        

    def getMin(self) -> int:
        # no mini yet
        if self.mini == float('inf'):
            return None

        return self.mini
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

