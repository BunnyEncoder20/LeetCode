'''
You are given an array of positive numbers from 1 to n, such that all numbers 
from 1 to n are present except one number x. You have to find x. 
The input array is not sorted. 
Look at the below array and give it a try before checking the solution.
'''

def find_missing(nums):
    n = len(nums)+1 
    sum1 = sum([n for n in range(1,n)])
    sum2 = sum(nums)
    # Replace this placeholder return statement with your code
    return sum1 - sum2