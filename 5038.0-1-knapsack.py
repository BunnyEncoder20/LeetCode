class Solution:
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
