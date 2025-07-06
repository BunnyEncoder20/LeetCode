class Solution:
    def sortStack(self, stack):
        # base case
        if len(stack) == 1:
            return
        
        # recursively go down stack
        top = stack.pop()
        self.sortStack(stack)

        # insert current val into sorted stack
        self.insertIntoStack(stack, top)
        return 
    
    def insertIntoStack(self, stack, val):
        # base case
        if not stack or stack[-1] <= val:
            stack.append(val)
            return
        
        # recursively remove top and go down
        top = stack.pop()
        self.insertIntoStack(stack, val)

        # put top back
        stack.append(top)

        return

st = [9,2,3,6,5,1,3,10,8,7]
Solution().sortStack(st)
print(st)
        
