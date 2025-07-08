class Solution1:
    # Recursion
    # Step1: express everything in terms of (index, weight)
    # Step2: Explore all possibilites (Pick and Not Pick)
    # Step3: Return max(pick, not pick)
    def knapsack(self, weights, values, maxW):
        def recursion(i, wt):
            '''Till idx i, what is the max val you can get with weight wt'''
            # base case last item left
            if i == 0:
                if weights[i] <= wt:
                    return values[i]
                else:
                    return 0


            notpick = 0 + recursion(i-1, wt)
            pick = int(-1e9)

            # make sure we can put item in bag first
            if weights[i] <= wt:
                pick = values[i] + recursion(i-1, wt-weights[i])

            return max(pick, notpick)

        n = len(weights)
        return recursion(n-1,maxW)

class Solution2:
    # Memoization
    # idx can be from 0 → n-1 | wt can be from 0 → maxW
    # dp[n][w+1]
    # chk for dp entry, if there return that, else make
    # it and return it
    def knapsack(self, weights, values, maxW):
        def recursion(i, wt):
            # base case
            if i == 0:
                if weights[i] <= wt:
                    return values[i]
                else:
                    return 0

            # check if dp entry
            if dp[i][wt] != -1:
                return dp[i][wt]

            # get pick and not pick values
            notpick = 0 + recursion(i-1, wt)
            pick = int(-1e9)
            if weights[i] <= wt:
                pick = values[i] + recursion(i-1, wt - weights[i])

            # update dp table
            dp[i][wt] = max(pick, notpick)
            return dp[i][wt]

        n = len(weights)
        dp = [[-1]*(maxW+1) for _ in range(n)]
        return recursion(n-1, maxW)
