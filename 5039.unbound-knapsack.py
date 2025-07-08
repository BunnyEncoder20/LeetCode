class Solution1:
    def unboundedKnapsack(self, weights, values, n, maxW):
        def recursion(i, current_capacity):
            # base case
            if i == 0:
                if weights[i] <= current_capacity:
                    return values[i]
                else:
                    return 0
            
            notpick = 0 + recursion(i-1, current_capacity)
            pick = int(-1e9)
            if weights[i] <= current_capacity:
                pick = values[i] + recursion(i, current_capacity-weights[i])
            
            return max(pick, notpick)
        
        return recursion(n-1, maxW)
            
        
        