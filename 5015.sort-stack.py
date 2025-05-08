class Solution:
    def sorted(self, stack):
        if len(stack) <= 1:
            return 
        
        top = stack.pop()
        self.sorted(stack)
        self.insert_into_stack(top, stack)
        return
    
    def insert_into_stack(self, val, stack):
        # base case
        if not stack or val >= stack[-1]:
            stack.append(val)
            return
        
        temp = stack.pop()
        self.insert_into_stack(val, stack)
        stack.append(temp)
        return
        

stack = [3,2,1]
Solution().sorted(stack)
print(stack)