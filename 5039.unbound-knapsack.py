class Solution1:
    def unboundedKnapsack(self, weights, values, n, maxW):
        def recursion(i, current_capacity):
            # base case
            if i == 0:
                # calc and return the max value for remaining capacity
                if weights[i] <= current_capacity:
                    return (current_capacity // weights[0]) * (values[0])
                else:
                    return 0 

            notpick = 0 + recursion(i-1, current_capacity)
            pick = int(-1e9)
            if weights[i] <= current_capacity:
                # to pick same item mulitple times, don't move i
                pick = values[i] + recursion(i, current_capacity-weights[i])

            return max(pick, notpick)

        return recursion(n-1, maxW)

class Solution2:
    def unboundedKnapsack(self, weights, values, n, maxW):
        def recursion(i, current_capacity):
            # base case
            if i == 0:
                # calc and return the max value for remaining capacity
                if weights[i] <= current_capacity:
                    return (current_capacity // weights[0]) * (values[0])
                else:
                    return 0

            notpick = 0 + recursion(i-1, current_capacity)
            pick = int(-1e9)
            if weights[i] <= current_capacity:
                # to pick same item mulitple times, don't move i
                pick = values[i] + recursion(i, current_capacity-weights[i])

            return max(pick, notpick)

        dp = [[-1]*(maxW+1) for _ in range(n)]
        return recursion(n-1, maxW)
