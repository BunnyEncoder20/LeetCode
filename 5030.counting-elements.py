# Brute Force
def brute_countingElements(a,b):
    res = []
    for n1 in a:
        count = 0
        for n2 in b:
            if n2 <= n1:
                count += 1
        res.append(count)
    return res 

# Raw Binary search (upper bound)
def countingElements(a,b):
    # helper func
    def bsearch(target):
        low, high = 0, len(b)-1
        while low<=high:
            mid = (low+high)//2
            if b[mid] <= target:
                low = mid+1
            else:
                high = mid-1
        return low

    b.sort()
    res = []
    for n1 in a:
        count = bsearch(n1)
        res.append(count)
    return res

# using built in functions
import bisect
def countingElements_Bisect(a,b):
    b.sort()
    res = []
    for n1 in a:
        count = bisect.bisect_right(b,n1)
        res.append(count)
    return res